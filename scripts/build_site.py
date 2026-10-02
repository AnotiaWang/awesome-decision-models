#!/usr/bin/env python3
"""Build the GitHub Pages site from README.md and README_zh.md.

The two READMEs are the only source of truth. This script parses both,
pairs English and Chinese entries by URL, and renders one static page
that switches language on the client.

    python3 scripts/build_site.py            # build into _site/
    python3 scripts/build_site.py --strict   # also fail if the READMEs drift apart

Standard library only, so CI needs nothing but Python 3.
"""

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
SITE_SRC = ROOT / "site"
DEFAULT_REPO = "AnotiaWang/awesome-decision-models"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
ENTRY_RE = re.compile(r"^\[([^\]]+)\]\(([^)\s]+)\)(?:\s+-\s+(.*))?$")
CODE_RE = re.compile(r"`([^`]+)`")


# --- Parsing ---------------------------------------------------------------


def parse(path):
    """Return {"intro": [str], "sections": [section]} for one README.

    section = {"title", "subsections": [{"title" | None, "blocks"}]}
    block   = ("note", text) | ("list", [item])
    item    = {"text", "children": [item]}
    """
    doc = {"intro": [], "sections": []}
    section = sub = None

    def blocks():
        return sub["blocks"]

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line or line.startswith("# "):
            continue
        if line.startswith("## "):
            sub = {"title": None, "blocks": []}
            section = {"title": line[3:].strip(), "subsections": [sub]}
            doc["sections"].append(section)
        elif line.startswith("### "):
            sub = {"title": line[4:].strip(), "blocks": []}
            section["subsections"].append(sub)
        elif section is None:
            # Skip the language switcher; keep the rest of the intro.
            if "README" not in line:
                doc["intro"].append(line)
        elif line.startswith("- "):
            item = {"text": line[2:].strip(), "children": []}
            if blocks() and blocks()[-1][0] == "list":
                blocks()[-1][1].append(item)
            else:
                blocks().append(("list", [item]))
        elif re.match(r"^\s+- ", line):
            blocks()[-1][1][-1]["children"].append({"text": line.strip()[2:], "children": []})
        else:
            blocks().append(("note", line.strip()))

    # Drop the table of contents: a section whose links all point in-page.
    def is_toc(s):
        items = [i for sub in s["subsections"] for kind, b in sub["blocks"] if kind == "list" for i in b]
        return items and all(primary_url(i) and primary_url(i).startswith("#") for i in items)

    doc["sections"] = [s for s in doc["sections"] if not is_toc(s)]
    return doc


def primary_url(item):
    m = ENTRY_RE.match(item["text"])
    return m.group(2) if m else None


def list_items(doc):
    for s in doc["sections"]:
        for sub in s["subsections"]:
            for kind, b in sub["blocks"]:
                if kind == "list":
                    yield from b


# --- Rendering -------------------------------------------------------------


def github_slug(title):
    """Anchor GitHub generates for a heading."""
    slug = title.strip().lower()
    slug = re.sub(r"[^\w\- ]", "", slug)
    return slug.replace(" ", "-")


class Renderer:
    def __init__(self, repo, anchors):
        self.repo = repo
        self.anchors = anchors

    def href(self, url):
        if url.startswith("#"):
            return "#" + self.anchors.get(url[1:], url[1:])
        if re.match(r"^[a-z]+:", url):
            return url
        return f"https://github.com/{self.repo}/blob/main/{url}"

    def inline(self, text):
        """Render the inline Markdown used in the READMEs: code, links, bold, italic."""
        codes = []

        def stash(m):
            codes.append(f"<code>{html.escape(m.group(1))}</code>")
            return f"\x00{len(codes) - 1}\x00"

        out = html.escape(CODE_RE.sub(stash, text), quote=False)

        def link(m):
            label, url = m.group(1), html.unescape(m.group(2))
            href = html.escape(self.href(url))
            ext = "" if href.startswith("#") else ' target="_blank" rel="noopener"'
            return f'<a href="{href}"{ext}>{label}</a>'

        out = LINK_RE.sub(link, out)
        out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
        out = re.sub(r"(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])", r"<em>\1</em>", out)
        return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], out)

    def bilingual(self, en, zh, tag="span", cls=""):
        """Both languages side by side; CSS shows the active one."""
        c = f" {cls}" if cls else ""
        if en == zh:
            return f'<{tag} class="both{c}">{en}</{tag}>'
        return (
            f'<{tag} class="l-en{c}" lang="en">{en}</{tag}>'
            f'<{tag} class="l-zh{c}" lang="zh-CN">{zh}</{tag}>'
        )

    def item(self, en, zh):
        m_en, m_zh = ENTRY_RE.match(en["text"]), ENTRY_RE.match(zh["text"])
        search = plain(en["text"]) + " " + plain(zh["text"])
        if m_en:
            name_en, url, desc_en = m_en.group(1), m_en.group(2), m_en.group(3) or ""
            name_zh, desc_zh = (m_zh.group(1), m_zh.group(3) or "") if m_zh else (name_en, desc_en)
            name = self.bilingual(self.inline(name_en), self.inline(name_zh))
            href = html.escape(self.href(url))
            head = (
                f'<div class="entry-head"><a class="entry-name" href="{href}" target="_blank" rel="noopener">{name}</a>'
                f'<span class="host">{html.escape(host_label(url))}</span></div>'
            )
            desc = self.bilingual(self.inline(desc_en), self.inline(desc_zh), "p", "desc") if desc_en else ""
            body = head + desc
        else:
            body = self.bilingual(self.inline(en["text"]), self.inline(zh["text"]), "p", "desc")

        kids = ""
        if en["children"]:
            zkids = zh["children"] if len(zh["children"]) == len(en["children"]) else en["children"]
            kids = '<ul class="children">' + "".join(
                f"<li>{self.item(a, b)[0]}</li>" for a, b in zip(en["children"], zkids)
            ) + "</ul>"
        return body + kids, search


def plain(text):
    """Searchable text: link labels and URLs, without Markdown syntax."""
    text = LINK_RE.sub(lambda m: f"{m.group(1)} {m.group(2)}", text)
    return re.sub(r"[`*]", "", text)


def host_label(url):
    p = urlparse(url)
    host = p.netloc.removeprefix("www.")
    parts = [x for x in p.path.split("/") if x]
    if host in ("github.com", "huggingface.co") and len(parts) >= 2:
        if parts[0] == "spaces" and len(parts) >= 3:
            return f"{host}/spaces/{parts[1]}"
        return f"{host}/{parts[0]}"
    return host


# --- Pairing ---------------------------------------------------------------


def build(en_doc, zh_doc, repo, problems):
    if len(en_doc["sections"]) != len(zh_doc["sections"]):
        sys.exit(
            f"error: README.md has {len(en_doc['sections'])} sections, "
            f"README_zh.md has {len(zh_doc['sections'])}. Headings must match one to one."
        )

    zh_by_url = {}  # url -> (item, section index)
    for i, s in enumerate(zh_doc["sections"]):
        for it in list_items({"sections": [s]}):
            url = primary_url(it)
            if url:
                zh_by_url[url] = (it, i)
    en_urls = {primary_url(it) for it in list_items(en_doc)} - {None}
    for url in zh_by_url.keys() - en_urls:
        problems.append(f"only in README_zh.md: {url}")

    anchors = {}
    for s_en, s_zh in zip(en_doc["sections"], zh_doc["sections"]):
        sid = github_slug(s_en["title"])
        anchors[github_slug(s_zh["title"])] = anchors[sid] = sid
    r = Renderer(repo, anchors)

    sections, toc, footer = [], [], []
    total = 0
    for s_index, (s_en, s_zh) in enumerate(zip(en_doc["sections"], zh_doc["sections"])):
        sid = github_slug(s_en["title"])
        title = r.bilingual(html.escape(s_en["title"]), html.escape(s_zh["title"]))
        has_items = any(kind == "list" for sub in s_en["subsections"] for kind, _ in sub["blocks"])
        if not has_items:
            # Prose-only sections (Contribute, License) go in the footer.
            notes_zh = [b for sub in s_zh["subsections"] for kind, b in sub["blocks"] if kind == "note"]
            notes_en = [b for sub in s_en["subsections"] for kind, b in sub["blocks"] if kind == "note"]
            if len(notes_zh) != len(notes_en):
                notes_zh = notes_en
            body = "".join(r.bilingual(r.inline(a), r.inline(b), "p") for a, b in zip(notes_en, notes_zh))
            footer.append(f'<div class="footer-block"><h3>{title}</h3>{body}</div>')
            continue

        count = 0
        parts = []
        zsubs = s_zh["subsections"]
        if len(zsubs) != len(s_en["subsections"]):
            problems.append(f"section '{s_en['title']}' has different ### subsections in the two READMEs")
            zsubs = s_en["subsections"]
        for sub_en, sub_zh in zip(s_en["subsections"], zsubs):
            if sub_en["title"]:
                sub_id = f"{sid}-{github_slug(sub_en['title'])}"
                stitle = r.bilingual(html.escape(sub_en["title"]), html.escape(sub_zh["title"] or sub_en["title"]))
                parts.append(f'<h3 id="{sub_id}">{stitle}</h3>')
            notes_zh = [b for kind, b in sub_zh["blocks"] if kind == "note"]
            notes_en = [b for kind, b in sub_en["blocks"] if kind == "note"]
            if len(notes_zh) != len(notes_en):
                problems.append(f"section '{s_en['title']}' has different intro paragraphs in the two READMEs")
                notes_zh = notes_en
            note_i = 0
            for kind, block in sub_en["blocks"]:
                if kind == "note":
                    parts.append(r.bilingual(r.inline(block), r.inline(notes_zh[note_i]), "p", "note"))
                    note_i += 1
                    continue
                lis = []
                for it in block:
                    url = primary_url(it)
                    zh, zh_index = zh_by_url.get(url, (None, None)) if url else (None, None)
                    if zh is None:
                        problems.append(f"missing from README_zh.md: {url or it['text'][:60]}")
                        zh = it
                    elif zh_index != s_index:
                        problems.append(f"in a different section in README_zh.md: {url}")
                    inner, search = r.item(it, zh)
                    lis.append(f'<li class="entry" data-search="{html.escape(search.lower())}">{inner}</li>')
                    count += 1
                parts.append('<ul class="entries">' + "".join(lis) + "</ul>")

        total += count
        sections.append(
            f'<section class="section" id="{sid}" data-section>'
            f'<h2><a class="anchor" href="#{sid}">{title}</a> <span class="count" data-count>{count}</span></h2>'
            + "".join(parts)
            + "</section>"
        )
        toc.append(
            f'<li><a href="#{sid}" data-toc="{sid}">{title}</a> <span class="count" data-toc-count="{sid}">{count}</span></li>'
        )

    intro_en, intro_zh = en_doc["intro"], zh_doc["intro"]
    if len(intro_zh) != len(intro_en):
        problems.append("the intro paragraphs differ in number between the two READMEs")
        intro_zh = intro_en
    tagline = r.bilingual(r.inline(intro_en[0]), r.inline(intro_zh[0]), "p", "tagline") if intro_en else ""
    intro = "".join(r.bilingual(r.inline(a), r.inline(b), "p") for a, b in zip(intro_en[1:], intro_zh[1:]))

    return {
        "TAGLINE": tagline,
        "INTRO": intro,
        "TOC": "".join(toc),
        "SECTIONS": "".join(sections),
        "FOOTER": "".join(footer),
        "TOTAL": str(total),
        "DESCRIPTION": html.escape(plain(intro_en[0]) if intro_en else "", quote=True),
    }


def commit_info():
    sha = os.environ.get("GITHUB_SHA")
    try:
        sha = sha or subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        when = subprocess.check_output(["git", "show", "-s", "--format=%cI", sha], cwd=ROOT, text=True).strip()
        date = datetime.fromisoformat(when).astimezone(timezone.utc).strftime("%Y-%m-%d")
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return sha or "", date


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=str(ROOT / "_site"), help="output directory (default: _site)")
    ap.add_argument("--strict", action="store_true", help="exit 1 if the two READMEs are out of sync")
    args = ap.parse_args()

    repo = os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPO)
    problems = []
    values = build(parse(ROOT / "README.md"), parse(ROOT / "README_zh.md"), repo, problems)
    sha, date = commit_info()
    values.update(REPO=repo, SHA=sha, SHORT_SHA=sha[:7], DATE=date)

    page = (SITE_SRC / "index.html").read_text(encoding="utf-8")
    page = re.sub(r"\{\{(\w+)\}\}", lambda m: values[m.group(1)], page)

    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(SITE_SRC, out)
    (out / "index.html").write_text(page, encoding="utf-8")

    for p in problems:
        # GitHub Actions turns these into annotations on the PR.
        print(f"::{'error' if args.strict else 'warning'}::{p}" if os.environ.get("CI") else f"warning: {p}")
    print(f"built {out}/index.html: {values['TOTAL']} entries, {len(problems)} sync problem(s)")
    if problems and args.strict:
        print("README.md and README_zh.md must list the same links in the same sections.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
