# Awesome Decision Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of decision models (also called System One models or typed decision models) and the APIs, runtimes, tools, applications, benchmarks, and research around them.

**[English](README.md)** | **[简体中文](README_zh.md)** · [Website](https://anotiawang.github.io/awesome-decision-models/)

A decision model reads a state (text, JSON, and for some models images) plus questions whose answers you declare up front, and returns a probability for every answer instead of generated text. Questions come in three shapes: Noul (the probability that a statement is true), Choice (one of your options), and Score (a level on an ordered rubric). TypeSafe AI introduced the category in September 2026 with [Jev](https://docs.typesafe.ai/introduction) and its `/v1/systemone` API, and many of the models and runtimes below accept the same request shape.

Community-maintained and not affiliated with any model provider. Pull requests welcome.

## Contents

- [Hosted APIs](#hosted-apis)
- [Open Models](#open-models)
- [Inference Techniques](#inference-techniques)
- [Runtimes & Platforms](#runtimes--platforms)
- [SDKs & Clients](#sdks--clients)
- [Applications](#applications)
- [Demos & Games](#demos--games)
- [Agent Tools](#agent-tools)
- [Benchmarks & Evaluations](#benchmarks--evaluations)
- [Papers](#papers)
- [Articles](#articles)
- [Related](#related)
- [Contribute](#contribute)

## Hosted APIs

API-only models, oldest first. Open-weight models that their publishers also host, such as Clef and pplx-decider, are under [Open Models](#open-models).

- [Jev](https://docs.typesafe.ai/introduction) - TypeSafe AI's first System One model and the origin of the `/v1/systemone` API: Noul, Choice, and Score questions over a text state in one request. Keys from the [console](https://console.typesafe.ai/settings/keys); also served through Vercel AI Gateway, Cloudflare Workers AI, and OpenRouter.
  - [Playground](https://console.typesafe.ai/playground) · [Console](https://console.typesafe.ai) · [GitHub](https://github.com/typesafe-ai) · [Workflow evals](https://evals.typesafe.ai) · [Cookbooks](https://docs.typesafe.ai/llms.txt) · [Patterns](https://docs.typesafe.ai/patterns)
  - [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) - Known failure modes
  - Community: [Discord](https://discord.gg/typesafe) (builder demos in [Show and Tell](https://discord.com/channels/1483217544214085663/1483217545040232493)) · [X @typesafeai](https://x.com/typesafeai)
- [meraGPT Decider 1](https://meragpt.com/docs) - Hosted decision model (`state-decider-1`, alias `sd-1`) answering Noul, Choice, and Score through `/v1/systemone`, compatible with the TypeSafe SDK; requests are limited to 4,096 tokens and Choice to ten labels
- [Solar Decide](https://openrouter.ai/upstage/solar-decide) - Upstage's decision model on Solar Mini 4, in beta, with a 512K context and the same request format as Jev
- [Span-01](https://www.respan.ai/blog/introducing-span-1) - Respan's behavior classifier for AI traces: for each plain-language behavior you define, such as prompt injection, hallucination, or agent loops, it returns present, absent, or not observable. Span-01 and a Lite tier are on [OpenRouter](https://openrouter.ai/respan/span-01).
- [d1](https://docs.liquid.ai/lfm/models/decision-models) - Liquid AI's first decision model, served at a `/v1/systemone` endpoint that the TypeSafe SDKs can call, and on [OpenRouter](https://openrouter.ai/liquid/d1). Model size not disclosed.
- [OpenAI Decisions API](https://openai.com/index/devday-2026-recap) - Announced at DevDay 2026 and built on Luna: context, a question, and a closed list of answers in; an answer with a confidence score out. Limited preview, pricing not yet published.
- [Mercury Decide](https://openrouter.ai/inception/mercury-decide) - Inception's decision model, with a free route on OpenRouter; Inception cites up to 14 decisions per second.

## Open Models

Open-weight models you can download and run. Scores are as reported by each project on the benchmark it chose, so numbers are not comparable across entries.

### From companies and labs

- [Clef](https://huggingface.co/Cloudflare/clef) - Cloudflare's Apache-2.0 decision models post-trained from Qwen3.8-27B: Clef reads text, JSON, images, or video and scores every option of every question jointly, and Clef-flash is the smaller, faster variant. Both are hosted on Workers AI with a Jev-compatible API. Launch post with Jev Decision Index results: [blog](https://blog.cloudflare.com/clef-decision-models).
- [pplx-decider-v1-27b](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b) - Perplexity's Apache-2.0 multimodal decision model fine-tuned from Qwen3.8-27B; its card reports a mean of 85.71% over 11 benchmarks against 84.51% for Jev. Also served through the [Perplexity Decisions API](https://docs.perplexity.ai/docs/decisions/quickstart).
- [Strands Decider 2B](https://github.com/strands-labs/strands-decider) - AWS Strands Labs' decision model: Qwen3.5-2B with the LM head replaced by a pointer head of about a million parameters that scores each option, plus a rank-16 LoRA. Weights, training data, and scripts are public; the [launch post](https://strandsagents.com/blog/introducing-strands-decider) uses it to check a Strands agent's tool calls before they run.
- [Nimble](https://github.com/bespokelabsai/nimble) - Bespoke Labs' 9B LoRA fine-tune of Qwen3.5-9B on contrastively curated synthetic data, with a public 13-dataset benchmark suite. In Ollama as `nimble`.
- [Tev1](https://huggingface.co/togethercomputer/Tev1-4B-experimental) - Together AI's experimental 4B and 0.8B supervised fine-tunes of Qwen3.5, released with a walkthrough on [training your own decision model for $17](https://www.together.ai/blog/how-to-train-your-own-jev). In Ollama as `tev1`.
- [Laya](https://github.com/NandhaKishorM/laya) - Convai Innovations' multilingual non-autoregressive decision model: Choice, Score, and Noul in one forward pass, with published weights, a PyPI package, and a router that picks a checkpoint per request
- [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide) - Fastino's Apache-2.0 DeBERTa-v3-large decision classifier: caller-defined tasks and labels get probabilities in one forward pass through `gliner2` on CPU or GPU, for operational classification, routing, and ordinal scoring
- [Standard One](https://huggingface.co/StandardThinking/StandardOne-8B) - Standard Thinking's Apache-2.0 3B and 8B decision models on Ministral 3, with a retained Pixtral vision tower: text or images in, option probabilities out through `/v1/systemone`, with merged weights, adapters, GGUF builds, and server code
- [OpenJev](https://huggingface.co/openjev/openjev) - Independent open-weight decision model that scores caller-defined options in one forward pass, with calibration and serving code; weights are CC BY-NC 4.0 for noncommercial use and helper/server code is Apache-2.0. Separate from SemIf, formerly named OpenJev.

### Community models

- [Kev](https://github.com/jaredpalmer/kev) - Qwen3.5 decision models (0.8B, 4B, 9B) you can train and serve yourself. Choice, Score, and Noul in one forward pass, with published weights and frozen eval suites, and a local server that speaks `/v1/systemone`.
- [Von](https://github.com/wfzyx/von) - Local non-autoregressive System One model with a `/v1/systemone`-compatible server and a Doom demo where each move is one forward pass
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - 0.6B parallel decision model: state and questions in, a full distribution out, no decoded text. Published weights and one checkpoint for ViZDoom, Maze, and Snake; on the author's ViZDoom Basic split, 128/128 against 56/128 for Jev.
- [jevlike](https://github.com/vinnylarouge/jevlike) - Train a small one-pass scorer that maps context + N text options to a probability per option. Includes Doom / chess vision demos and a Wikispeedia next-click example. Explicitly *not* a reproduction of TypeSafe's architecture or RLCD.
- [decider](https://github.com/Mapika/decider) - Qwen3.5-2B fine-tune that emits typed decisions with calibrated probabilities in one pass
- [RSI-Jev](https://github.com/Shanghua-Gao/RSI-Jev) - Jev-like model trained by a recursively self-improving (RSI) AI research system that publishes every experiment, failures included. 2B Qwen3.5, with Choice, Score, and Noul in one forward pass over text or up to four images (v4.0-VL), open weights, and a `/v1/systemone`-compatible server.
- [jev-style](https://github.com/lawrence3699/jev-style) - 0.8B Qwen3.5 decision model you install with `pip install "jev-style[torch]"` (or `[mlx]` on Apple silicon) and run locally (PyTorch, MLX, or llama.cpp with a separately built scorer) behind a `/v1/systemone`-compatible server: Choice, Score, and Noul in one pass, plus an MCP server and a Claude Code guard hook
- [PlayJev](https://github.com/OmniJev/PlayJev) - Qwen3.5-0.8B-Base fine-tuned to play ten browser games from 448 px frames: one forward pass per move, a probability over the game's option list read off the option letters, no generated text. Open weights and a demo of all ten in the browser.
- [OneJev](https://github.com/OmniJev/OneJev) - Open multimodal System One model from the OmniJev team, in four sizes (0.8B to 27B): Choice, Score, and Noul questions about a screenshot, photo, video, or text get a calibrated probability for every option in one forward pass. Weights on Hugging Face.
- [jevos](https://github.com/feder-cr/jev) - 1B decision model for CPU-only laptops: MiniCPM5 cut to 17 layers with a one-logit head, GGUF q4_k_m at 619 MB, running on llama.cpp with no GPU, about 54 ms per short request. Speaks Jev's `/v1/systemone` wire format for Noul (yes/no) questions only; Choice and Score return 422.
- [WebJev](https://github.com/lexmount/WebJev) - Jev-compatible decision model for browser agents: a Qwen3.5-35B-A3B fine-tune that picks the next operation and target element in the Jev Ultrafast loop, behind a `/v1/systemone`-compatible server. On 125 real-website tasks graded by deterministic verifiers, it completes 38.5% vs 16.7% for Jev 1.13 in the same agent. Apache-2.0 weights, training data and recipe, and a demo app.
- [Vev](https://github.com/Xiaooolong/vev) - Open-source Jev implementation with vision input, fine-tuned from Qwen3.5 4B / 9B. Screenshots and photos go straight into the state, and Choice, Score, and Noul answers draw on both text and image, read from label-token probabilities with no generated text. Serves `/v1/systemone`; open code and weights, weights for non-commercial use only.
- [JEV-27B](https://huggingface.co/autotrust/JEV-27B) - AutoTrust's Apache-2.0 model distilled from Jev 1.13 onto Qwen3.8-27B; one vLLM engine serves both the decisions and the untouched Qwen model for ordinary generation. The authors report 84.07 against 83.85 for Jev over six public decision benchmarks in their own runs. Smaller sibling: [JEV-9B](https://huggingface.co/autotrust/JEV-9B).
- [Winnow](https://huggingface.co/EldanRing/Winnow-12B) - Apache-2.0 Gemma 4 fine-tunes (12B and E4B) for typed decisions, served from a llama.cpp-based server that answers both `/v1/systemone` and `/v1/chat/completions`.
- [JevK5](https://github.com/allebee/jevk5) - Apache-2.0 decision models on Qwen3.5 (2B, 4B, 9B) behind a `/v1/systemone` server, with GGUF builds for llama.cpp on CPUs and GPUs
- [reflex](https://github.com/kshetrajna12/reflex) - Small decision model on a frozen Qwen3.5-4B: one `/v1/systemone` endpoint answered by a single forward pass in about 200 ms, compared against Jev on JevBench's public items
- [imajev](https://huggingface.co/mohit67890/imajev-4b) - Apache-2.0 4B LoRA on Qwen3.5-4B for decisions about photos: checks a photo against your record or compares two photos, with a trained `unknown` probability so the app can stop instead of guessing. Jev's request shape plus `images`; runs with MLX or PyTorch.
- [NeoHorse-Jev-4B](https://huggingface.co/TokenRhythm/NeoHorse-Jev-4B) - TokenRhythm's Apache-2.0 4B decision model on NeoHorse-1-4B: text or a single image with text, prefill-only inference, served at `/v1/systemone`
- [WaterSheep](https://github.com/SamratDuttaOfficial/WaterSheep) - Apache-2.0 open-weight decision model for text: Noul, Choice, Score, and multi-label questions get a calibrated probability for every option, served by a local `/v1/systemone` server that TypeSafe's Python SDK works with unchanged

## Inference Techniques

Ways to get decision-model behavior from existing models, usually by reading option probabilities in one forward pass, with little or no training.

- [SemIf](https://github.com/TheoLeeCJ/SemIf-OpenJev) - Formerly OpenJev. Typed decisions from open models on a home RTX 3090 and in the browser: reads option logits instead of generating text.
- [LitJev](https://github.com/zhengxuyu/litjev) - A reproduction of Jev that turns any Qwen model into a fast decision model, serving the same `/v1/systemone` schema (Choice, Score, Noul) with no training and no generated answer text.
- [TetraJev](https://github.com/FeiLiuEM/tetrajev) - Locally-deployed decision layer for complex decision problems across domains: two frozen open-weight readers give four readings per item — letter and per-candidate yes/no — fused fit-free and routed by agreement with calibrated release gates; evaluated on eight decision suites and the RAG reranking pass, including DecisionBench's 35 real-world task categories. No training of any kind.
- [jevmlx](https://github.com/bnsd55/jevmlx) - Jev-style parallel constrained decisions for any MLX model on Apple Silicon: schema-valid JSON in one forward pass
- [JEVfire](https://github.com/kikoncuo/jevfire) - Jev-inspired parallel decisions for CUDA LLMs via vLLM, with a browser Mario demo (~71 ms/action locally)
- [PocketJev](https://github.com/NullPo-jp/PocketJev) - On-device iPhone visual decisions with MLX + Qwen3-VL option logits. Camera + 3-choice, no text generation, ~1s, no photo saved.
- [jev-visual](https://github.com/hr98w/jev-visual) - Educational Jev-like visual inference on Apple Silicon: shared multimodal context, candidate scoring, sorting-factory / Breakout / gesture demos
- [DiffusionGemma decision endpoint](https://huggingface.co/spaces/victor/DiffusionGemma-free-endpoint) - Free Hugging Face Space that reads a probability for every answer from DiffusionGemma, without fine-tuning, behind the `/v1/systemone` wire format

## Runtimes & Platforms

Servers, gateways, and native runtimes for running decision models.

- [Ollama](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models) - Serves `/v1/systemone` locally since 0.35; the first decision models in its library are `nimble` and `tev1`.
- [Ollaya](https://github.com/ollaya-dev/ollaya) - Ollama-style runtime for decision models: pulls and serves open encoders and decoders (Laya, Von, Kev, Decider, Nimble, Winnow, and more) with each author's calibration, behind `/v1/systemone`; the official TypeSafe Python SDK works against it unchanged. Site: [ollaya.dev](https://ollaya.dev).
- [Laya-MLX](https://github.com/mizorewww/laya-mlx) - Independent native MLX port of Laya for Apple Silicon: Choice, Score, and Noul without text generation or a cloud API, retaining upstream question formatting and calibration, with published port-fidelity checks and performance measurements
- [OpenRouter decision models](https://openrouter.ai/models?output_modalities=decisions) - Decision models from several publishers behind OpenRouter's alpha Decisions API, which chat-completions SDKs cannot call. Usage guide as an agent skill: [openrouter-decisions](https://openrouter.ai/skills/openrouter-decisions).
- [Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) - Hosts Jev as `typesafe-ai/jev`
- [stuntd](https://github.com/bladedevoff/stuntd) - Local proxy on the open Laya model that speaks the Jev System One API, records the app's Choice, Score and Noul answers from a Jev upstream, trains a per-question head, and serves it with a calibrated confidence threshold and fallback to the upstream
- [Bud Decision Studio](https://github.com/BudEcosystem/Bud-Decision-Studio) - Open-source, cross-platform desktop runtime and playground from Bud Ecosystem for running, evaluating, managing, and training Jev-like decision models locally, with a `/v1/systemone` API. Supports 10+ decision models.

## SDKs & Clients

Clients for the `/v1/systemone` API, official first. Most were written for TypeSafe's hosted Jev; the official TypeSafe SDKs also work against compatible servers such as Ollaya and Liquid d1. Community packages are not affiliated with any provider unless noted.

- [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) - Official client. `pip install typesafe-sdk`. Docs: [Python SDK](https://docs.typesafe.ai/sdk/python). The community [typesafe-ai](https://pypi.org/project/typesafe-ai/) package is a defensive redirect shim; install `typesafe-sdk` directly.
- [JavaScript / TypeScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) - Official client. `npm install @typesafe-ai/sdk`. Docs: [JavaScript SDK](https://docs.typesafe.ai/sdk/javascript).
- [System One adapter (Python)](https://github.com/typesafe-ai/system-one-adapter-python) - Official drop-in `TypeSafeClient` replacement backed by LLM APIs, for comparing Jev against chat models on the same questions. `pip install system-one-adapter`.
- [Vercel AI SDK provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) - `@ai-sdk/typesafe-ai` plus `experimental_evaluate`. Use `typeSafeAi.evaluationModel('jev-latest')` or the Gateway id `typesafe-ai/jev`.
- [Milvus Model](https://github.com/milvus-io/milvus-model) - Python reranker adapter that sends candidate documents as Jev Noul questions in one request, then sorts the returned scores and preserves original document indices
- [Elixir SDK](https://github.com/nshkrdotcom/typesafe_sdk) - Community Hex package [`typesafe_sdk`](https://hex.pm/packages/typesafe_sdk) for `system_one` and model listing. Docs: [HexDocs](https://hexdocs.pm/typesafe_sdk).
- [Jev (Elixir OTP)](https://github.com/dannote/jev) - Hex package [`jev`](https://hex.pm/packages/jev): Jev as a peer GenServer; answers arrive as messages you pattern-match, with network-free tests
- [Ruby SDK](https://github.com/joshmn/typesafe-sdk) - Community Ruby 3.1+ client: Noul / Choice / Score, retries, model listing, thread-safe pooled HTTP. No async client.
- [RubyLLM TypeSafe](https://github.com/kieranklaassen/ruby_llm-typesafe) - TypeSafe provider for RubyLLM 2 with offline model metadata and typed responses.
- [typesafe-ai-rails](https://github.com/GenieRobot/typesafe-ai-rails) - Unofficial Rails integration on the community `typesafe-sdk` Ruby gem: configuration, usage/cost telemetry, and opt-in confidence policies
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
- [System One Foundation Models](https://github.com/peterfriese/system-one-foundation-models) - Unofficial Swift 6 bridge mapping Apple's `@Generable` types to Noul, Choice, and Score, with hosted Jev, HTTP Laya, and on-device Core ML Laya backends plus confidence routing
- [discern](https://github.com/doeixd/discern) - Unofficial Effect library: Choice / Noul / Score answers become typed patterns with an explicit `Uncertain` branch you must handle, plus routable procedures, with recording, replay, caching and call budgets as `DecisionModel` middleware. Provider-neutral; reaches Jev through `@effect/ai-typesafe`
- [kojev (Kotlin Multiplatform)](https://github.com/ItisNoMatter/kojev) - Community client for JVM, Android, and iOS. Choice and Score answers come back as your own enums; one typed way to read them, no default thresholds. Maven Central: `io.github.itisnomatter:kojev:0.1.0`.
- [jev4k](https://github.com/pambrose/jev4k) - Unofficial JVM Kotlin client: Choice, Score, and Noul as a DSL, with answers read back as typed values including enums. Maven Central: `com.pambrose:jev4k`
- [hunch](https://github.com/steven-shoemaker/hunch) - Unofficial Python library, with a TypeScript port, that turns Choice / Score / Noul into functions over lists and DataFrames (classify, score, check, where, extract, pick, rank, verify), with deduplication, caching, and optional escalation of unsure rows to an LLM that must pick from the same labels
- [JevT++](https://github.com/wiatrM/jevtpp) - Unofficial C++20 library with compile-time enum schemas, typed decisions and abstention, local Laya backends, and an optional TypeSafe System One HTTP client; remote tests use mocks and loopback HTTP, not live-provider validation

## Applications

Open-source products and demos that put a decision model in a real loop. Most use Jev today.

- [MemSearch](https://github.com/zilliztech/memsearch) - Markdown memory for coding agents with an optional Jev Noul reranker and a published English/Chinese retrieval evaluation; community integration, not an official TypeSafe SDK
- [Jev-Mem](https://github.com/libingzheren/Jev-Mem) - Unofficial agent memory system where Jev or local Laya controls memory organization, query routing, retrieval budgets, candidate scoring, and stopping while an LLM writes answers; its [paper](https://arxiv.org/abs/2609.23986) reports LoCoMo results
- [Jev RAG](https://github.com/aifabrice/jev-rag) - Unofficial local-first knowledge search app using SQLite BM25 or agent-planned lexical retrieval, Jev `Noul` judgments for evidence reranking, and a published reproducible NFCorpus evaluation; no vector database is required by default
- [Jev Deep Research](https://github.com/sunyasheng/JevDeepResearch) - Unofficial experimental research agent: Jev Choice locates evidence and Noul checks its presence across document regions in parallel; Pi-Serini returns original passages for GPT to verify and continue
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) - Browser agent from [Browser Use](https://github.com/browser-use). Jev picks an operation and a DOM element in one request; a small LLM writes text only for `TYPE_TEXT`. Zürich → London on Google Flights in ~7s. Library, local inspector, and measurements included.
- [Jev Social](https://github.com/socai-io/jev-social) - Browser-grounded social research: Jev selects bounded Instagram, TikTok, and LinkedIn search/read operations, socai executes them in the user's Chrome, and reports cite the captured posts, comments, and video evidence; unofficial community project
- [Jev Web Analyzer](https://github.com/replynodes/jev-web-analyzer) - Community project that analyzes a public SaaS landing page as clean Markdown and asks Jev ten bounded `Choice` questions about first-visit understanding, including the first change to make.
- [jev-align (Sutro)](https://github.com/sutro-sh/jev-align) - Unofficial active-learning CLI that evaluates CSV, Parquet, and JSONL rows with Jev, asks people to label uncertain and audit samples, and uses GEPA to propose improved definitions
- [JevSpan](https://github.com/lzq-0529/jev-span) - Unofficial zero-shot named entity recognition for Chinese and English: code enumerates candidate spans at punctuation, Jev `Choice` questions nominate, verify, and fix the boundary of each entity, and every entity keeps its probability and a decision trace
- [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome) - Unofficial Chrome extension (Manifest V3) port of Jev Ultrafast: Jev picks the operation and DOM element in one request, a small text model writes typed values, and it runs in the user's own tabs through OpenRouter, TypeSafe or Cloudflare; includes a 17-task headless-Chromium suite with recorded traces.
- [jev-ego](https://github.com/romaluev/jev-ego) - Browser agent on [ego lite](https://lite.ego.app/): one TypeSafe request picks operation + indexed element; agent-facing observe/act/suggest/step CLI
- [jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) - Unofficial browser automation: an LLM plans the outcome, Jev decides each click/type on a Playwright snapshot (~300 ms/call). Ships as a library, CLI, and MCP server (`npx -y -p jev-browser jev-browser-mcp`).
- [Sedum](https://github.com/sedum-dev/sedum) - Unofficial open-source end-to-end AI testing tool for Playwright: in goal mode Jev picks each next action and its target, plain-English steps use a Jev Choice to find their element, and verify claims are two Nouls (holds, contradicted), while clicks, waits, verdicts and exit codes stay deterministic
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - macOS computer-use loop: OCR the screen, Jev classifies the next action, then click. About $0.0002/step.
- [Yappy](https://yappy.biz/jev/) - macOS voice agent (closed source, public write-up with measurements). On its hosted plan Jev picks the operation and target control from the window's accessibility table each step; a chat model writes text only for typing, and the full agent takes over when confidence drops. Author-reported: 275–690 ms per decision, $0.003 for five.
- [Mobile Jev](https://github.com/droidrun/mobile-jev) - Android agent on [Mobilerun](https://mobilerun.ai): Jev decides each tap. Opens Uber, SFO → Golden Gate, payment screen in ~21s / 9 actions. Live studio, CLI, and traces. No ADB.
- [Unclutter](https://github.com/kitze/unclutter) - Chrome / Firefox extension: Jev classifies nonessential page elements; local template rules hide them on later visits.
- [jevMail](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling) - Unofficial open-source Gmail AI spam filter, auto-labeler, and inbox organizer: Jev understands each email's intent to apply custom labels and optionally archive high-confidence unwanted mail
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
- [jev-lint](https://github.com/ckorhonen/jev-lint) - Unofficial fuzzy linter for Claude Code and Codex that uses Jev to flag team-rule violations at edit time, with configurable rule packs and repository-specific rules so agents can fix issues before code review
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
- [Jev Chat Assistant](https://github.com/jev-chat/jev-chat-jarvis) - Unofficial Android chat copilot: an accessibility service reads the visible QQ, X, or Feishu/Lark chat (Feishu text via on-device OCR), one batched Jev request asks intent, needs, and next-action `Choice` questions, a danger `Score`, and three `Noul` checks, a separate chat model drafts three replies that one more `Choice` ranks, and code fills the picked reply into the input box without sending
- [Paper Radar](https://github.com/Eliot5566/JEV-Paper-Radar) - Unofficial daily arXiv and bioRxiv radar. Jev answers one Noul per plain-English interest for every new paper; code applies the thresholds and publishes a page and RSS feed from GitHub Actions. [Live demo](https://eliot5566.github.io/JEV-Paper-Radar/public/) needs no key.

## Demos & Games

Toys, live sites, and realtime agents.

- [Yes / No](https://yesno.coderai.dev) - Free no-signup Noul demo. Ask a question, get yes / no / maybe, with web search when needed.
- [TypeSafe AdBlock](https://github.com/realZachi/typesafe-adblock) - Chrome extension demo: Jev judges candidate DOM elements and removes likely ads, with BYOK and no backend; each page consumes API tokens and the author documents missed ads and mistaken removals
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
- [1 Million Emojis](https://chriswijnia.com/lab/emoji) - A shared 1000 × 1000 emoji canvas, live for everyone; after each stroke Jev picks a square next to it and its emoji as one Choice ([source](https://github.com/cwdx/1-million-emojis))
- [Jevvie](https://chriswijnia.com/lab/jevvie) - Page companion: the page offers its actions as WebMCP tools, and one Jev `Choice` picks the action a visitor's request means (with a `Choice` per argument asked alongside), asking back when the top two are close; a voxel character then hops to the button and does it ([source](https://github.com/cwdx/jevvie)).
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
- [FlightBench](https://github.com/AlperKartkaya/FlightBench) - A fixed-wing landing simulator and benchmark where you can compete with Jev in landing a plane, mapping four Jev `Choice` decisions to aircraft controls and benchmarking landings against human-pilot, baseline, and LLM controllers.

## Agent Tools

Tools that expose decision models to coding agents and MCP clients.

- [TypeSafe agent skill](https://github.com/typesafe-ai/skills) - Official skill: primitives, patterns, and how to structure evaluations. Claude Code: `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai`. Other agents: `npx skills add typesafe-ai/skills --skill typesafe-ai`.
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Claude Code plugin and npm library: Jev scores tool calls and drops stale ones instead of summarizing context
- [SkillRanker](https://github.com/Dicklesworthstone/skillranker) - Rust CLI: Jev ranks which agent skill fits the next step from live session context, with Claude Code hooks
- [langchain-skill-router](https://github.com/deyna256/langchain-skill-router) - LangChain deepagents middleware for per-turn skill routing: Jev ranks and verifies which SKILL.md skills each turn needs from a catalog of hundreds, splitting the ranking to fit Jev's limits and falling back to the full catalog on failure. The judge is pluggable. `pip install "langchain-skill-router[jev]"`.
- [JevRouter](https://github.com/BillionsBobby/JevRouter) - Unofficial router that puts models, subagents, skills, MCP tools, and CLIs in one candidate set: Jev answers one Choice, and code enforces availability, permissions, risk, and confirmation. On 10 Toolathlon tasks, position-wise hits were 38–44% for Jev against 24% for DeepSeek V4.1 Flash
- [JevLoop](https://github.com/zjunlp/JevLoop) - Unofficial agent loop that sends each fork (tool, risk, done) to Jev 1.13.0 and keeps the LLM for writing; with no key it falls back to local Laya, then rules. `npm run demo` runs offline
- [Jevbridge](https://github.com/gamesonrblx/Jevbridge) - Unofficial ACP/MCP adapter: typed Jev decisions and computer use beside Codex, Claude, Grok, and OpenCode
- [Conscio](https://github.com/neguiolidas/conscio) - A local-first agent memory framework where Jev serves as a typed-decision voice on the decision council: it evaluates the decision state with choice/score/boolean questions, and the calibrated probabilities weight the council's verdict.
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
- [toolgate](https://github.com/RiskAverseTech/toolgate) - Unofficial tool-call firewall for Claude Code hooks and MCP servers: Jev answers seven risk questions per call and deterministic code maps them to allow/ask/deny, fails closed, and tracks write-then-execute across a session
- [Jevonian](https://github.com/xinyao27/jevonian) - Local OpenAI / Anthropic / Responses-compatible proxy where one Jev call answers both the model route and the thinking level for `jevonian/auto`, from session state (recent messages and tool results, consecutive errors, context headroom, quota, candidate capabilities, cache-switch penalties); deterministic code filters candidates and owns every threshold first, a pinned model or explicit `jevonian/<route>` skips Jev entirely, and each decision is recorded with the serving model, reason, token usage, and estimated cost.
- [jev-opus](https://github.com/WXK-AI/jev-opus) - Unofficial CLI and Claude Code gateway: runs Claude Code on Opus 5.5 and asks Jev typed Choice / Score / Noul questions on each prompt and after every tool batch to pick the next call's reasoning effort, with code enforcing floors and ceilings and sending the result as a per-message effort statement so the prompt cache is kept
- [jev-belay](https://github.com/valentynkit/jev-belay) - Claude Code Stop hook that checks the transcript for evidence before trusting a "done" claim, spending one four-question Jev call only when files changed with no passing check since, and failing open on every error path.
- [jev-commit](https://github.com/valentynkit/jev-commit) - Pre-commit hook where one Jev call judges whether the commit message matches the staged diff, flags debug leftovers and unmentioned work, and blocks only when it detects a credential.
- [jev-use](https://github.com/shitianfang/jev-use) - Claude Code, Codex and pi plugin: Jev answers the batched typed questions an agent loop needs, and a typed escalation contract hands writing and low-confidence steps back to the LLM
- [dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools) - DeepSeek Harness plugin: Jev prunes oversized tool output, screens fetched pages for injected instructions, and picks which skill fits the next step, plus the jev_ask and jev_gate tools
- [slop-grader](https://github.com/lukstei/slop-grader) - Rule-based CLI and agent skill that grades text against custom rulesets for AI slop, grammar, and technical documentation quality, and guides an AI agent to auto-fix violations
- [pytest-jev](https://github.com/allebee/pytest-jev) - pytest plugin for semantic assertions on LLM output: each plain-English claim about a reply becomes a Jev Noul in one request, a claim passes at p ≥ 0.8, and failures print every claim's probability; `choice` and `score` cover routing and rubric checks
- [jgrep (kyu1204)](https://github.com/kyu1204/jgrep) - Semantic grep for code, git diffs and CSV rows: one Noul per 5-60 line chunk, 16 chunks per Jev request, grep-style file:line output and exit codes for CI lint rules written in English
- [jevgrep (allebee)](https://github.com/allebee/jevgrep) - Streaming grep by meaning for logs: asks Jev one Noul per line against a plain-English question and prints the lines at or above a threshold, including from `tail -f`
- [wellposed](https://github.com/suraj-phanindra/wellposed) - Offline linter and agent skill for Jev requests: 40 structural checks with no model call (missing none-of-the-above options, broken state paths, wrong criteria shapes), plus Jev-on-Jev checks for what structure cannot decide, with labelled corpora that score both layers.
- [jev-auto-approve](https://github.com/BasmaAbouzied0/jev-auto-approve) - Claude Code PreToolUse hook: one Jev Noul per Bash command on whether it is strictly read-only; auto-approves at p ≥ 0.95, otherwise falls back to the normal permission prompt and never denies. A local hard-no list and injection filter keep risky commands away from Jev; 0 of 8 state-changing commands approved in its published calibration
- [jev-secret-guard](https://github.com/BasmaAbouzied0/jev-secret-guard) - Claude Code PreToolUse hook that stops agents writing or sending secrets: known key formats are blocked locally, unknown high-entropy strings go to Jev as a Noul only in masked form so the check never leaks the value; p ≥ 0.80 blocks, 0.30 to 0.80 or any Jev error asks the human. 6 of 6 secrets and 0 of 6 benign strings blocked in its published calibration

## Benchmarks & Evaluations

Leaderboards first, then single-task studies and evaluation tooling. Most studies so far measure Jev.

### Leaderboards

- [Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index) - Hugging Face Space comparing Jev with open decision models on a versioned benchmark suite, with calibration metrics and documented methods; open-model inference timings and Jev's hosted HTTPS latency are not directly comparable
- [JevBench](https://github.com/fstandhartinger/jevbench) - MIT-licensed harness and leaderboard of 534 English decisions with public and sealed tiers, reporting accuracy, latency, and price together. Discussion: [Show HN](https://news.ycombinator.com/item?id=49800574).
- [Jevals.com](https://jevals.com/) - Independent benchmark of hosted Jev and six LLMs on the same Noul, Choice and Score questions, graded against human labels (PubMedQA, Banking77, HelpSteer2), with per-decision logs as open data
- [LangWatch Jev benchmark](https://langwatch.ai/compare/jev-benchmark) - Jev against seven open models under 1B on 15 decision tasks, with 95% intervals, latency, and contamination checks

### Studies

- [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) - Side-by-side of Jev vs Qwen 3.8 27B on Cerebras for the same System One questions. Video: [Shannon](https://x.com/iamMrDuncan/status/2100467548298899918).
- [Jev Rerank Bench](https://github.com/anessbelbati/jev-rerank-bench) - Reranking comparison with raw provider responses, scoring code, uncertainty intervals, and documented limits.
- [Jev Spam Eval](https://github.com/bitnovus/jev-spam-eval) - Exploratory zero-shot spam study vs trained TF-IDF baselines, with post-hoc-tuning caveats.
- [Jev × NASA Kepler](https://gist.github.com/ipaulsmith/e5c3ae3a492a455435d5bfc161404312) - Independent retrospective test of Jev 1.13 on 8,054 historical Kepler Objects of Interest with NASA Exoplanet Archive dispositions hidden during prediction; 72.5% archive-disposition match vs 64.4% for a fixed 3-rule baseline, with exact requests, metrics, baseline, and caveats
- [Jev Phishing Bench](https://github.com/anisselbd/jev-phishing-bench) - 2,000 emails: Jev vs Claude Haiku 4.5 on click-or-not, with calibration, latency, and cost. Haiku wins accuracy here.
- [jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark) - Who&When Pro (injected agent failures): Jev vs a strong LLM on who / which step / error category.
- [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) - Blind prompt-injection and vulnerable-code detection benches on public corpora, built on jev-go.
- [ASSAY-001](https://github.com/jourdanlabs/assay-001) - Independent pre-registered check of Jev calibration and type safety on Banking77 / CLINC150. Split verdict, full logs. Write-up: [donttrustme.ai](https://donttrustme.ai/assay-001.html)
- [Jev search rerank eval](https://github.com/zhuyansen/jev-search-rerank-eval) - 9,831 labelled pairs: Jev rerank vs BM25 / bge-m3, with judge-circularity measured. Fusion wins; Jev alone does not beat embeddings
- [Smoking-history extraction benchmark](https://github.com/vclic/smoking-extraction-benchmark) - 1,000 synthetic notes: Jev vs OpenAI structured outputs on accuracy, cost, and latency
- [jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench) - Compares batched and separate Jev calls in 2,976 requests through OpenRouter, reporting approximately 261 fixed input tokens per request, charges matching the published token rate, and answer differences comparable to repeat-request noise.

### Tooling

- [System One Playground](https://github.com/goodboybeau/system-one-playground) - Local Apple Silicon workbench comparing Laya, Decider, Kev, Jev, and other engines side by side, with public-dataset benchmarks for accuracy and calibration, input-truncation diagnostics, latency, memory, and load tests
- [Jev DSPy Lab](https://github.com/jmanhype/jev-dspy-lab) - Unofficial DSPy companion that records and replays TypeSafe calls while measuring calibration, selective risk, confidence-gated abstention, latency, tokens, and modeled cost.
- [jevcal](https://github.com/abhixhek/jevcal) - Unofficial CLI that fits a per-question confidence threshold to a target accuracy on your own labeled data, verifies it on a held-out split, shows how much traffic still needs an LLM fallback, and fails CI when a Jev update breaks the locked thresholds

## Papers

- [Typed Decision Models: An Early Evidence Audit and Evaluation Checklist](https://arxiv.org/abs/2609.32160) - Reviews 28 papers from the first days after Jev's release: the typed readout shows no independent accuracy advantage over comparable label-probability readouts, the clearest gains are latency and cost, and the paper derives a 14-item evaluation checklist
- [Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](https://arxiv.org/abs/2609.30216) - First data-driven survey and analysis of Jev's application ecosystem across 2,170 public GitHub projects, covering rapid early growth, application domains, and decision-use patterns
- [Evaluating and Benchmarking the System One Model Jev](https://arxiv.org/abs/2609.37647) - Zero-shot Jev 1.13 on 37 datasets (346,009 requests for under $10) against Qwen3.8-27B and Gemma-4-E4B option probabilities: Jev beats Qwen on 27 of 37 and Gemma on all 37, with well-calibrated choice probabilities but poorly placed binary thresholds. Code and raw responses released.
- [Beyond Calibration: Do a Typed-Decision Model's Probabilities Obey the Probability Axioms?](https://arxiv.org/abs/2609.33209) - Label-free coherence checks: Jev's probabilities for "X" and "not X" miss summing to one by 0.064 on average against 0.293 for Qwen3.8-27B's first-token readout, and its single-label probabilities over-sum to 1.14
- [Evaluating System One Models for Agent Security Decisions](https://arxiv.org/abs/2609.33401) - Jev, Laya, Decider, and Nimble against specialized classifiers and LLM judges on prompt injection and risk screening: good aggregate calibration can hide confident failures concentrated in particular attack groups
- [JevAdvBench](https://arxiv.org/abs/2609.31142) - First adversarial benchmark for decision models: 812 typed questions and 9,744 single-edit attacks. On Jev 1.13, one unverified opinion appended to the state flips 12.1% of decisions, so the state should be treated as untrusted input.
- [From Text Decisions to Pixels](https://arxiv.org/abs/2609.29283) - PixelJev, a native-image decision interface on small open multimodal models; 64-shot adaptation lifts Pets accuracy from 60.13% to 92.40%, while calibration does not follow accuracy gains
- [Chinese-Jev](https://arxiv.org/abs/2609.36965) - Encoder-only System One model for Chinese, pretrained on 10 million examples and fine-tuned for medicine, law, and finance, with the CJ-Bench benchmark; the authors report higher general-domain accuracy than Jev at a 20x speedup
- [Calibrated Decision Models for Autonomous Penetration-Testing Harnesses](https://arxiv.org/abs/2609.28940) - Where Jev and Laya fit in LLM pentest agents: finding adjudication, severity recalibration, agent pruning, and confirmation loops, with an exploratory case study

## Articles

Independent measurements and experiments.

- [Jev in Search: Three Practical Evaluations](https://zc277584121.github.io/rag/2026/09/22/jev-search-deep-evaluation.html) - Independent experiments on search stopping, memory reranking, and multi-hop relation selection, with implementation links and limitations including private data, unequal sample counts, and a simulated speed illustration
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

- [awesome-jev-prompts](https://github.com/vicfei/awesome-jev-prompts) - 43 field-tested Jev question patterns (Choice/Score/Noul) with templates, thresholds, and failure modes, plus 10 anti-patterns. CC0, bilingual EN/中文.
- [MrJev/awesome-jev](https://github.com/MrJev/awesome-jev) - Selective list behind a 10-star bar, with hands-on reviews at [mrjev.com](https://mrjev.com/best-jev-tools/) recording what each tool sends and where.
- [Awesome TypeSafe Jev](https://github.com/AbdelStark/awesome-typesafe-jev) - Unofficial source-backed Jev field guide with a typed-decision walkthrough, community project cards, independent evaluation links, and a first-contribution path
- [laya.tools](https://laya.tools) - Unofficial directory of about 950 projects built on the open Laya model, from GitHub, npm, Hugging Face and X, browsable by platform and use case, with a Laya vs Jev comparison. Not affiliated with TypeSafe or ConvAI
- [AgentPlugins JEV directory](https://agentplugins-2v1.pages.dev/jev-plugins/) - Cross-ecosystem JEV plugin & tool directory covering browser-use/jev-ultrafast, Laya, Kev and fast-jev-compaction, ranked by GitHub stars, with a practical [JEV tutorial](https://agentplugins-2v1.pages.dev/typesafe/) and a [Laya vs Jev vs Kev comparison](https://agentplugins-2v1.pages.dev/laya-vs-jev/). Not affiliated with TypeSafe.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: open a pull request that adds a project with a link and a one-line description. Useful, interesting, and built on or around a decision model.

## License

[CC0 1.0](LICENSE) — this list is dedicated to the public domain.
