# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of applications, libraries, tools, and research built with [Jev](https://docs.typesafe.ai/introduction).

**[English](README.md)** | **[简体中文](README_zh.md)**

Unofficial, not affiliated with [TypeSafe AI](https://typesafe.ai). Public access opened 21 September 2026 — keys from the [console](https://console.typesafe.ai/settings/keys). Pull requests welcome.

## Contents

- [Official](#official)
- [Community](#community)
- [SDKs & Clients](#sdks--clients)
- [Applications](#applications)
- [Demos & Games](#demos--games)
- [Agent Tools](#agent-tools)
- [Research & Open Models](#research--open-models)
- [Articles](#articles)
- [Contribute](#contribute)

## Official

- [Documentation](https://docs.typesafe.ai/introduction) - API, SDKs, [cookbooks](https://docs.typesafe.ai/llms.txt), and [patterns](https://docs.typesafe.ai/patterns)
- [Playground](https://console.typesafe.ai/playground)
- [Console](https://console.typesafe.ai) - Keys and usage
- [GitHub](https://github.com/typesafe-ai)
- [Workflow evals](https://evals.typesafe.ai)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) - Known failure modes
- [Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) - Hosted `typesafe-ai/jev`

## Community

- [Discord](https://discord.gg/typesafe) - Builder demos in [Show and Tell](https://discord.com/channels/1483217544214085663/1483217545040232493)
- [X @typesafeai](https://x.com/typesafeai)

## SDKs & Clients

Official first, then community clients. Community packages are not affiliated with TypeSafe unless noted.

- [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) - Official client. `pip install typesafe-sdk`. Docs: [Python SDK](https://docs.typesafe.ai/sdk/python).
- [JavaScript / TypeScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) - Official client. `npm install @typesafe-ai/sdk`. Docs: [JavaScript SDK](https://docs.typesafe.ai/sdk/javascript).
- [System One adapter (Python)](https://github.com/typesafe-ai/system-one-adapter-python) - Official drop-in `TypeSafeClient` replacement backed by LLM APIs, for comparing Jev against chat models on the same questions. `pip install system-one-adapter`.
- [Vercel AI SDK provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) - `@ai-sdk/typesafe-ai` plus `experimental_evaluate`. Use `typeSafeAi.evaluationModel('jev-latest')` or the Gateway id `typesafe-ai/jev`.
- [Milvus Model](https://github.com/milvus-io/milvus-model) - Python reranker adapter that sends candidate documents as Jev Noul questions in one request, then sorts the returned scores and preserves original document indices
- [Elixir SDK](https://github.com/nshkrdotcom/typesafe_sdk) - Community Hex package [`typesafe_sdk`](https://hex.pm/packages/typesafe_sdk) for `system_one` and model listing. Docs: [HexDocs](https://hexdocs.pm/typesafe_sdk).
- [Jev (Elixir OTP)](https://github.com/dannote/jev) - Hex package [`jev`](https://hex.pm/packages/jev): Jev as a peer GenServer; answers arrive as messages you pattern-match, with network-free tests
- [Ruby SDK](https://github.com/joshmn/typesafe-sdk) - Community Ruby 3.1+ client: Noul / Choice / Score, retries, model listing, thread-safe pooled HTTP. No async client.
- [RubyLLM TypeSafe](https://github.com/kieranklaassen/ruby_llm-typesafe) - TypeSafe provider for RubyLLM 2 with offline model metadata and typed responses.
- [typesafe-ai-rails](https://github.com/GenieRobot/typesafe-ai-rails) - Rails integration on top of the official Python SDK: config, usage/cost telemetry, opt-in confidence policies.
- [Rust SDK (typesafe-ai-rs)](https://github.com/gilljon/typesafe-ai-rs) - Independent async and blocking client for System One.
- [TypeSafe AI for Rust](https://github.com/Twister915/typesafe-ai) - Another Rust client: async + blocking transports, typed responses, observable retries.
- [typesafe-rs](https://github.com/AbdelStark/typesafe-rs) - Latency-focused Rust transport SDK aiming for behavioral parity with the official clients.
- [s1-rs](https://github.com/AbdelStark/s1-rs) - Rust derive layer for Choice / Score / Noul, typed question sets, confidence gates, and network-free tests.
- [Advocaat](https://github.com/pithings/advocaat) - Small TypeScript client with tagged helpers for chances, choices, and scores.
- [Scala / ZIO SDK](https://github.com/jamesward/zio-typesafe-ai) - Community ZIO client with a small DSL for noul / choice / score.
- [.NET SDK](https://github.com/saibimajdi/typesafe-dotnet-sdk) - Community client for typed questions and confidence-scored answers.
- [PHP SDK](https://github.com/Butochnikov/typesafe-sdk-php) - Unofficial PHP client: typed DTOs, promises, and exceptions. Used by the Laravel package below.
- [Laravel TypeSafe Jev](https://github.com/Butochnikov/laravel-typesafe-jev) - Unofficial Laravel 12/13 integration: config, facade, scoped DI, and a recording fake on the PHP SDK.
- [jev-go](https://github.com/Gaurav-Gosain/jev-go) - Unofficial Go client for typed judgments and calibrated probabilities. `go get github.com/Gaurav-Gosain/jev-go`.
- [Stumble/jev-go](https://github.com/Stumble/jev-go) - Unofficial dependency-free Go SDK for TypeSafe direct and Vercel AI Gateway, with typed questions, retries, an interactive CLI, and an installable agent skill
- [jevclient](https://github.com/AboveColin/jevclient) - Unofficial async Python client (`pip install jevclient`). Typed Noul / Choice / Score helpers, separate from the official `typesafe-sdk`.
- [LlamaIndex Jev](https://github.com/WiktorB2004/llama-index-jev) - Unofficial LlamaIndex reranker (`JevRerank`) and router (`JevSingleSelector` / `JevMultiSelector`) on the official Python SDK
- [Swift SDK](https://github.com/ainame/swift-typesafe) - Unofficial Swift 6.4 client aligned with the Python SDK 0.6.0 API, including Linux
- [TypeSafe AI Swift SDK](https://github.com/alterhq/typesafe-sdk-swift) - Unofficial dependency-free Swift 6 client for Choice / Score / Noul, with strict concurrency, configurable authentication and retries, and network-free tests
- [discern](https://github.com/doeixd/discern) - Unofficial Effect library: Choice / Noul / Score answers become typed patterns with an explicit `Uncertain` branch you must handle, plus routable procedures, with recording, replay, caching and call budgets as `DecisionModel` middleware. Provider-neutral; reaches Jev through `@effect/ai-typesafe`
- [kojev (Kotlin Multiplatform)](https://github.com/ItisNoMatter/kojev) - Community client for JVM, Android, and iOS. Choice and Score answers come back as your own enums; one typed way to read them, no default thresholds. Maven Central: `io.github.itisnomatter:kojev:0.1.0`.
- [jev4k](https://github.com/pambrose/jev4k) - Unofficial JVM Kotlin client: Choice, Score, and Noul as a DSL, with answers read back as typed values including enums. Maven Central: `com.pambrose:jev4k`
- [hunch](https://github.com/steven-shoemaker/hunch) - Unofficial Python library, with a TypeScript port, that turns Choice / Score / Noul into functions over lists and DataFrames (classify, score, check, where, extract, pick, rank, verify), with deduplication, caching, and optional escalation of unsure rows to an LLM that must pick from the same labels

- [JevT++](https://github.com/wiatrM/jevtpp) - Unofficial C++20 library with compile-time enum schemas, typed decisions and abstention, local Laya backends, and an optional TypeSafe System One HTTP client; remote tests use mocks and loopback HTTP, not live-provider validation

## Applications

Open-source products and demos that put Jev in a real loop.

- [MemSearch](https://github.com/zilliztech/memsearch) - Markdown memory for coding agents with an optional Jev Noul reranker and a published English/Chinese retrieval evaluation; community integration, not an official TypeSafe SDK
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) - Browser agent from [Browser Use](https://github.com/browser-use). Jev picks an operation and a DOM element in one request; a small LLM writes text only for `TYPE_TEXT`. Zürich → London on Google Flights in ~7s. Library, local inspector, and measurements included.
- [Jev Social](https://github.com/socai-io/jev-social) - Browser-grounded social research: Jev selects bounded Instagram, TikTok, and LinkedIn search/read operations, socai executes them in the user's Chrome, and reports cite the captured posts, comments, and video evidence; unofficial community project
- [Jev Web Analyzer](https://github.com/replynodes/jev-web-analyzer) - Community project that analyzes a public SaaS landing page as clean Markdown and asks Jev ten bounded `Choice` questions about first-visit understanding, including the first change to make.
- [jev-align (Sutro)](https://github.com/sutro-sh/jev-align) - Unofficial active-learning CLI that evaluates CSV, Parquet, and JSONL rows with Jev, asks people to label uncertain and audit samples, and uses GEPA to propose improved definitions
- [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome) - Unofficial Chrome extension (Manifest V3) port of Jev Ultrafast: Jev picks the operation and DOM element in one request, a small text model writes typed values, and it runs in the user's own tabs through OpenRouter, TypeSafe or Cloudflare; includes a 17-task headless-Chromium suite with recorded traces.
- [jev-ego](https://github.com/romaluev/jev-ego) - Browser agent on [ego lite](https://lite.ego.app/): one TypeSafe request picks operation + indexed element; agent-facing observe/act/suggest/step CLI
- [jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) - Unofficial browser automation: an LLM plans the outcome, Jev decides each click/type on a Playwright snapshot (~300 ms/call). Ships as a library, CLI, and MCP server (`npx -y -p jev-browser jev-browser-mcp`).
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - macOS computer-use loop: OCR the screen, Jev classifies the next action, then click. About $0.0002/step.
- [Yappy](https://yappy.biz/jev/) - macOS voice agent (closed source, public write-up with measurements). On its hosted plan Jev picks the operation and target control from the window's accessibility table each step; a chat model writes text only for typing, and the full agent takes over when confidence drops. Author-reported: 275–690 ms per decision, $0.003 for five.
- [Mobile Jev](https://github.com/droidrun/mobile-jev) - Android agent on [Mobilerun](https://mobilerun.ai): Jev decides each tap. Opens Uber, SFO → Golden Gate, payment screen in ~21s / 9 actions. Live studio, CLI, and traces. No ADB.
- [Unclutter](https://github.com/kitze/unclutter) - Chrome / Firefox extension: Jev classifies nonessential page elements; local template rules hide them on later visits.
- [jevMail](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling) - Unofficial open-source Gmail AI spam filter, auto-labeler, and inbox organizer: Jev understands each email's intent to apply custom labels and optionally archive high-confidence unwanted mail
- [TypeSafe AdBlock](https://github.com/realZachi/typesafe-adblock) - Chrome extension: Jev judges whether a DOM element is an ad and removes it. BYOK, no backend. Author calls it a demo, not a real ad blocker
- [HA-Jev](https://github.com/AboveColin/HA-Jev) - Unofficial Home Assistant integration: typed questions about entity state become sensors and automation actions, with a target picker that builds the state from the user's own entities and usage, cost, and daily-budget entities alongside the answers
- [Every](https://github.com/sufianetaouil/every) - Semantic code-search CLI: a yes/no question against every function, ranked by Noul probability.
- [JevPDF](https://github.com/kylemclaren/jevpdf) - Unofficial Ctrl+F by meaning for PDFs: pdf.js extracts lines in the browser, Jev answers one Noul per line on whether it answers the query, and matching lines light up ranked by probability
- [blink](https://github.com/ellipsis-dev/blink) - Codebase search: an ensemble of walkers asks Jev which file answers a natural-language query
- [Jev Search](https://github.com/superagents-lab/jev-search) - Unofficial web search app using Jev's Choice and Noul judgments to select sources, time ranges, and query candidates, then rank results retrieved through Search1API
- [Jev Reranker (Rust CLI)](https://github.com/shinpr/jev-reranker) - Unofficial JSON-in/JSON-out CLI that uses Jev `Noul` judgments to rerank search results, filter documents without usable evidence, or extract query-specific passages
- [jevsearch](https://github.com/kylemclaren/jevsearch) - Unofficial shadcn/ui site-search block: keyword hits appear on the first keystroke, then one Jev request re-ranks the top 20 with a Noul per page, a Choice for the best answer, and a Noul for whether any page answers
- [jev-research-pipeline](https://github.com/shimo4228/jev-research-pipeline) - Unofficial experimental research monitor: Jev screens papers and other sources against each open research question (Noul gates, Score dimensions), code applies thresholds, and Qwen writes question-centric notes into an Obsidian vault
- [neo4jev](https://github.com/jexp/neo4jev) - Neo4j graph navigation: at each node Jev chooses which relationship to follow, with beam search over log-probabilities
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) - Experimental Hono router: Jev matches an incoming request to a plain-language route description
- [sqlite3-jev](https://github.com/mattn/sqlite3-jev) - SQLite C extension: `jev_noul` / `jev_choice` / `jev_score` as SQL functions via libcurl
- [jevql](https://github.com/kylemclaren/jevql) - Unofficial psql-shaped CLI and Go/TypeScript/Python SDKs for vanilla Postgres: `jev()` / `jev_prob` / `jev_choice` / `jev_score` in plain SQL with no extension, the SQL runs on the server and Jev judges the surviving rows in batches
- [jev-resilience](https://github.com/Vicente-MD/jev-resilience) - Unofficial Spring WebFlux starter: a semantic circuit breaker that uses Jev to catch silent HTTP 200 failures
- [tripwire](https://github.com/noelzappy/tripwire) - Unofficial AI SDK middleware and OpenAI-compatible proxy: seven Jev checks on every LLM response in ~100 ms, confidence-gated
- [ProgressGate](https://github.com/AshutoshVJTI/progressgate) - Detects semantic stagnation in agent loops: Jev judges the trajectory; code returns CONTINUE / WARN / REPLAN / HALT
- [jev-harness](https://github.com/AntonioCoppe/jev-harness) - Unofficial production layer around Jev: policy, confidence gate, shadow mode, recipes, and an eval CLI
- [jev-tree](https://github.com/reachjalil/jev-tree) - Recursive Choice over a taxonomy so catalogs larger than Jev's 255-option cap still fit
- [jev-shell-history](https://github.com/mrnugget/jev-shell-history) - Fish-style zsh autosuggestions: Jev ranks recent history as you type
- [Supercov](https://github.com/supercorp-ai/supercov) - Code quality and test coverage for coding agents: Jev scores each source file so the agent knows what to fix first
- [Jev Review](https://github.com/devagrawal09/jev-review) - Staged code-review workflow and local dashboard driven by focused Jev calls.
- [Foreman](https://github.com/thruwire/foreman) - Software-factory loop: Codex implements; Jev independently judges completeness, tests, and whether a human is needed.
- [Jev Drone](https://github.com/RomanSlack/jev-drone) - MuJoCo quadrotor: control and safety stay in code; Jev handles slower tactical judgments.
- [Jev Plays StarCraft](https://github.com/phyous/tsai-sc) - Structured-state harness for the original StarCraft shareware campaign, with verified run and probability traces.
- [Jev × Civilization II](https://github.com/phyous/tsai-civ2) - Original Civ II in a browser; Jev chooses empire, city, research, and unit actions. Experimental; no verified win yet
- [Jev Trade](https://github.com/aowang-ai/jev-trade) - Live Hyperliquid desk: each tick Jev answers Choice questions for long/short, open/close/hold, and leverage; code places or pulls the quote. Dry-run by default; a live key sends real orders. Demo: [jev-trade.com](https://www.jev-trade.com/).
- [Jev Trader](https://github.com/jarrodwatts/jev-trader) - One buy/sell decision per Monad block on Kuru's MON-USDC book. Live demo: [jev-trader.vercel.app](https://jev-trader.vercel.app/).
- [Human Compiler](https://github.com/asfarsadewa/human-compiler) - Paste corporate prose; Jev scores passive-aggression, urgency, and information density, then code emits rustc-style diagnostics. Live: [human-compiler.asfarlab.fun](https://human-compiler.asfarlab.fun).
- [Jev Wrapped](https://github.com/gaborishka/jev-wrapped) - Telegram channel X-ray: Jev judges up to 1,500 public posts from a channel's last year with one `Choice` over ten kinds of post and three `Noul` checks for paid ad, clickbait and emotional pressure; code draws the monthly mix on a shareable card and links the highest-scoring posts. Live: [wrapped.ivanhabor.com](https://wrapped.ivanhabor.com).
- [JEVMETER](https://github.com/ChetasLua/jevmeter) - Live Jev meter on any video: every sentence scored, rendered as a 16:9 edit. Demo: [Chetaslua](https://x.com/chetaslua/status/2100473581251748216).
- [jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper) - Low-latency audio insult detector: Jev decides, ffmpeg beeps in ~466 ms without rewriting the rest of the track.
- [jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm) - Zero-shot English goals on a simulated Franka. Jev chains hardcoded primitives.
- [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) - Per-turn Codex routing: Jev picks model, thinking depth, and speed mode.
- [Codex Jev Router](https://github.com/suenot/codex-jev-router) - Codex subagent routing: Jev chooses a model and reasoning effort from typed Choice and Noul answers; code applies confidence gates and falls back to Sol.
- [Jev Auto Router](https://github.com/miniLV/Jev-Auto-Router) - Unofficial model-routing prototype that uses Jev to choose a model and reasoning effort for each call, with a local Responses proxy and independent task verification
- [jev-router](https://github.com/gargpratyush/jev-router) - Per-turn routing for Claude Code and Codex: Jev sends simple work to the fast tier and hard work to the strong tier. `npm i -g jev-router`.
- [jev-secret-detection](https://github.com/teyhouse/jev-secret-detection) - Secret-in-diff detector with repeatable Jev verdicts.
- [commit-miner](https://github.com/devanshbatham/commit-miner) - Rust CLI that classifies commit diffs with Jev: bug fixes, security/CWEs, and change types. HTML/CSV reports.
- [jev-eval-agent](https://github.com/vinilana/jev-eval-agent) - Public eval harness for early Jev tests.
- [Jev Logs](https://github.com/reachjalil/jevlogs) - OpenTelemetry log triage: Jev scores diagnostic value and priority before an expensive LLM looks at the archive.
- [Smart home assistant demo](https://docs.typesafe.ai/demos/smart-home) - Official interactive demo of [speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)
- [jev.nvim](https://github.com/valentynkit/jev.nvim) - Neovim plugin that splits the buffer into functions with Treesitter, scores each against a plain-language question with Jev, and ranks answers by probability in the quickfix window.
- [jev-skip](https://github.com/valentynkit/jev-skip) - Browser extension that reads the YouTube caption track and paints a per-segment sponsor probability on the seek bar before the intro ends, with no crowd database, reporting catching 77% of SponsorBlock's sponsor seconds across 23 videos at $0.0008 a video.
- [JevBystander](https://github.com/Nisaka520/JevBystander) - Android accessibility app that reads the visible WeChat chat screen and sends one batched Jev request (10-way intent `Choice`, 9-way emotion distribution, 0-3 urgency `Score`, 11-way reply-posture `Choice`) to show exactly three toasts - no generated reply text, no input injection, no screenshot or OCR; a local contact table supplies relation aliases as state context.
- [Paper Radar](https://github.com/Eliot5566/JEV-Paper-Radar) - Unofficial daily arXiv and bioRxiv radar. Jev answers one Noul per plain-English interest for every new paper; code applies the thresholds and publishes a page and RSS feed from GitHub Actions. [Live demo](https://eliot5566.github.io/JEV-Paper-Radar/public/) needs no key.

## Demos & Games

Toys, live sites, and realtime agents.

- [Yes / No](https://yesno.coderai.dev) - Free no-signup Noul demo. Ask a question, get yes / no / maybe, with web search when needed.
- [Jev Tetris](https://jev-omega.vercel.app) - Jev picks rotation and column from holes, stack height, and bumpiness.
- [Jev Pac-Man](https://jev-pacman.ephraimduncan.com) - Maze as JSON; Jev picks the turn at each junction in realtime.
- [Jev Chess](https://jevchess.com) - One shared board, the internet vs Jev; every legal move is one Choice question, probabilities shade the pieces, live calibration panel scores every move.
- [Chess with Jev](https://chriswijnia.com/experiments/chess) - Chess and Chess960 in the browser: code works out each legal move's facts and Jev picks one per turn as a single Choice, with its candidates drawn as arrows ([source](https://github.com/cwdx/chess-with-jev))
- [typesafe-mario](https://github.com/fhshaik/typesafe-mario) - Super Mario Bros. from structured emulator state.
- [jev-doom-agent](https://github.com/lukaske/jev-doom-agent) - Browser-native Doom with Chocolate Doom WASM, spatial state, and live decision telemetry.
- [jev-gomoku](https://github.com/mizchi/jev-gomoku) - MoonBit client plus Jev-vs-Jev gomoku; write-up: [jev 同士に五目並べで対戦させた](https://zenn.dev/mizchi/articles/jev-plays-gomoku).
- [jev-t-rex-runner](https://github.com/joshlarsen/jev-t-rex-runner) - Chrome dinosaur game played by Jev.
- [snake-jev](https://github.com/siroccomask/snake-jev) - Snake: hundreds of typed direction decisions per run.
- [Jev Guard](https://guard-jev.vercel.app) - Comment-moderation playground.
- [jev-fit](https://jev-fit.com) - Paste a software idea; Jev answers a fixed typed rubric in one call and the page says plain code, Jev, or a reasoning LLM, with probabilities. Unofficial, closed source, free page and API.
- [Hollow Creek](https://hollow-creek-sigma.vercel.app) - Village NPCs that *judge* you each tick (what to do, how they feel) instead of chatting.
- [Jev mood demo](https://jev-demo.vercel.app) - Talk nicely or nastily over time; structured state tracks mood.
- [Jev Room](https://jev-room.moe136231.chatgpt.site) - One sentence → six room settings. Jev chooses, the app renders.
- [1 Million Emojis](https://chriswijnia.com/experiments/emoji) - A shared 1000 × 1000 emoji canvas, live for everyone; after each stroke Jev picks a square next to it and its emoji as one Choice ([source](https://github.com/cwdx/1-million-emojis))
- [TypeSafe Typewriter](https://typesafe-demo.val.run/) - Live Val Town demo: 16 typed judgments update as you type. Launch post: [Steve Krouse](https://x.com/stevekrouse/status/2100287368221659289).
- [got-jev](https://github.com/phureewat29/got-jev) - Game of Thrones roleplay as Jon Snow. A story model writes the scene; Jev answers where he is, how much danger, and what should play under it.
- [Little Airways](https://github.com/lbotinelly/jev-little-airways) - Toy archipelago ATC: Jev judges divert / emergency / who lands first from each plane's local state, ~150 ms.
- [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) - Pokemon Red on PyBoy where deterministic code owns the route and arithmetic and Jev picks only at branches, with every battle turn's faint prediction scored by Brier against the emulator's RAM state.
- [jev-canvas](https://github.com/gaborishka/jev-canvas) - Draw on a tldraw canvas with your voice and a webcam-tracked finger; Jev decides action, target and place on every partial transcript. English and Ukrainian commands.
- [Jevtown](https://github.com/gaborishka/jevtown) - A town of 10,000 computed personas reads your post, listing, product or headline. Jev scores who the text is for to pick the first 600 readers and answers one `Choice` per persona for its reaction; code sends the text to the next wave only while glad readers outnumber annoyed ones by at least a tenth of the wave. Live: [jevtown.ivanhabor.com](https://jevtown.ivanhabor.com).
- [sudoku-vs-jev](https://github.com/zebedelu/sudoku-vs-jev) - Terminal Sudoku where Python owns the rules and Jev picks one move per turn, steady while forced moves exist and shaky once it has to guess.
- [chess-vs-jev](https://github.com/zebedelu/chess-vs-jev) - Pygame chess where python-chess owns the rules and Jev picks one legal move per turn, playable Human vs Human, Human vs Jev, or Jev vs Jev.
- [JevsBistro](https://github.com/andrewsilber/JevsBistro) - Deterministic 3D restaurant sim that replays the same dinner service to compare rule-based, camera-assisted, and Jev-planned waiters, logging each decision's state, options, confidence, and latency.
- [jev-asks-until-sure](https://github.com/mintannn/jev-asks-until-sure) - Twenty questions where confidence sets the stopping rule: Jev commits, hedges, or refuses to guess, and the UI narrates every judgment. Live: [jev.mintan.org](https://jev.mintan.org).
- [Jev × 2048](https://jev-2048-ultra.vercel.app) - A web lab where Jev is the 2048 decision engine, showing each move's probability distribution, confidence, latency, and token cost so you can watch how context design shapes the decision model.
- [Book Aurora](https://github.com/dani1005/book-aurora) - Jev reads a whole novel in seconds: each passage gets nine emotion scores plus intensity in one call, and every passage becomes a feathered row of colour. Frankenstein is 601 passages, 6,010 typed decisions, about 25 s and 3 cents; exports a poster.

## Agent Tools

Tools that expose Jev to coding agents and MCP clients.

- [TypeSafe agent skill](https://github.com/typesafe-ai/skills) - Official skill: primitives, patterns, and how to structure evaluations. Claude Code: `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai`. Other agents: `npx skills add typesafe-ai/skills --skill typesafe-ai`.
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Claude Code plugin and npm library: Jev scores tool calls and drops stale ones instead of summarizing context
- [SkillRanker](https://github.com/Dicklesworthstone/skillranker) - Rust CLI: Jev ranks which agent skill fits the next step from live session context, with Claude Code hooks
- [langchain-skill-router](https://github.com/deyna256/langchain-skill-router) - LangChain deepagents middleware for per-turn skill routing: Jev ranks and verifies which SKILL.md skills each turn needs from a catalog of hundreds, splitting the ranking to fit Jev's limits and falling back to the full catalog on failure. The judge is pluggable. `pip install "langchain-skill-router[jev]"`.
- [JevRouter](https://github.com/BillionsBobby/JevRouter) - Unofficial router that puts models, subagents, skills, MCP tools, and CLIs in one candidate set: Jev answers one Choice, and code enforces availability, permissions, risk, and confirmation. On 10 Toolathlon tasks, position-wise hits were 38–44% for Jev against 24% for DeepSeek V4.1 Flash
- [JevLoop](https://github.com/zjunlp/JevLoop) - Unofficial agent loop that sends each fork (tool, risk, done) to Jev 1.13.0 and keeps the LLM for writing; with no key it falls back to local Laya, then rules. `npm run demo` runs offline
- [Jevbridge](https://github.com/gamesonrblx/Jevbridge) - Unofficial ACP/MCP adapter: typed Jev decisions and computer use beside Codex, Claude, Grok, and OpenCode
- [eve](https://github.com/vercel/eve) - Vercel's agent framework. Experimental `autoModel` defaults to Gateway `typesafe-ai/jev` to pick a language model from an allowlist.
- [jev-mcp](https://github.com/jkudish/jev-mcp) - Node MCP wrapping three cookbook patterns: `jev_verify` (citation check), `jev_screen` (prompt-injection / guardrails), `jev_find` (semantic ranking without embeddings). `npx -y github:jkudish/jev-mcp`.
- [Jev MCP (Python)](https://github.com/blakestone-x/jev-mcp) - Python MCP server: classify, score, check, match, and screen tools.
- [Jev Review MCP](https://github.com/NiazMorshed2007/jev-review) - Local-first MCP: Claude Code, Codex, Cursor, and OpenCode get structured quality review from Jev while they write. Not the same project as [Jev Review](#applications) above.
- [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) - Go CLI and single-binary MCP for Claude Desktop, Claude Code, and Codex.
- [pi-typesafe](https://github.com/DevMortimer/pi-typesafe) - Pi extension: one consented, key-managed TypeSafe client, batched `typesafe_evaluate`, offline-testable transport.
- [pi-jev](https://github.com/y0usaf/pi-jev) - Pi extension with a shadow-mode tool-call gate, output judge, and typed `jev_ask`.
- [pi-warden](https://github.com/DevMortimer/pi-warden) - Pi guardrails on pi-typesafe: held tool results instead of a dialog; write checks against a project rules file.
- [pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode) - Pi auto mode: Jev semantically approves `bash` / `write` / `edit`, and fails closed when it cannot decide.
- [Bicameral](https://github.com/AbdelStark/bicameral) - Pi coding harness: LLM writes, Jev supplies typed reflexes for policy, loop detection, and review. Explicitly not a sandbox.
- [jev-pref](https://github.com/doeixd/jev-pref) - Turn AGENTS.md preferences into a Jev-powered AI linter: project-specific semantic review rules in `jev-pref.json`, checked against hunks, staged files, or PRs, with findings fed back to your coding agent. `npx jev-pref setup`.
- [ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill) - Hermes skill: ask Jev whenever the agent needs a bounded decision.
- [hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) - Hermes pack, also for Claude Code and Codex: Jev handles model routing, skill choice, search, memory, and compaction. About 0.4 s per routing turn, and about 2.8 s to pick among 377 skills. A measured handoff digest recalled less than the plain transcript, so handoffs keep the dialogue
- [jev-system-architect](https://github.com/samtay32/jev-system-architect) - Skill that hunts for brittle semantic logic and turns it into Choice / Score / Noul boundaries.
- [augustus](https://github.com/24601/Augustus) - Unofficial augustus and augustus-train agent skills for application-specific decision models: primitive/base-model/method selection, data assembly, fitting, export/reload, bounded improvement and independent evaluation; TypeSafe Jev is the default hosted exemplar
- [jev-axi](https://github.com/shiftynick/jev-axi) - CLI plus Claude Code and Codex hooks: Jev scores each shell command for hazards before it runs and screens fetched text for prompt injection, with routine commands decided locally so nothing is sent
- [jev-engineering](https://github.com/eugeniughelbur/jev-engineering) - Decision layer for coding agents: deterministic rules before any model call, then one Jev request, as a Claude Code hook, an MCP server, a loopback service and a shared team policy. Ships the 300-call injection test behind its own numbers.
-  [toolgate](https://github.com/RiskAverseTech/toolgate) - Unofficial tool-call firewall for Claude Code hooks and MCP servers: Jev answers seven risk questions per call and deterministic code maps them to allow/ask/deny, fails closed, and tracks write-then-execute across a session
- [Jevonian](https://github.com/xinyao27/jevonian) - Local OpenAI / Anthropic / Responses-compatible proxy where one Jev call answers both the model route and the thinking level for `jevonian/auto`, from session state (recent messages and tool results, consecutive errors, context headroom, quota, candidate capabilities, cache-switch penalties); deterministic code filters candidates and owns every threshold first, a pinned model or explicit `jevonian/<route>` skips Jev entirely, and each decision is recorded with the serving model, reason, token usage, and estimated cost.
- [jev-belay](https://github.com/valentynkit/jev-belay) - Claude Code Stop hook that checks the transcript for evidence before trusting a "done" claim, spending one four-question Jev call only when files changed with no passing check since, and failing open on every error path.
- [jev-commit](https://github.com/valentynkit/jev-commit) - Pre-commit hook where one Jev call judges whether the commit message matches the staged diff, flags debug leftovers and unmentioned work, and blocks only when it detects a credential.
- [jev-use](https://github.com/shitianfang/jev-use) - Claude Code, Codex and pi plugin: Jev answers the batched typed questions an agent loop needs, and a typed escalation contract hands writing and low-confidence steps back to the LLM
- [dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools) - DeepSeek Harness plugin: Jev prunes oversized tool output, screens fetched pages for injected instructions, and picks which skill fits the next step, plus the jev_ask and jev_gate tools
- [slop-grader](https://github.com/lukstei/slop-grader) - Rule-based CLI and agent skill that grades text against custom rulesets for AI slop, grammar, and technical documentation quality, and guides an AI agent to auto-fix violations
- [pytest-jev](https://github.com/allebee/pytest-jev) - pytest plugin for semantic assertions on LLM output: each plain-English claim about a reply becomes a Jev Noul in one request, a claim passes at p ≥ 0.8, and failures print every claim's probability; `choice` and `score` cover routing and rubric checks
- [jgrep (kyu1204)](https://github.com/kyu1204/jgrep) - Semantic grep for code, git diffs and CSV rows: one Noul per 5-60 line chunk, 16 chunks per Jev request, grep-style file:line output and exit codes for CI lint rules written in English
- [jevgrep (allebee)](https://github.com/allebee/jevgrep) - Streaming grep by meaning for logs: asks Jev one Noul per line against a plain-English question and prints the lines at or above a threshold, including from `tail -f`
- [wellposed](https://github.com/suraj-phanindra/wellposed) - Offline linter and agent skill for Jev requests: 40 structural checks with no model call (missing none-of-the-above options, broken state paths, wrong criteria shapes), plus Jev-on-Jev checks for what structure cannot decide, with labelled corpora that score both layers.

## Research & Open Models

Independent work inspired by Jev's interface. These are not TypeSafe models.

- [Kev](https://github.com/jaredpalmer/kev) - Unofficial Qwen3.5 decision models (0.8B, 4B, 9B) you can train and serve yourself. Choice, Score, and Noul in one forward pass, with published weights and frozen eval suites, and a local server that speaks `/v1/systemone`. Not TypeSafe's model
- [Von](https://github.com/wfzyx/von) - Unofficial local non-autoregressive System One model with a `/v1/systemone`-compatible server and a Doom demo where each move is one forward pass. Not TypeSafe's model
- [Laya](https://github.com/NandhaKishorM/laya) - Unofficial multilingual non-autoregressive decision model: Choice, Score, and Noul in one forward pass, with published weights, a PyPI package, and a router that picks a checkpoint per request. Not TypeSafe's model
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - Unofficial 0.6B parallel decision model: state and questions in, a full distribution out, no decoded text. Published weights and one checkpoint for ViZDoom, Maze, and Snake; on the author's ViZDoom Basic split, 128/128 against 56/128 for Jev. Not TypeSafe's model
- [jevlike](https://github.com/vinnylarouge/jevlike) - Train a small one-pass scorer that maps context + N text options to a probability per option. Includes Doom / chess vision demos and a Wikispeedia next-click example. Explicitly *not* a reproduction of TypeSafe's architecture or RLCD.
- [SemIf](https://github.com/TheoLeeCJ/SemIf-OpenJev) - Formerly OpenJev. Unofficial typed decisions from open models on a home RTX 3090 and in the browser: reads option logits instead of generating text. Not TypeSafe's model
- [PocketJev](https://github.com/NullPo-jp/PocketJev) - On-device iPhone visual decisions with MLX + Qwen3-VL option logits. Camera + 3-choice, no text generation, ~1s, no photo saved.
- [jev-visual](https://github.com/hr98w/jev-visual) - Educational Jev-like visual inference on Apple Silicon: shared multimodal context, candidate scoring, sorting-factory / Breakout / gesture demos. Not TypeSafe's model
- [jevmlx](https://github.com/bnsd55/jevmlx) - Jev-style parallel constrained decisions for any MLX model on Apple Silicon: schema-valid JSON in one forward pass
- [JEVfire](https://github.com/kikoncuo/jevfire) - Jev-inspired parallel decisions for CUDA LLMs via vLLM, with a browser Mario demo (~71 ms/action locally)
- [decider](https://github.com/Mapika/decider) - Qwen3.5-2B fine-tune that emits typed decisions with calibrated probabilities in one pass. Unofficial; not TypeSafe's architecture.
- [jev-style](https://github.com/lawrence3699/jev-style) - Unofficial 0.8B Qwen3.5 decision model you install with `pip install "jev-style[torch]"` (or `[mlx]` on Apple silicon) and run locally (PyTorch, MLX, or llama.cpp with a separately built scorer) behind a `/v1/systemone`-compatible server: Choice, Score, and Noul in one pass, plus an MCP server and a Claude Code guard hook. Not TypeSafe's model
- [LitJev](https://github.com/zhengxuyu/litjev) - A reproduction of Jev that turns any Qwen model into a fast decision model, serving the same `/v1/systemone` schema (Choice, Score, Noul) with no training and no generated answer text. Unofficial; not TypeSafe's model.
- [PlayJev](https://github.com/OmniJev/PlayJev) - Qwen3.5-0.8B-Base fine-tuned to play ten browser games from 448 px frames: one forward pass per move, a probability over the game's option list read off the option letters, no generated text. Open weights and a demo of all ten in the browser. Unofficial; not TypeSafe's model.
- [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) - Side-by-side of Jev vs Qwen 3.8 27B on Cerebras for the same System One questions. Video: [Shannon](https://x.com/iamMrDuncan/status/2100467548298899918).
- [Jev Rerank Bench](https://github.com/anessbelbati/jev-rerank-bench) - Reranking comparison with raw provider responses, scoring code, uncertainty intervals, and documented limits.
- [Jev Spam Eval](https://github.com/bitnovus/jev-spam-eval) - Exploratory zero-shot spam study vs trained TF-IDF baselines, with post-hoc-tuning caveats.
- [Jev × NASA Kepler](https://gist.github.com/ipaulsmith/e5c3ae3a492a455435d5bfc161404312) - Independent retrospective test of Jev 1.13 on 8,054 historical Kepler Objects of Interest with NASA Exoplanet Archive dispositions hidden during prediction; 72.5% archive-disposition match vs 64.4% for a fixed 3-rule baseline, with exact requests, metrics, baseline, and caveats
- [Jev Phishing Bench](https://github.com/anisselbd/jev-phishing-bench) - 2,000 emails: Jev vs Claude Haiku 4.5 on click-or-not, with calibration, latency, and cost. Haiku wins accuracy here.
- [jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark) - Who&When Pro (injected agent failures): Jev vs a strong LLM on who / which step / error category.
- [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) - Blind prompt-injection and vulnerable-code detection benches on public corpora, built on jev-go.
- [Jev DSPy Lab](https://github.com/jmanhype/jev-dspy-lab) - Unofficial DSPy companion that records and replays TypeSafe calls while measuring calibration, selective risk, confidence-gated abstention, latency, tokens, and modeled cost.
- [jevcal](https://github.com/abhixhek/jevcal) - Unofficial CLI that fits a per-question confidence threshold to a target accuracy on your own labeled data, verifies it on a held-out split, shows how much traffic still needs an LLM fallback, and fails CI when a Jev update breaks the locked thresholds
- [ASSAY-001](https://github.com/jourdanlabs/assay-001) - Independent pre-registered check of Jev calibration and type safety on Banking77 / CLINC150. Split verdict, full logs. Write-up: [donttrustme.ai](https://donttrustme.ai/assay-001.html)
- [Jev search rerank eval](https://github.com/zhuyansen/jev-search-rerank-eval) - 9,831 labelled pairs: Jev rerank vs BM25 / bge-m3, with judge-circularity measured. Fusion wins; Jev alone does not beat embeddings
- [Smoking-history extraction benchmark](https://github.com/vclic/smoking-extraction-benchmark) - 1,000 synthetic notes: Jev vs OpenAI structured outputs on accuracy, cost, and latency
- [Jevals.com](https://jevals.com/) - Independent benchmark of hosted Jev and six LLMs on the same Noul, Choice and Score questions, graded against human labels (PubMedQA, Banking77, HelpSteer2), with per-decision logs as open data
- [stuntd](https://github.com/bladedevoff/stuntd) - Local proxy on the open Laya model that speaks the Jev System One API, records the app's Choice, Score and Noul answers from a Jev upstream, trains a per-question head, and serves it with a calibrated confidence threshold and fallback to the upstream
- [jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench) - Compares batched and separate Jev calls in 2,976 requests through OpenRouter, reporting approximately 261 fixed input tokens per request, charges matching the published token rate, and answer differences comparable to repeat-request noise.

## Articles

Independent measurements and experiments.

- [Jev in Search: Three Practical Evaluations](https://zc277584121.github.io/rag/2026/09/22/jev-search-deep-evaluation.html) - Independent experiments on search stopping, memory reranking, and multi-hop relation selection, with implementation links and limitations including private data, unequal sample counts, and a simulated speed illustration
- [Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](https://arxiv.org/abs/2609.30216) - First data-driven survey and analysis of Jev's application ecosystem across 2,170 public GitHub projects, covering rapid early growth, application domains, and decision-use patterns
- [Mini-Vibe Check: TypeSafe's Jev Judged Everything I’ve Written in 0.7 Seconds](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) - Every's Mike Taylor runs Jev over a writing corpus.
- [TypeSafeのJevを正しく驚く、それってLLMでできませんか？](https://zenn.dev/nwn/articles/824026c76116e0) - Reproduces the JSON-vs-logit shortcut on Gemma and compares Jev with LLMs on the public Mario harness.
- [Jev: one judge call, or twelve dimension scores? I measured both on three tasks](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/) - Independent measurement on three classification tasks: one direct Jev question per row against 12–14 Jev-scored dimensions with locally fitted weights, with token costs, confidence intervals, and false-positive rates.
- [Testing Jev on public and private data: classifier or filter?](https://amankumar.ai/blogs/jev-measured) - 16,000 calls vs gpt-5.4-mini and gpt-5.6-luna; where it wins, where it breaks, and a threshold procedure
- [Is Jev as Accurate as Frontier Models at Classification?](https://openrouter.ai/blog/insights/jev-vs-claude-opus-5-classification/) - OpenRouter runs all 3,080 Banking77 test utterances through Jev 1.13 and Claude Opus 5: 81.0% vs 84.4% accuracy, 175 ms vs 2,266 ms median, about $0.11 vs $2.42 per 1,000
- [We Tested Jev on 791 Labeled Decisions Against Four LLMs](https://www.ayautomate.com/blog/jev-vs-llm-benchmark) - Independent OpenRouter run on 8-way and 77-way Banking77 routing plus prompt-injection detection: Jev matches the small models, trails GPT-5.6 Terra by about 5 points on 77-way routing, and a 0.80 confidence gate that escalates the rest to Terra matches Terra's accuracy at about a quarter of the cost
- [Jev × LexGLUE](https://github.com/chepyle/jev-test) - Reproducible zero-shot run of Jev 1.13 (`typesafe/jev-1.13-20260917`) on all seven LexGLUE tasks, 23,607 test examples: mean micro-F1 69.9 at $4.02, against 71.3 at $16.45 for GPT-5.6 Luna via chat JSON
- [Jev Does Not Play Dice: 83% probability, 19% accuracy on a hidden fair die roll](https://kantahayashiai.github.io/posts/jev-does-not-play-dice/) - Independent calibration check on fair dice, coins and spinners, where the true probability is known exactly, and on synthetic forecast documents; Jev selects face 1 on all 400 die rolls with 82.9% mean reported probability against 19.0% accuracy. Code and raw responses on [GitHub](https://github.com/KantaHayashiAI/jev-does-not-play-dice).

Community cookbooks.

- [Milvus Search with Jev](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) - Nine runnable Python notebooks combining Gemini embeddings, Milvus retrieval, and Jev decisions for reranking, filtering, search stopping, routing, cache reuse, curation, guardrails, and evaluation

## Related

- [MrJev/awesome-jev](https://github.com/MrJev/awesome-jev) - Selective list behind a 10-star bar, with hands-on reviews at [mrjev.com](https://mrjev.com/best-jev-tools/) recording what each tool sends and where.
- [typesafe-ai on PyPI](https://pypi.org/project/typesafe-ai/) - Community redirect shim. The real package is `typesafe-sdk`; this name was registered to block slopsquatting. Not affiliated with TypeSafe.
- [laya.tools](https://laya.tools) - Unofficial directory of about 950 projects built on the open Laya model, from GitHub, npm, Hugging Face and X, browsable by platform and use case, with a Laya vs Jev comparison. Not affiliated with TypeSafe or ConvAI

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: open a pull request that adds a project with a link and a one-line description. Useful, interesting, and actually built on Jev (or clearly inspired by its interface).

## License

[CC0 1.0](LICENSE) — this list is dedicated to the public domain.
