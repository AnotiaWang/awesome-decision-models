# Contributing

**English** | **[简体中文](#贡献指南)**

Thanks for helping grow this list. [Awesome Decision Models](README.md) is a community catalog of decision models (System One / typed decision models such as Jev, Clef, d1, Laya, or Kev) and the things built around them.

This repository is community-maintained and not affiliated with any model provider.

## What belongs here

- Decision models, hosted or open-weight: a state plus caller-defined questions in, a probability per answer out, no generated text.
- Runtimes, gateways, and inference techniques that serve such models or get the same behavior from existing models.
- Open-source applications, libraries, MCP servers, skills, and substantial demos that use a decision model in a meaningful way.
- Benchmarks, leaderboards, evaluations, and papers about decision models.
- High-signal articles, talks, and cookbooks that help people build.

Please skip:

- Closed-source products with no public write-up or demo.
- Trivial “hello world” gists that only repeat the official quick start.
- Walkthroughs, release roundups, or “what is a decision model?” guides that restate vendor docs without original measurement, code, or a new failure mode.
- Marketing posts, waitlist spam, or content that is not about decision models.
- Benchmark claims without a public method: say which benchmark and who ran it.
- Anything that is just a wrapper around someone else's already-listed project.

## How to add an item

1. Fork this repo.
2. Add the project to **both** [README.md](README.md) and [README_zh.md](README_zh.md), in the same section and the same relative position. Official items stay first; community items go with similar projects. Hosted APIs are ordered by release date.
3. Use this format:

   ```markdown
   - [Project Name](https://github.com/org/repo) - One sentence: what it does and which decision model it uses, and how.
   ```

4. Keep the description short. Link the repo or canonical page, not a tracking URL.
5. If the project is an unofficial client or integration for a vendor's API, say so in the blurb.
6. Open a pull request. In the PR body, include: what the project is, which decision model it uses and how, and why it is interesting.

New sections are fine when a category has three or more items.

## Style

- American English in `README.md`; Simplified Chinese in `README_zh.md`.
- Sentence case. No trailing period unless the description has multiple sentences.
- No emoji in list entries. No star-count badges (they go stale).
- Do not paste secrets or API keys.

## Related

If you are not sure a project fits, open an issue first.

---

# 贡献指南

感谢帮忙扩充这份列表。[Awesome Decision Models](README_zh.md) 收集决策模型（System One 模型 / 类型化决策模型，如 Jev、Clef、d1、Laya、Kev）以及围绕它们构建的项目。

本仓库由社区维护，与任何模型厂商无隶属关系。

## 什么适合收录

- 决策模型，托管或开源权重均可：输入状态和调用方定义的问题，为每个答案输出概率，不生成文本。
- 托管这类模型的运行时、网关，以及让现有模型表现出同样行为的推理方法。
- 真正用到决策模型的开源应用、库、MCP 服务、skill，以及有分量的 demo。
- 关于决策模型的 benchmark、排行榜、评测和论文。
- 对动手有帮助的高质量文章、演讲和 cookbook。

请不要提交：

- 没有公开说明或 demo 的闭源产品。
- 只是复述官方 quick start 的 hello world。
- 没有独立实测、代码或新失败模式的走读、发布综述、「决策模型是什么」指南。
- 营销软文、候补名单广告，或与决策模型无关的内容。
- 没有公开方法的跑分结论：请写明是哪个 benchmark、由谁跑的。
- 只是给列表里已有项目再包一层的包装器。

## 如何添加条目

1. Fork 本仓库。
2. **同时**改 [README.md](README.md) 和 [README_zh.md](README_zh.md)，放进同一章节、同一相对位置。官方条目靠前，社区条目跟同类项目放在一起。托管 API 按发布时间排序。
3. 格式：

   ```markdown
   - [项目名](https://github.com/org/repo) - 一句话：它做什么，用的是哪个决策模型、怎么用。
   ```

4. 简介保持短。链到仓库或权威页面，不要用带追踪参数的链接。
5. 如果是某家厂商 API 的非官方客户端或集成，请在简介里写明。
6. 提交 PR。正文说明：项目是什么、用的是哪个决策模型以及怎么用、为什么值得收录。

某一类满 3 个条目时，可以新开章节。

## 文风

- `README.md` 用美式英语；`README_zh.md` 用简体中文。
- 条目描述用短句。不要在列表项里用 emoji，也不要加星标数徽章。
- 不要粘贴密钥或 API key。

不确定是否适合收录时，可以先开 issue。
