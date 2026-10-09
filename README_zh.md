# Awesome Decision Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

精选的决策模型（decision model，也称 System One 模型、类型化决策模型）资源，以及围绕它们的 API、运行时、工具、应用、评测与研究。

**[English](README.md)** | **[简体中文](README_zh.md)** · [网页版](https://anotiawang.github.io/awesome-decision-models/?lang=zh)

决策模型读入一段状态（文本、JSON，部分模型也支持图片），再加上答案事先声明好的问题，为每个答案返回一个概率，而不是生成文本。问题有三种形态：Noul（某个陈述为真的概率）、Choice（从你给的选项里选一个）和 Score（在有序量表上的等级）。TypeSafe AI 在 2026 年 9 月用 [Jev](https://docs.typesafe.ai/introduction) 和它的 `/v1/systemone` API 开创了这一类别，下面许多模型和运行时都接受同样的请求格式。

由社区维护，与任何模型厂商无隶属关系。欢迎 PR。

## 目录

- [托管 API](#托管-api)
- [开源模型](#开源模型)
- [推理方法](#推理方法)
- [运行时与平台](#运行时与平台)
- [SDK 与客户端](#sdk-与客户端)
- [应用](#应用)
- [Demo 与游戏](#demo-与游戏)
- [Agent 工具](#agent-工具)
- [评测与排行榜](#评测与排行榜)
- [论文](#论文)
- [文章](#文章)
- [相关](#相关)
- [贡献](#贡献)

## 托管 API

只提供 API 的模型，按发布时间排序。厂商同时托管的开源权重模型（如 Clef、pplx-decider）放在[开源模型](#开源模型)。

- [Jev](https://docs.typesafe.ai/introduction) - TypeSafe AI 的第一个 System One 模型，也是 `/v1/systemone` API 的源头：一次请求里对文本状态回答 Noul、Choice 和 Score 问题。密钥在[控制台](https://console.typesafe.ai/settings/keys)获取；也可以通过 Vercel AI Gateway、Cloudflare Workers AI 和 OpenRouter 调用。
  - [Playground](https://console.typesafe.ai/playground) · [控制台](https://console.typesafe.ai) · [GitHub](https://github.com/typesafe-ai) · [Workflow evals](https://evals.typesafe.ai) · [Cookbook](https://docs.typesafe.ai/llms.txt) · [模式](https://docs.typesafe.ai/patterns)
  - [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) - 已知失败模式
  - 社区：[Discord](https://discord.gg/typesafe)（builder demo 在 [Show and Tell](https://discord.com/channels/1483217544214085663/1483217545040232493)）· [X @typesafeai](https://x.com/typesafeai)
- [meraGPT Decider 1](https://meragpt.com/docs) - 托管决策模型（`state-decider-1`，别名 `sd-1`），通过 `/v1/systemone` 回答 Noul、Choice 和 Score，可用 TypeSafe SDK 调用；请求上限为 4,096 token，Choice 最多十个标签
- [Solar Decide](https://openrouter.ai/upstage/solar-decide) - Upstage 基于 Solar Mini 4 的决策模型，目前为 beta，512K 上下文，请求格式与 Jev 相同。[Solar Decide Flash](https://openrouter.ai/upstage/solar-decide-flash) 是低延迟版本。
- [Span-01](https://www.respan.ai/blog/introducing-span-1) - Respan 面向 AI trace 的行为分类模型：对你用自然语言定义的每种行为（提示注入、幻觉、Agent 死循环等）判断为出现、未出现或无法观察。Span-01 及其 Lite 版已上架 [OpenRouter](https://openrouter.ai/respan/span-01)。
- [d1](https://docs.liquid.ai/lfm/models/decision-models) - Liquid AI 的第一个决策模型，支持文本和图片，提供可用 TypeSafe SDK 调用的 `/v1/systemone` 端点，也上架了 [OpenRouter](https://openrouter.ai/liquid/d1)（目前仅文本）。发布文章：[blog](https://www.liquid.ai/blog/d1-decision-model)。未公开模型规模。
- [OpenAI Decisions API](https://openai.com/index/devday-2026-recap) - 在 DevDay 2026 发布，2026 年 10 月起公开 beta：由 GPT-6 Luna 针对文本、JSON 或图片 state 回答 Noul、Choice 和 Score 问题，为每个选项给出概率，不生成文本。也以 GPT-6 Luna Decisions 上架 [OpenRouter](https://openrouter.ai/openai/gpt-6-luna-decisions)。
- [Mercury Decide](https://openrouter.ai/inception/mercury-decide) - Inception 的决策模型，OpenRouter 上有免费线路；Inception 称每秒最多可做 14 次决策。

## 开源模型

可以下载并自行运行的开源权重模型。分数均为各项目在自选 benchmark 上的自报结果，不同条目之间不可直接比较。

### 公司与机构发布

- [Clef](https://huggingface.co/Cloudflare/clef) - Cloudflare 基于 Qwen3.8-27B 后训练的 Apache-2.0 决策模型：Clef 可读文本、JSON、图片或视频，对所有问题的所有选项联合打分；Clef-flash 是更小更快的版本。两者都托管在 Workers AI 上，API 与 Jev 兼容。发布文章附 Jev Decision Index 成绩：[blog](https://blog.cloudflare.com/clef-decision-models)。
- [pplx-decider-v1.1-27b](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b) - Perplexity 基于 Qwen3.8-27B 微调的 Apache-2.0 多模态决策模型；v1.1 去掉了因果掩码并用更多数据训练，模型卡报告 Jev Decision Index 61.56，Jev 为 57.9。也可通过 [Perplexity Decisions API](https://docs.perplexity.ai/docs/decisions/quickstart) 和 [OpenRouter](https://openrouter.ai/perplexity/pplx-decider-v1.1-27b) 调用。
- [Strands Decider 2B](https://github.com/strands-labs/strands-decider) - AWS Strands Labs 的决策模型：把 Qwen3.5-2B 的 LM head 换成约一百万参数的 pointer head 为每个选项打分，并加 rank-16 LoRA。权重、训练数据和脚本全部公开；[发布文章](https://strandsagents.com/blog/introducing-strands-decider)用它在 Strands Agent 调用工具前做检查。
- [Nimble](https://github.com/bespokelabsai/nimble) - Bespoke Labs 用对比式筛选的合成数据对 Qwen3.5-9B 做的 9B LoRA 微调，附公开的 13 个数据集评测套件。Ollama 中名为 `nimble`。
- [Tev1](https://huggingface.co/togethercomputer/Tev1-4B-experimental) - Together AI 基于 Qwen3.5 的实验性监督微调模型（4B 和 0.8B），同时发布了[花 17 美元训练自己的决策模型](https://www.together.ai/blog/how-to-train-your-own-jev)的教程。Ollama 中名为 `tev1`。
- [Laya](https://github.com/NandhaKishorM/laya) - Convai Innovations 的多语言非自回归决策模型：一次前向完成 Choice、Score 和 Noul，权重和 PyPI 包已公开，并按请求选择检查点
- [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide) - Fastino 基于 DeBERTa-v3-large 的 Apache-2.0 决策分类模型：调用方定义任务和标签，通过 `gliner2` 在 CPU 或 GPU 上一次前向返回概率，面向业务分类、路由与有序评分
- [Standard One](https://huggingface.co/StandardThinking/StandardOne-8B) - Standard Thinking 基于 Ministral 3 的 Apache-2.0 决策模型（3B、8B），保留 Pixtral 视觉编码器：输入文本或图片，通过 `/v1/systemone` 返回选项概率，附合并权重、适配器、GGUF 和服务端代码
- [OpenJev](https://huggingface.co/openjev/openjev) - 独立开放权重决策模型，一次前向为调用方定义的选项打分，附校准与服务端代码；权重采用 CC BY-NC 4.0，仅限非商业用途，辅助与服务端代码采用 Apache-2.0。与曾名为 OpenJev 的 SemIf 是不同项目。
- [StartLux-Decision](https://github.com/StartLuxLabs/StartLux-Decision) - 原点星辉（StartLux）的类型化决策模型，含 0.8B 到 27B 五档稠密模型和一个 35B-A3B MoE，通过 `/v1/systemone` 读取最长 256K token 的文本、JSON 或图片；作者报告在 Decision Index 0.2.1 上得分 63.88，Jev 为 57.91。代码为 Apache-2.0，权重为 CC BY-NC 4.0。
- [Decision 2.0](https://huggingface.co/collections/vllm-sr/decision-20-6ab7cf7bdfb506bf8269cb00) - vLLM Semantic Router 的 Apache-2.0 决策模型，规模从 0.6B 到 27B：一次前向回答同一输入上最多 64 个 Choice、Noul 和 Score 问题，可直接用 Transformers 加载
- [Intern-Decision](https://github.com/InternLM/Intern-Decision) - InternLM 基于 Qwen3.5 微调、冻结视觉塔的多模态决策模型（0.8B、2B、4B）：输入 state、可选图片以及 Choice、Score、Noul 问题，输出概率。附训练代码、两套推理后端、温度校准和 96 例分布校准 benchmark；权重在 [Hugging Face](https://huggingface.co/collections/internlm/intern-decision)。
- [Security-One 27B](https://huggingface.co/superagent-ai/security-one-27b) - Superagent 面向安全分诊的 Apache-2.0 决策模型，基于 AutoJev-27B（Qwen3.8-27B）微调：一次前向为提示注入、工具调用、代码变更和告警严重度等问题的候选项打分。发布文章：[blog](https://www.superagent.sh/blog/introducing-security-one)。
- [Jeeves](https://github.com/PostHog/jeeves) - PostHog 的 9B Jev-like 模型（Qwen3.5-9B + LoRA + pointer head），用 CISPO 训练成先推理再决策，并配扩散草稿模型加速；在 JevBench 231 道公开题上报告 0.935，Jev 为 0.866。训练代码和数据均已公开。

### 社区模型

- [Kev](https://github.com/jaredpalmer/kev) - Qwen3.5 决策模型（0.8B、4B、9B），可以自己训练和部署。一次前向完成 Choice、Score 和 Noul，权重和固定评测集已公开，本地服务实现 `/v1/systemone`。
- [Von](https://github.com/wfzyx/von) - 本地非自回归 System One 模型，服务端兼容 `/v1/systemone`，带 Doom 演示：每步动作是一次前向
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - 0.6B 并行决策模型：输入状态和问题，一次前向给出完整分布，不解码文本。权重已公开，同一检查点可玩 ViZDoom、迷宫和贪吃蛇；作者自己的 ViZDoom Basic 划分上是 128/128，对照 Jev 为 56/128。
- [jevlike](https://github.com/vinnylarouge/jevlike) - 训练一个小的单次 scorer：上下文 + N 个文本选项 → 每个选项一个概率。含 Doom / 国际象棋视觉 demo，以及 Wikispeedia 下一跳例子。明确*不是* TypeSafe 架构或 RLCD 的复现。
- [decider](https://github.com/Mapika/decider) - 基于 Qwen3.5-2B 的微调：一次前向就给出类型化决策和校准概率
- [RSI-Jev](https://github.com/Shanghua-Gao/RSI-Jev) - 由递归自我改进（RSI）的 AI 研究系统训练的 Jev-like 模型，公开每一次实验（包括失败的）。4B 和 27B（v6.1-VL），一次前向为 Choice、Score、Noul 的每个选项给出概率，可读文本或图片，可选 effort 档位（low、medium、high，或按问题自选深度的 auto），开放权重，提供兼容 `/v1/systemone` 的服务。
- [jev-style](https://github.com/lawrence3699/jev-style) - 0.8B 决策模型（Qwen3.5 微调），`pip install "jev-style[torch]"`（Apple 芯片用 `[mlx]`）即可在本地运行（PyTorch、MLX，或配合单独编译的打分程序用 llama.cpp），提供兼容 `/v1/systemone` 的服务：一次前向回答 Choice、Score、Noul，并附带 MCP 服务和 Claude Code 守门钩子
- [PlayJev](https://github.com/OmniJev/PlayJev) - Qwen3.5-0.8B-Base 微调后从 448 px 画面玩十款浏览器小游戏：每步一次前向，概率直接从选项字母上读出，不生成任何文本。权重和十款游戏的浏览器 demo 都已公开。
- [OneJev](https://github.com/OmniJev/OneJev) - OmniJev 团队的开源多模态 System One 模型，四种尺寸（0.8B 到 27B）：对截图、照片、视频或文本提出 Choice、Score、Noul，一次前向为每个选项给出校准概率。权重在 Hugging Face。
- [jevos](https://github.com/feder-cr/jev) - 1B 决策模型，面向纯 CPU 笔记本：把 MiniCPM5 裁剪到 17 层并接一个单 logit 输出头，GGUF q4_k_m 量化后 619 MB，跑在 llama.cpp 上不需要 GPU，短请求约 54 ms。只支持 Jev `/v1/systemone` 协议里的 Noul（是/否）问题，Choice 和 Score 会返回 422。
- [WebJev](https://github.com/lexmount/WebJev) - 浏览器 agent 决策模型，接口与 Jev 兼容：基于 Qwen3.5-35B-A3B 微调，在 Jev Ultrafast 循环中选择下一步操作和目标元素，提供兼容 `/v1/systemone` 的服务。在 125 个由确定性判据评分的真实网站任务上，同一 agent 中完成率为 38.5%，Jev 1.13 为 16.7%。公开 Apache-2.0 权重、训练数据、训练方法和演示应用。
- [Vev](https://github.com/Xiaooolong/vev) - 支持视觉输入的 Jev 开源实现，基于 Qwen3.5 4B / 9B 微调。截图、照片可以直接放进 state，Choice、Score、Noul 结合文本与图像作答，概率直接从标签 token 上读出，不生成文本。提供兼容 `/v1/systemone` 的服务，代码与权重开源，权重仅限非商用。
- [JEV-27B](https://huggingface.co/autotrust/JEV-27B) - AutoTrust 以 Jev 1.13 为教师、在 Qwen3.8-27B 上蒸馏的 Apache-2.0 模型；同一个 vLLM 引擎既提供决策，也提供未改动的 Qwen 用于普通生成。作者自测六个公开决策 benchmark 平均 84.07，Jev 为 83.85。较小版本：[JEV-9B](https://huggingface.co/autotrust/JEV-9B)。
- [Winnow](https://huggingface.co/EldanRing/Winnow-12B) - 面向类型化决策的 Apache-2.0 Gemma 4 微调（12B 和 E4B），基于 llama.cpp 的服务同时提供 `/v1/systemone` 和 `/v1/chat/completions`。
- [JevK5](https://github.com/allebee/jevk5) - 基于 Qwen3.5 的 Apache-2.0 决策模型（2B、4B、9B），提供 `/v1/systemone` 服务，并有可在 CPU 和 GPU 上用 llama.cpp 运行的 GGUF 版本
- [reflex](https://github.com/kshetrajna12/reflex) - 基于冻结 Qwen3.5-4B 的小型决策模型：单个 `/v1/systemone` 端点，一次前向约 200 ms 作答，并在 JevBench 公开题上与 Jev 对比
- [imajev](https://huggingface.co/mohit67890/imajev-4b) - 基于 Qwen3.5-4B 的 Apache-2.0 4B LoRA，用于针对照片的决策：把照片和你的记录核对，或比较两张照片；训练了 `unknown` 概率，应用可以停下而不是瞎猜。请求格式为 Jev 的格式外加 `images`，可用 MLX 或 PyTorch 运行。
- [NeoHorse-Jev-4B](https://huggingface.co/TokenRhythm/NeoHorse-Jev-4B) - TokenRhythm 基于 NeoHorse-1-4B 的 Apache-2.0 4B 决策模型：输入文本或单张图片加文本，只做 prefill 推理，提供 `/v1/systemone` 服务
- [WaterSheep](https://github.com/SamratDuttaOfficial/WaterSheep) - Apache-2.0 开源权重的文本决策模型：Noul、Choice、Score 和多标签问题都为每个选项给出校准概率，由本地 `/v1/systemone` 服务提供，TypeSafe 官方 Python SDK 无需修改即可使用
- [Wald-4B](https://huggingface.co/org2ai/Wald-4B) - 基于 Qwen3.5-4B-Base 全量训练的 Apache-2.0 4B 解码器决策模型，可选思考模式，输出校准后的选项概率，附面向 CUDA GPU 的自托管 `/v1/systemone` 服务（[GitHub](https://github.com/org2AI/wald-4b)）
- [Valen](https://github.com/Liuziyu77/Valen) - Apache-2.0 多模态 System One 模型（0.8B、2B、4B）：输入文本、图片和视频，输出候选项上的概率，附训练代码、训练数据和在线 demo

## 推理方法

不训练或少量训练、直接让现有模型表现得像决策模型的方法，通常是在一次前向中读出各选项的概率。

- [SemIf](https://github.com/TheoLeeCJ/SemIf-OpenJev) - 原名 OpenJev。用开源模型在家用 RTX 3090 和浏览器里做类型化决策，直接读选项 logits，不生成文本。
- [LitJev](https://github.com/zhengxuyu/litjev) - Jev 的复现：把任意 Qwen 模型变成快速决策模型，提供与 Jev 相同的 `/v1/systemone` schema（Choice、Score、Noul），不训练、不生成回答文本
- [TetraJev](https://github.com/FeiLiuEM/tetrajev) - 可本地部署的决策层，处理跨领域的复杂决策：两个冻结的开源权重读取器对每条样本给出四次读数（选项字母，以及逐候选项的是/否），无拟合地融合，再按一致性路由并设有校准后的放行门；已在八个决策套件和 RAG 重排上评测，包括 DecisionBench 的 35 类真实任务。全程不训练。
- [jevmlx](https://github.com/bnsd55/jevmlx) - 给任意 MLX 模型做 Jev 风格并行约束决策：一次前向得到带概率的、按 schema 合法的 JSON
- [JEVfire](https://github.com/kikoncuo/jevfire) - CUDA LLM 上的 Jev 风格并行决策（vLLM），带浏览器马里奥 demo（本地约 71 ms/步）
- [PocketJev](https://github.com/NullPo-jp/PocketJev) - iPhone 端侧视觉判断：MLX + Qwen3-VL 选项 logits。相机 + 三选一，不生成文字，约 1 秒，不存照片。
- [jev-visual](https://github.com/hr98w/jev-visual) - Apple Silicon 上的教学向 Jev 风格视觉推理：共享多模态上下文、候选打分，含分拣厂 / Breakout / 手势 demo
- [DiffusionGemma 决策端点](https://huggingface.co/spaces/victor/DiffusionGemma-free-endpoint) - 免费的 Hugging Face Space：不做微调，直接从 DiffusionGemma 读出每个答案的概率，对外使用 `/v1/systemone` 协议
- [AnyJev](https://github.com/nokia-applied-research/AnyJev) - Nokia 的免训练方法：把任意 LLM 变成 Jev 式决策模型，打乱选项顺序时答案保持一致；另有自蒸馏的 Tacit 模型（1.7B 到 9B），可把有上限比例的低置信度决策交给模型自身推理。`pip install anyjev`。
- [simple-jev](https://github.com/featherless-ai/simple-jev) - Featherless AI 的服务端：无需训练分类头，就能把兼容的 Hugging Face 开源模型变成 `/v1/systemone` 分类端点，另有 Laya 后端和可复现的提示格式搜索

## 运行时与平台

运行决策模型的服务端、网关与原生运行时。

- [Ollama](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models) - 从 0.35 起在本地提供 `/v1/systemone`；模型库里首批决策模型是 `nimble` 和 `tev1`。
- [llama.cpp](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) - `llama-server` 通过 `/v1/systemone` 提供 Laya、Kev-4B、OpenJev、Clef 等决策模型，支持图片 state，router 模式可按需加载多个模型
- [SGLang](https://docs.sglang.io/docs/supported-models/decision_models) - 原生 `/v1/decisions` 和 `/v1/systemone` 端点，从经过验证的对话模型的下一 token 分数读出选项概率，无需专门的 checkpoint
- [vLLM Jev](https://github.com/mode-io/vllm-jev) - 在 Linux 和 Apple Silicon 上用 vLLM 原生部署决策模型，支持 Valen 的图片与视频问题
- [Unsloth](https://unsloth.ai/docs/models/decision-laya) - Unsloth 桌面应用可在 macOS、Windows 和 Linux 本地通过兼容 TypeSafe 的 `/v1/systemone` API 提供 Laya 和 Clef
- [Ollaya](https://github.com/ollaya-dev/ollaya) - 面向决策模型的 Ollama 式运行时：拉取并运行开源 encoder 与 decoder 模型（Laya、Von、Kev、Decider、Nimble、Winnow 等），沿用各作者的校准，对外提供 `/v1/systemone`；官方 TypeSafe Python SDK 无需修改即可连接。官网：[ollaya.dev](https://ollaya.dev)。
- [Laya-MLX](https://github.com/mizorewww/laya-mlx) - 面向 Apple Silicon 的独立 Laya 原生 MLX 移植：本地完成 Choice、Score 和 Noul，无文本生成或云 API，沿用上游问题格式与校准，附公开的移植一致性检查和性能测量
- [Laya-CoreML](https://github.com/mizorewww/laya-coreml) - Laya-MLX 作者的 Laya Core ML 与神经引擎移植，附移植一致性验证和可复现的速度、能耗测试；M3 Max 上短决策约 5 ms
- [laya.cpp](https://github.com/lkarlslund/laya.cpp) - 基于 ggml 的 Laya 原生 C++ 推理，支持 CUDA、Vulkan 和 Core ML 后端，附自动批处理的 Jev 兼容 HTTP 服务和预编译二进制
- [sys1](https://github.com/alvarobartt/sys1) - 基于 candle 的 Rust 服务端，自托管 Laya 等开源决策模型，提供 System One 兼容 API、按 token 动态批处理，支持 CPU、Metal 和 CUDA
- [OpenRouter 决策模型](https://openrouter.ai/models?output_modalities=decisions) - OpenRouter alpha 版 Decisions API 上多家发布方的决策模型；chat completions SDK 无法调用该 API。使用指南以 Agent skill 形式提供：[openrouter-decisions](https://openrouter.ai/skills/openrouter-decisions)。
- [Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) - 以 `typesafe-ai/jev` 托管 Jev
- [stuntd](https://github.com/bladedevoff/stuntd) - 基于开放 Laya 模型的本地代理，实现 Jev System One API；记录来自 Jev 上游的 Choice、Score 和 Noul 答案，为每个问题训练一个决策头，并以校准过的置信度阈值提供服务，低于阈值时回退到上游
- [Bud Decision Studio](https://github.com/BudEcosystem/Bud-Decision-Studio) - 来自 Bud Ecosystem 的开源跨平台桌面运行时与 Playground，可在本地运行、评测、管理和训练 Jev 风格决策模型，并提供 `/v1/systemone` API。支持 10+ 个决策模型。

## SDK 与客户端

调用 `/v1/systemone` API 的客户端，官方在前。大多数是为 TypeSafe 托管的 Jev 编写的；官方 TypeSafe SDK 也能连接 Ollaya、Liquid d1 等兼容服务。除非另行说明，社区包与任何厂商都无隶属关系。

- [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) - 官方客户端。`pip install typesafe-sdk`。文档：[Python SDK](https://docs.typesafe.ai/sdk/python)。社区包 [typesafe-ai](https://pypi.org/project/typesafe-ai/) 是为防占名而注册的重定向包；请直接安装 `typesafe-sdk`。
- [JavaScript / TypeScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) - 官方客户端。`npm install @typesafe-ai/sdk`。文档：[JavaScript SDK](https://docs.typesafe.ai/sdk/javascript)。
- [System One adapter（Python）](https://github.com/typesafe-ai/system-one-adapter-python) - 官方提供的 `TypeSafeClient` 替身，后端走 LLM API，方便用同一套问题对比 Jev 与聊天模型。`pip install system-one-adapter`。
- [Vercel AI SDK provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) - `@ai-sdk/typesafe-ai` + `experimental_evaluate`。可用 `typeSafeAi.evaluationModel('jev-latest')`，或 Gateway id `typesafe-ai/jev`。
- [Pydantic AI](https://pydantic.dev/docs/ai/api/models/system_one) - `pydantic_ai.models.system_one` 可向任意 `/v1/systemone` 端点发送类型化问题，并有 TypeSafe Jev 及其他决策模型的 provider 文档
- [Milvus Model](https://github.com/milvus-io/milvus-model) - 社区 Python 重排适配器，一次请求用 Jev Noul 判断候选文档，再按分数排序并保留原始文档索引
- [Elixir SDK](https://github.com/nshkrdotcom/typesafe_sdk) - 社区 Hex 包 [`typesafe_sdk`](https://hex.pm/packages/typesafe_sdk)，支持 `system_one` 与模型列表。文档：[HexDocs](https://hexdocs.pm/typesafe_sdk)。
- [Jev（Elixir OTP）](https://github.com/dannote/jev) - Hex 包 [`jev`](https://hex.pm/packages/jev)：把 Jev 当成对等 GenServer，答案以消息到达再 pattern match，测试可以不碰网络
- [Ruby SDK](https://github.com/joshmn/typesafe-sdk) - 社区 Ruby 3.1+ 客户端：Noul / Choice / Score、重试、模型列表、线程安全连接池。没有异步客户端。
- [RubyLLM TypeSafe](https://github.com/kieranklaassen/ruby_llm-typesafe) - RubyLLM 2 的 TypeSafe provider，带离线模型元数据和类型化响应。
- [typesafe-ai-rails](https://github.com/GenieRobot/typesafe-ai-rails) - 非官方 Rails 集成，基于社区 Ruby gem `typesafe-sdk`：配置、用量/成本遥测，以及可选的置信度策略
- [Rust SDK (typesafe-ai-rs)](https://github.com/gilljon/typesafe-ai-rs) - 独立的异步 / 阻塞 System One 客户端。
- [TypeSafe AI for Rust](https://github.com/Twister915/typesafe-ai) - 另一个 Rust 客户端：异步 + 阻塞传输、类型化响应、可观测重试。
- [typesafe-rs](https://github.com/AbdelStark/typesafe-rs) - 偏延迟的 Rust 传输 SDK，目标对齐官方客户端行为。
- [s1-rs](https://github.com/AbdelStark/s1-rs) - Rust derive 层：Choice / Score / Noul、类型化问题集、置信度门控、无网络测试。
- [Advocaat](https://github.com/pithings/advocaat) - 小型 TypeScript 客户端，给 chance / choice / score 打了 tagged helper。
- [Scala / ZIO SDK](https://github.com/jamesward/zio-typesafe-ai) - 社区 ZIO 客户端，带 noul / choice / score 的小 DSL。
- [.NET SDK](https://github.com/saibimajdi/typesafeai-dotnet-sdk) - 社区客户端，类型化问题 + 带置信度的答案。
- [PHP SDK](https://github.com/Butochnikov/typesafe-sdk-php) - 非官方 PHP 客户端：类型化 DTO、Promise 与异常。下面的 Laravel 包基于它。
- [Laravel TypeSafe Jev](https://github.com/Butochnikov/laravel-typesafe-jev) - 非官方 Laravel 12/13 集成：配置、Facade、scoped DI，以及基于 PHP SDK 的 recording fake。
- [jev-go](https://github.com/Gaurav-Gosain/jev-go) - 非官方 Go 客户端，返回类型化判断与校准概率。`go get github.com/Gaurav-Gosain/jev-go`。
- [Stumble/jev-go](https://github.com/Stumble/jev-go) - 非官方零依赖 Go SDK，支持 TypeSafe 直连和 Vercel AI Gateway，并提供类型化问题、重试、交互式 CLI 和可安装的 agent skill
- [jevclient](https://github.com/AboveColin/jevclient) - 非官方异步 Python 客户端（`pip install jevclient`）。带 Noul / Choice / Score helper，与官方 `typesafe-sdk` 不是同一个包。
- [LlamaIndex Jev](https://github.com/WiktorB2004/llama-index-jev) - 非官方 LlamaIndex 重排序（`JevRerank`）与路由（`JevSingleSelector` / `JevMultiSelector`），基于官方 Python SDK
- [Swift SDK](https://github.com/ainame/swift-typesafe) - 非官方 Swift 6.4 客户端，对齐 Python SDK 0.6.0 API，含 Linux
- [TypeSafe AI Swift SDK](https://github.com/alterhq/typesafe-sdk-swift) - 非官方零依赖 Swift 6 客户端，支持 Choice / Score / Noul、严格并发、可配置鉴权与重试，以及无网络测试
- [System One Foundation Models](https://github.com/peterfriese/system-one-foundation-models) - 非官方 Swift 6 桥接库，将 Apple 的 `@Generable` 类型映射为 Noul、Choice 和 Score，支持托管 Jev、HTTP Laya 和设备端 Core ML Laya，并提供置信度路由
- [discern](https://github.com/doeixd/discern) - 非官方 Effect 库：把 Choice / Noul / Score 答案变成带类型的模式匹配，`Uncertain` 是必须显式处理的分支，并支持可路由的 procedure；录制、回放、缓存与调用预算都做成 `DecisionModel` 中间件。不绑定供应商，通过 `@effect/ai-typesafe` 接入 Jev
- [kojev（Kotlin Multiplatform）](https://github.com/ItisNoMatter/kojev) - 社区客户端，支持 JVM、Android 和 iOS。Choice 与 Score 的答案直接回到你自己的 enum；只有一种带类型的读取方式，不设默认阈值。Maven Central：`io.github.itisnomatter:kojev:0.1.0`。
- [jev4k](https://github.com/pambrose/jev4k) - 非官方 JVM Kotlin 客户端：用 DSL 写 Choice、Score 和 Noul，答案以类型化的值读回，包括 enum。Maven Central：`com.pambrose:jev4k`
- [hunch](https://github.com/steven-shoemaker/hunch) - 非官方 Python 库（另有 TypeScript 版本），把 Choice / Score / Noul 变成作用于列表和 DataFrame 的函数（classify、score、check、where、extract、pick、rank、verify），支持请求去重、缓存，并可把不确定的行交给 LLM 在同一组标签中复核
- [JevT++](https://github.com/wiatrM/jevtpp) - 非官方 C++20 库，提供编译期枚举模式、类型化决策与弃权机制、本地 Laya 后端及可选的 TypeSafe System One HTTP 客户端；远程测试使用模拟响应和本地 HTTP 服务，尚未验证真实服务兼容性

## 应用

把决策模型放进真实循环里的开源产品与 demo。目前大多使用 Jev。

- [MemSearch](https://github.com/zilliztech/memsearch) - 面向编程 Agent 的 Markdown 记忆系统，提供可选的 Jev Noul 重排器与公开的中英文检索评测；属于社区集成，并非 TypeSafe 官方 SDK
- [Jev-Mem](https://github.com/libingzheren/Jev-Mem) - 非官方 Agent 记忆系统：Jev 或本地 Laya 负责记忆组织、查询路由、检索预算、候选评分与停止判断，LLM 负责生成答案；[论文](https://arxiv.org/abs/2609.23986)报告了作者在 LoCoMo 上的评测结果
- [Jev RAG](https://github.com/aifabrice/jev-rag) - 非官方本地优先知识检索应用：使用 SQLite BM25 或 Agent 规划的关键词检索召回候选，以 Jev `Noul` 判断重排证据，并公开可复现的 NFCorpus 评测；默认不需要向量数据库
- [Jev Deep Research](https://github.com/sunyasheng/JevDeepResearch) - 非官方实验性研究 Agent：Jev 通过 Choice 定位证据、Noul 判断证据是否存在，并行处理文档区域，再由 Pi-Serini 返回原文供 GPT 核查并继续研究
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) - [Browser Use](https://github.com/browser-use) 的浏览器 Agent。一次请求里由 Jev 选出操作和 DOM 元素；只有 `TYPE_TEXT` 才让小模型写字。Google Flights 苏黎世 → 伦敦约 7 秒。含库、本地 inspector 与测时。
- [Jev Social](https://github.com/socai-io/jev-social) - 浏览器实证社媒调研：Jev 选择受限的 Instagram、TikTok 与 LinkedIn 搜索/读取操作，socai 在用户 Chrome 中执行，报告仅引用捕获的帖子、评论与视频证据；非官方社区项目
- [Jev Web Analyzer](https://github.com/replynodes/jev-web-analyzer) - 社区项目：把公开 SaaS 落地页提取为干净 Markdown，再让 Jev 提出十个有界的 `Choice` 问题，判断首次访问者能理解什么，包括最先要改的地方。
- [jev-align (Sutro)](https://github.com/sutro-sh/jev-align) - 非官方主动学习 CLI：用 Jev 评估 CSV、Parquet 和 JSONL 数据，让人工标注不确定样本与审计样本，并用 GEPA 提议改进后的定义
- [JevSpan](https://github.com/lzq-0529/jev-span) - 非官方中英文零样本命名实体识别：代码按标点列出候选片段，由 Jev 的 `Choice` 问题提名、核验并确定每个实体的边界，每个实体都保留概率和完整的决策过程
- [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome) - Jev Ultrafast 的非官方 Chrome 扩展（Manifest V3）移植：Jev 一次请求同时选出操作和 DOM 元素，只有打字时才调用小文本模型，直接跑在用户自己的标签页里（OpenRouter / TypeSafe / Cloudflare 三种渠道）；附 17 个任务的 headless Chromium 测试套件和完整轨迹（仓库 docs/ 目录，同一套任务多轮 13–14/17）。
- [jev-ego](https://github.com/romaluev/jev-ego) - [ego lite](https://lite.ego.app/) 上的浏览器 Agent：一次 TypeSafe 请求选出操作和编号元素；面向 Agent 的 observe/act/suggest/step CLI
- [jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) - 非官方浏览器自动化：LLM 规划目标，Jev 在 Playwright 快照上决定每次点击/输入（约 300 ms/次）。提供库、CLI 与 MCP 服务（`npx -y -p jev-browser jev-browser-mcp`）。
- [Sedum](https://github.com/sedum-dev/sedum) - 非官方的开源 Playwright 端到端 AI 测试工具：目标模式下由 Jev 选出每一步操作及其目标，纯英文步骤用 Jev Choice 找到对应元素，验证断言是两个 Noul（holds、contradicted），点击、等待、判定和退出码均由确定性代码完成
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - macOS computer-use：OCR 屏幕，Jev 分类下一步动作再点击。约 $0.0002/步。
- [Yappy](https://yappy.biz/jev/) - macOS 语音 Agent（闭源，附公开测量数据）。在其托管方案上，Jev 每一步从窗口的无障碍控件表中选择操作与目标控件；只有输入文本时才调用聊天模型，置信度下降时交回完整 Agent。作者报告：每次决策 275–690 ms，五次共 $0.003。
- [Mobile Jev](https://github.com/droidrun/mobile-jev) - [Mobilerun](https://mobilerun.ai) 上的 Android Agent：每次点击由 Jev 决定。打开 Uber，旧金山机场 → 金门大桥，约 21 秒 / 9 步到支付页。含实时 studio、CLI 与 traces。不需要 ADB。
- [Unclutter](https://github.com/kitze/unclutter) - Chrome / Firefox 扩展：Jev 标出页面上不重要的元素，本地按页面模板记住并在下次访问时藏起来。
- [jevMail](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling) - 非官方开源 Gmail AI 垃圾邮件过滤、自动标签与收件箱整理工具：Jev 理解每封邮件的意图，应用自定义标签，并可自动归档高置信度的无用邮件
- [HA-Jev](https://github.com/AboveColin/HA-Jev) - 非官方 Home Assistant 集成：把关于实体状态的类型化提问变成传感器与自动化动作；可直接选取实体、设备或区域来构造 state，并附带用量、成本与每日 token 预算实体
- [Every](https://github.com/sufianetaouil/every) - 语义代码搜索 CLI：对每个函数问 yes/no，按 Noul 概率排序。
- [JevPDF](https://github.com/kylemclaren/jevpdf) - 非官方的 PDF 语义版 Ctrl+F：pdf.js 在浏览器中逐行提取文本，Jev 对每一行问一个 Noul（这一行是否回答了问题），命中的行按概率排序并高亮
- [DocJev](https://github.com/jerryjliu/docjev) - 文档分类与拆分：LiteParse 在本地提取页面文本，Jev 判断文档类别或一叠文件中各文档的边界，附基于 40 份真实政府文档的可视化报告
- [tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) - 从生产流水线开源的税务页面分类器：每页一次 Jev 请求，依据 JSON 表单描述在 261 种 IRS 表单和 7 种页面类型中选择，每页约 0.001 美元
- [blink](https://github.com/ellipsis-dev/blink) - 代码库搜索：一组 walker 并行走文件系统，由 Jev 判断哪个文件能回答自然语言查询
- [Jev Search](https://github.com/superagents-lab/jev-search) - 非官方网页搜索应用：用 Jev 的 Choice 和 Noul 判断选择来源、时间范围和候选查询词，再对 Search1API 返回的结果进行相关性排序
- [Jev Reranker (Rust CLI)](https://github.com/shinpr/jev-reranker) - 非官方 JSON 输入/输出 CLI：使用 Jev 的 `Noul` 判断重排搜索结果、过滤不含可用证据的文档，或提取与查询相关的原文片段
- [jevsearch](https://github.com/kylemclaren/jevsearch) - 非官方 shadcn/ui 站内搜索组件：首次按键即显示关键词结果，随后用一次 Jev 请求对前 20 条重排：每个页面一个 Noul，一个 Choice 选出最佳答案，再用一个 Noul 判断是否有页面能回答
- [jev-research-pipeline](https://github.com/shimo4228/jev-research-pipeline) - 非官方实验性研究监测流水线：Jev 按研究问题筛选论文等来源（Noul 门控 + Score 评分），阈值由代码判定，Qwen 为通过筛选的来源撰写按问题组织的 Obsidian 笔记
- [neo4jev](https://github.com/jexp/neo4jev) - Neo4j 图导航：每个节点上由 Jev 选择跟哪条关系走，并对 log 概率做 beam search
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) - 实验性 Hono 路由器：用自然语言描述路由，由 Jev 匹配进来的请求
- [sqlite3-jev](https://github.com/mattn/sqlite3-jev) - SQLite C 扩展：把 `jev_noul` / `jev_choice` / `jev_score` 做成 SQL 函数，只依赖 libcurl
- [jevql](https://github.com/kylemclaren/jevql) - 非官方类 psql 命令行工具与 Go/TS/Python SDK：无需扩展即可在原生 Postgres 中使用 `jev()` / `jev_prob` / `jev_choice` / `jev_score`，SQL 在服务端执行，剩余行由 Jev 批量判断，结果会缓存
- [pg-jev](https://github.com/realZachi/pg-jev) - PostgreSQL 扩展：`jev()`、`jev_prob`、`jev_choice`、`jev_score` 用自然语言条件筛选、排序和分类数据行，由 Jev 判断，无需 embedding 或向量列
- [jev-resilience](https://github.com/Vicente-MD/jev-resilience) - 非官方 Spring WebFlux starter：语义熔断器，用 Jev 抓 HTTP 200 里的静默失败
- [tripwire](https://github.com/noelzappy/tripwire) - 非官方 AI SDK middleware 与 OpenAI 兼容代理：约 100 ms 内对每条 LLM 回复做七项 Jev 检查，按置信度门控
- [ProgressGate](https://github.com/AshutoshVJTI/progressgate) - 检测 Agent 循环里的语义停滞：Jev 评判轨迹，代码返回 CONTINUE / WARN / REPLAN / HALT
- [jev-harness](https://github.com/AntonioCoppe/jev-harness) - 非官方生产层：策略、置信度门控、影子模式、配方和 eval CLI
- [jev-tree](https://github.com/reachjalil/jev-tree) - 在分类树上递归做 Choice，突破 Jev 单次最多 255 个选项的上限
- [jev-shell-history](https://github.com/mrnugget/jev-shell-history) - Fish 风格的 zsh 自动补全：输入时由 Jev 给近期历史排序
- [Supercov](https://github.com/supercorp-ai/supercov) - 面向编码 agent 的代码质量与测试覆盖率工具：Jev 给每个源文件打分，agent 就知道该先修哪里
- [jev-lint](https://github.com/ckorhonen/jev-lint) - 非官方 Claude Code 和 Codex 模糊代码检查工具，使用 Jev 在编辑时发现违反团队规则的代码，并支持可配置的规则包和仓库专属规则，让智能体能在代码审查前修正问题
- [Jev Review](https://github.com/devagrawal09/jev-review) - 分阶段代码审查工作流 + 本地 dashboard，由聚焦的 Jev 调用驱动。
- [Foreman](https://github.com/thruwire/foreman) - 软件工厂循环：Codex 写实现，Jev 独立判断是否做完、测试够不够、要不要人来看。
- [Jev Drone](https://github.com/RomanSlack/jev-drone) - MuJoCo 四旋翼：控制和安全留在代码里，Jev 做较慢的战术判断。
- [Jev Plays StarCraft](https://github.com/phyous/tsai-sc) - 原版星际争霸共享战役的结构化 state harness，带验证跑次和概率轨迹。
- [Jev × Civilization II](https://github.com/phyous/tsai-civ2) - 浏览器里跑原版文明 II；Jev 选帝国、城市、科研和单位动作。实验性，尚未验证通关
- [Jev Trade](https://github.com/aowang-ai/jev-trade) - Hyperliquid 实盘桌面：每个 tick 由 Jev 用 Choice 回答多空、开平或 hold、以及杠杆；下单和撤单由代码执行。默认 dry-run；配置私钥后会真下单。在线：[jev-trade.com](https://www.jev-trade.com/)。
- [Jev Trader](https://github.com/jarrodwatts/jev-trader) - 每个 Monad 区块对 Kuru 的 MON-USDC 下一笔买卖。在线 demo：[jev-trader.vercel.app](https://jev-trader.vercel.app/)。
- [Human Compiler](https://github.com/asfarsadewa/human-compiler) - 粘贴职场废话，Jev 打被动攻击 / 紧急感 / 信息密度，代码按 rustc 风格报诊断。在线：[human-compiler.asfarlab.fun](https://human-compiler.asfarlab.fun)。
- [Jev Wrapped](https://github.com/gaborishka/jev-wrapped) - Telegram 频道透视：Jev 逐条判断公开频道近一年最多 1,500 条帖子，用一个 `Choice` 从十种帖子类型中选一种，再用三个 `Noul` 判断是否为付费广告、标题党和情绪施压；代码把每月构成画成可分享的卡片，并附上得分最高的帖子链接。在线：[wrapped.ivanhabor.com](https://wrapped.ivanhabor.com)。
- [JEVMETER](https://github.com/ChetasLua/jevmeter) - 给任意视频挂上实时 Jev 仪表：逐句打分，导出 16:9 成片。演示：[Chetaslua](https://x.com/chetaslua/status/2100473581251748216)。
- [jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper) - 低延迟音频脏话检测：Jev 判定后 ffmpeg 在约 466 ms 内叠一声 beep，不改其余音轨。
- [jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm) - 仿真 Franka 上用英文目标做 zero-shot；Jev 把硬编码原语串起来。
- [Codex Jev Router](https://github.com/suenot/codex-jev-router) - Codex 子代理路由：Jev 用 Choice 和 Noul 选择模型与推理档位，代码检查置信度，不确定时回退到 Sol。
- [Jev Auto Router](https://github.com/miniLV/Jev-Auto-Router) - 非官方模型路由原型：用 Jev 为每次调用选择模型与推理档位，并通过本地 Responses 代理转发、独立验收任务
- [jev-router](https://github.com/gargpratyush/jev-router) - Claude Code 与 Codex 的每轮路由：简单活走快档，难活走强档。`npm i -g jev-router`。
- [jev-secret-detection](https://github.com/teyhouse/jev-secret-detection) - 用 Jev 扫 diff 里的密钥，结果可复现。
- [commit-miner](https://github.com/devanshbatham/commit-miner) - 用 Jev 给 commit diff 分类的 Rust CLI：修 bug、安全/CWE、变更类型。可出 HTML/CSV 报告。
- [jev-eval-agent](https://github.com/vinilana/jev-eval-agent) - 早期 Jev 测试的公开评测 harness。
- [Jev Logs](https://github.com/reachjalil/jevlogs) - OpenTelemetry 日志分流：先让 Jev 打诊断价值和优先级，再决定要不要花 LLM。
- [Smart home assistant demo](https://docs.typesafe.ai/demos/smart-home) - 官方互动 demo，演示 [speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)
- [jev.nvim](https://github.com/valentynkit/jev.nvim) - Neovim 插件：用 Treesitter 把缓冲区拆成函数，向每个函数提出一个自然语言问题让 Jev 打分，结果按概率排进 quickfix 列表。
- [jev-skip](https://github.com/valentynkit/jev-skip) - 浏览器扩展：读取 YouTube 字幕轨道，在片头结束前就把每段视频的赞助概率画到进度条上，不依赖众包数据库，据报告在 23 个视频上抓住了 SponsorBlock 77% 的赞助时长，每个视频约 0.0008 美元。
- [JevBystander](https://github.com/Nisaka520/JevBystander) - 安卓无障碍应用：读取微信当前可见的聊天文字，一次批量 Jev 请求（10 类意图 `Choice`、9 类情绪分布、0–3 着急程度 `Score`、11 类回复姿态 `Choice`）后只弹三条 Toast；不生成回复文案、不注入输入、不截屏也不做 OCR；本地联系人表把关系别名放进 state
- [Jev Chat Assistant](https://github.com/jev-chat/jev-chat-jarvis) - 非官方安卓聊天副驾：用无障碍服务读取 QQ、X、飞书当前可见的对话（飞书正文走本机离线 OCR），一次批量 Jev 请求问意图、对方需要什么、下一步动作 3 个 `Choice`，危险等级 `Score` 和 3 个 `Noul`；另一个聊天模型起草 3 条候选，再用一个 `Choice` 排序；代码只把选中的回复填进输入框，不代发
- [Paper Radar](https://github.com/Eliot5566/JEV-Paper-Radar) - 非官方每日 arXiv 和 bioRxiv 论文雷达：Jev 对每篇新论文按每条自然语言兴趣给出一个 `Noul` 判断，代码应用阈值，再由 GitHub Actions 发布网页和 RSS 订阅源。[公开运行页面](https://eliot5566.github.io/JEV-Paper-Radar/public/) 无需密钥即可查看

## Demo 与游戏

玩具、小站和实时 Agent。

- [Yes / No](https://yesno.coderai.dev) - 免登录 Noul demo。问一句，得到 yes / no / maybe，必要时联网检索。
- [TypeSafe AdBlock](https://github.com/realZachi/typesafe-adblock) - Chrome 扩展 demo：Jev 判断候选 DOM 元素并移除疑似广告，BYOK、无后端；每页消耗 API token，作者说明了漏删广告和误删元素的局限
- [Jev Tetris](https://jev-omega.vercel.app) - Jev 根据空洞、堆高、起伏选旋转和落点列。
- [Jev Pac-Man](https://jev-pacman.ephraimduncan.com) - 迷宫做成 JSON，每个路口由 Jev 选转向，实时玩。
- [Jev Chess](https://jevchess.com) - 全网对 Jev 的一盘共享棋；每个合法着法都是一个 Choice 问题，概率给棋子上色，实时校准面板为每一步打分。
- [Chess with Jev](https://chriswijnia.com/lab/chess) - 浏览器里的国际象棋与 Chess960：代码算出每个合法着法的事实，Jev 每回合以一次 Choice 选一步，候选着法画成箭头（[源码](https://github.com/cwdx/chess-with-jev)）。
- [typesafe-mario](https://github.com/fhshaik/typesafe-mario) - 从结构化模拟器状态玩超级马里奥。
- [jev-doom-agent](https://github.com/lukaske/jev-doom-agent) - 浏览器里的 Doom（Chocolate Doom WASM），空间状态 + 实时决策遥测。
- [jev-gomoku](https://github.com/mizchi/jev-gomoku) - MoonBit 客户端 + Jev 对打五子棋。文章：[jev 同士に五目並べで対戦させた](https://zenn.dev/mizchi/articles/jev-plays-gomoku)。
- [jev-t-rex-runner](https://github.com/joshlarsen/jev-t-rex-runner) - Chrome 小恐龙由 Jev 来跳。
- [snake-jev](https://github.com/siroccomask/snake-jev) - 贪吃蛇：每局几百次类型化转向决策。
- [Jev Guard](https://guard-jev.vercel.app) - 评论审核 playground。
- [jev-fit](https://jev-fit.com) - 粘贴一个软件想法；Jev 在一次调用中回答一套固定的类型化问题，页面给出结论：普通代码、Jev 或推理型 LLM，并附概率。非官方，闭源，页面和 API 免费。
- [Hollow Creek](https://hollow-creek-sigma.vercel.app) - 村庄 NPC 每个 tick *评判*你（做什么、对你什么感觉），而不是聊天。
- [Jev mood demo](https://jev-demo.vercel.app) - 长时间对它好或坏，结构化 state 跟踪心情。
- [Jev Room](https://jev-room.moe136231.chatgpt.site) - 一句话 → 六个房间设定。Jev 选，应用渲染。
- [1 Million Emojis](https://chriswijnia.com/lab/emoji) - 一块人人实时共享的 1000 × 1000 emoji 画布；每一笔之后，Jev 用一次 Choice 选定旁边的一格及其 emoji（[源码](https://github.com/cwdx/1-million-emojis)）。
- [Jevvie](https://chriswijnia.com/lab/jevvie) - 页面小助手：页面把操作暴露为 WebMCP 工具，一次 Jev `Choice` 判定访客请求对应哪个操作（参数也各用一次 `Choice`），前两名接近时会再问一句；体素角色再跳到按钮上执行（[源码](https://github.com/cwdx/jevvie)）。
- [TypeSafe Typewriter](https://typesafe-demo.val.run/) - Val Town 在线 demo：打字时 16 条类型化判断实时更新。发布帖：[Steve Krouse](https://x.com/stevekrouse/status/2100287368221659289)。
- [jev-got](https://github.com/phureewat29/jev-got) - 权力的游戏角色扮演：你是琼恩·雪诺。故事模型写下一场，Jev 回答他在哪、有多危险、该配什么音乐。
- [Little Airways](https://github.com/lbotinelly/jev-little-airways) - 玩具群岛空管：每架飞机只看见自己附近，Jev 判断备降 / 紧急 / 谁先落地，约 150 ms。
- [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) - 基于 PyBoy 的精灵宝可梦红版：路线和数值运算都由代码掌控，Jev 只在分支点做选择，每回合战斗都会记录一次用 Brier 分数对照 RAM 状态检验的濒死预测。
- [Jev Plays Pokémon Red](https://github.com/christianmat/jev-pokemon) - 程序读取 Game Boy 内存并列出合法选项，每一步都由 Jev 选择；用时 37 小时 40 分、16,150 次决策、约 1.65 美元通关
- [jev-canvas](https://github.com/gaborishka/jev-canvas) - 用语音和摄像头追踪的手指在 tldraw 画布上绘图；Jev 在每段实时转写上决定动作、目标和位置。支持英语和乌克兰语指令。
- [Jevtown](https://github.com/gaborishka/jevtown) - 由 10,000 个计算生成的人物组成的小镇，阅读你的帖子、分类广告、产品或标题。Jev 判断文本适合哪些人，选出最先的 600 位读者，并为每个人物回答一个 `Choice` 给出反应；只有高兴的读者比反感的读者至少多出这一波人数的十分之一，代码才把文本送往下一波。在线：[jevtown.ivanhabor.com](https://jevtown.ivanhabor.com)。
- [sudoku-vs-jev](https://github.com/zebedelu/sudoku-vs-jev) - 终端数独：Python 掌握规则，Jev 每回合选择一步，在存在必走步时表现稳健，一旦需要猜测则表现不稳。
- [chess-vs-jev](https://github.com/zebedelu/chess-vs-jev) - Pygame 国际象棋：python-chess 掌握规则，Jev 每回合选择一个合法走法，支持人 vs 人、人 vs Jev 和 Jev vs Jev。
- [JevsBistro](https://github.com/andrewsilber/JevsBistro) - 确定性的 3D 餐厅模拟：重放同一场晚餐服务，对比规则驱动、摄像头辅助和由 Jev 规划的服务员，并记录每次决策的状态、选项、置信度和延迟。
- [jev-asks-until-sure](https://github.com/mintannn/jev-asks-until-sure) - 用置信度决定还要问几题的二十问游戏：Jev 会断言、含糊其辞，或者干脆拒绝作答，界面同步播报每一次判定。在线：[jev.mintan.org](https://jev.mintan.org)。
- [Jev × 2048](https://jev-2048-ultra.vercel.app) - 一个把 Jev 当作 2048 决策引擎的网页实验台，展示每一步的概率分布、置信度、延迟与 token 消耗，观察上下文设计如何影响决策模型。
- [Book Aurora](https://github.com/dani1005/book-aurora) - 让 Jev 几十秒读完一整本小说：每段文字一次调用返回九种情绪打分和强度，每段变成一行羽化的色带，整本书就是一幅极光。《弗兰肯斯坦》601 段、6010 次类型化判断，约 25 秒、3 美分，可导出海报。
- [FlightBench](https://github.com/AlperKartkaya/FlightBench) - 固定翼飞机着陆模拟器与基准测试，可与 Jev 比拼飞机着陆，将 Jev 的四个 `Choice` 决策映射为 JSBSim 中的飞机控制输入，并与人类飞行员、基线及 LLM 控制器的着陆表现进行对比

## Agent 工具

把决策模型接到编程 Agent 与 MCP 客户端上的工具。

- [TypeSafe agent skill](https://github.com/typesafe-ai/skills) - 官方技能包：原语、模式、如何组织 evaluation。Claude Code：`claude plugin marketplace add typesafe-ai/skills`，再 `claude plugin install typesafe@typesafe-ai`。其他 Agent：`npx skills add typesafe-ai/skills --skill typesafe-ai`。
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Claude Code 插件 + npm 库：用 Jev 给工具调用打分并丢掉过时的，而不是把上下文摘要掉
- [SkillRanker](https://github.com/Dicklesworthstone/skillranker) - Rust CLI：根据当前会话上下文，让 Jev 给下一步该用哪个 agent skill 排序，带 Claude Code hook
- [langchain-skill-router](https://github.com/deyna256/langchain-skill-router) - LangChain deepagents 中间件，按轮路由 skill：Jev 从数百个 SKILL.md skill 中排序并核验本轮需要哪些，排序会拆分以适应 Jev 的调用上限，出错时回退到完整目录。判定器可替换。`pip install "langchain-skill-router[jev]"`。
- [JevRouter](https://github.com/BillionsBobby/JevRouter) - 非官方路由器：模型、子 agent、skill、MCP 工具和 CLI 放进同一个候选集，Jev 做一次 Choice，代码负责可用性、权限、风险和确认。10 个 Toolathlon 任务上，Jev 的位置命中率是 38–44%，DeepSeek V4.1 Flash 是 24%
- [JevLoop](https://github.com/zjunlp/JevLoop) - 非官方 Agent 循环：每个分叉（选工具、风险、是否做完）交给 Jev 1.13.0，写字仍留给 LLM；没有 key 时退到本地 Laya，再退到规则。`npm run demo` 可以离线跑
- [Jevbridge](https://github.com/tacticocc/Jevbridge) - 非官方 ACP/MCP 适配器：把 Jev 的类型化判断和 computer use 接到 Codex、Claude、Grok、OpenCode 旁边
- [eve](https://github.com/vercel/eve) - Vercel 的 Agent 框架。实验性 `autoModel` 默认用 Gateway 上的 `typesafe-ai/jev`，从白名单里挑语言模型。
- [jev-mcp](https://github.com/jkudish/jev-mcp) - Node MCP，封装三条 cookbook：`jev_verify`（引文核验）、`jev_screen`（注入/护栏）、`jev_find`（无需 embedding 的语义排序）。`npx -y github:jkudish/jev-mcp`。
- [Jev MCP（Python）](https://github.com/blakestone-x/jev-mcp) - Python MCP：classify、score、check、match、screen。
- [Jev Review MCP](https://github.com/NiazMorshed2007/jev-review) - 本地优先的 MCP：Claude Code、Codex、Cursor、OpenCode 边写边拿 Jev 的结构化质量审查。与上面应用里的 [Jev Review](#应用) 不是同一个项目。
- [System One Connector](https://github.com/itsmostafa/system-one-connector) - Go CLI + 单二进制 MCP（原名 typesafe-mcp），让 Claude Code、Claude Desktop、Codex、Hermes 和 pi 调用 Jev、d1、CLM 或 Laya 做类型化决策。
- [pi-typesafe](https://github.com/DevMortimer/pi-typesafe) - Pi 扩展：一份经同意的、密钥托管的 TypeSafe 客户端，批量 `typesafe_evaluate`，可离线测传输。
- [pi-jev](https://github.com/y0usaf/pi-jev) - Pi 扩展：影子模式工具调用门控、输出评判、类型化 `jev_ask`。
- [pi-warden](https://github.com/DevMortimer/pi-warden) - 基于 pi-typesafe 的 Pi 护栏：把判决当成 held tool result 而不是对话框；对照项目规则文件检查写入。
- [pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode) - Pi 自动模式：Jev 按语义批准 `bash` / `write` / `edit`，判断不了就拒绝。
- [Bicameral](https://github.com/AbdelStark/bicameral) - Pi 编程 harness：LLM 写代码，Jev 提供策略、循环检测和 review 的类型化反射。明确不是沙箱。
- [jev-pref](https://github.com/doeixd/jev-pref) - 把 AGENTS.md 里的偏好变成 Jev 驱动的 AI linter：在 `jev-pref.json` 定义项目语义审查规则，对 diff hunk、暂存文件或 PR 求值，并把结果反馈给编程 Agent。`npx jev-pref setup`。
- [hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) - Hermes（也覆盖 Claude Code 和 Codex）的一组技能：模型路由、技能选择、检索、记忆和压缩交给 Jev。路由大约 0.4 秒，在 377 个技能里挑选大约 2.8 秒。交接摘要的实测召回不如原文，所以交接默认仍保留完整对话
- [jev-system-architect](https://github.com/samtay32/jev-system-architect) - 专门找脆弱语义逻辑、改写成 Choice / Score / Noul 边界的 skill。
- [augustus](https://github.com/24601/Augustus) - 非官方的 augustus 和 augustus-train 智能体技能，面向特定应用的决策模型，涵盖原语、基础模型与方法选择、数据组装、拟合、导出与重新加载、有界改进及独立评估；默认以 TypeSafe Jev 为托管模型示例
- [jev-axi](https://github.com/shiftynick/jev-axi) - CLI 加 Claude Code、Codex hook：命令执行前先用 Jev 给危险性打分，并筛查抓取到的文本是否含提示注入，常规命令在本地判定、不发送任何内容
- [jev-engineering](https://github.com/eugeniughelbur/jev-engineering) - 编程 Agent 的决策层：先走确定性规则再发一次 Jev 请求，可作为 Claude Code hook、MCP 服务、本地回环服务，并带共享团队策略。附带支撑其数字的 300 次注入测试。
- [toolgate](https://github.com/RiskAverseTech/toolgate) - 非官方：面向 Claude Code 钩子与 MCP 服务器的工具调用防火墙，由 Jev 回答七个风险问题，确定性代码将其映射为 allow/ask/deny，默认失败即拦截，并跟踪同一会话中先写入后执行的文件
- [Jevonian](https://github.com/xinyao27/jevonian) - 本地 OpenAI / Anthropic / Responses 兼容代理：`jevonian/auto` 用一次 Jev 请求同时决定走哪个模型和用多深的思考，状态来自会话（近期消息与工具结果、连续报错次数、上下文余量、配额、候选能力、切换模型的缓存代价）；候选筛选和全部阈值由确定性代码负责，指定具体模型或显式 `jevonian/<route>` 时完全不调用 Jev，每次决策都会记录实际服务的模型、理由、真实 token 用量和估算成本。
- [jev-opus](https://github.com/WXK-AI/jev-opus) - 非官方 CLI 和 Claude Code 网关：在 Opus 5.5 上运行 Claude Code，每次收到提示词和每批工具调用之后，用 Jev 的 Choice / Score / Noul 类型化问题决定下一次调用的推理强度（effort），由代码负责上下限，并以逐条消息的 effort 声明发送，因此不会破坏提示缓存
- [jev-belay](https://github.com/valentynkit/jev-belay) - Claude Code 的 Stop 钩子：先从对话记录里找证据，只有在文件改动且之后没有通过检查时才发起一次四问的 Jev 调用来核实"完成"，任何出错都放行。
- [jev-commit](https://github.com/valentynkit/jev-commit) - Git 预提交钩子：用一次 Jev 调用判断提交信息是否匹配暂存的改动，并检查调试残留、未提及的改动和凭据泄露，只有检测到凭据才会阻止提交。
- [jev-use](https://github.com/shitianfang/jev-use) - Claude Code、Codex 和 pi 插件：把 Agent 循环里不需要输出文本的判断批量交给 Jev，需要写字或置信度不足的步骤按类型化契约退回 LLM
- [dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools) - DeepSeek Harness 插件：用 Jev 精简超长工具输出、筛查抓取页面里的注入指令、挑选下一步该用的 skill，并提供 jev_ask 与 jev_gate 两个工具
- [slop-grader](https://github.com/lukstei/slop-grader) - 基于规则的命令行与 Agent skill：按自定义规则集（custom rulesets）用 Jev 评分和行级标志检查文本的 AI 废话、语法和技术文档质量，并引导 AI Agent 自动修复违规
- [pytest-jev](https://github.com/allebee/pytest-jev) - pytest 插件，为 LLM 输出做语义断言：关于回复的每条自然语言断言都作为 Jev Noul 问题在一次请求中提出，p ≥ 0.8 才算通过，失败时列出每条断言的概率；`choice` 和 `score` 用于路由和评分检查
- [jgrep (kyu1204)](https://github.com/kyu1204/jgrep) - 面向代码、git diff 和 CSV 行的语义 grep：每个 5-60 行代码块一个 Noul，每次 Jev 请求打包 16 个块，输出 grep 风格的 file:line 和退出码，可在 CI 中用英文句子做规则检查
- [jevgrep (allebee)](https://github.com/allebee/jevgrep) - 面向日志的流式语义 grep：对每一行向 Jev 提出一个 Noul 问题（用自然语言描述条件），打印概率不低于阈值的行，也可接在 `tail -f` 后使用
- [jevgrep (dzhng)](https://github.com/dzhng/jevgrep) - 面向编码 Agent 的代码搜索 CLI 与 skill：Jev 在目录、文件和声明层级判断相关性，`jg` 返回相关文件、阅读线索和原文片段。作者在 10 个 SWE-bench 任务上的对比中，它与基线同样完成 8 个，成本约低 30%。
- [wellposed](https://github.com/suraj-phanindra/wellposed) - 面向 Jev 请求的离线 linter 与 agent skill：40 条结构检查完全不调用模型（缺少「以上都不是」选项、state 路径失效、criteria 形状错误），再用 Jev 自身检查结构无法判定的部分，并附带为两层分别打分的标注语料。
- [jev-auto-approve](https://github.com/BasmaAbouzied0/jev-auto-approve) - Claude Code PreToolUse hook：每条 Bash 命令向 Jev 提一个 Noul，判断是否严格只读；p ≥ 0.95 自动批准，否则回退到正常的权限确认，从不拒绝。本地黑名单和注入过滤让高风险命令不会发给 Jev；公开校准中 8 条会改变状态的命令无一被批准
- [jev-secret-guard](https://github.com/BasmaAbouzied0/jev-secret-guard) - 阻止 Agent 写入或发送密钥的 Claude Code PreToolUse hook：已知格式的密钥在本地直接拦截，未知的高熵字符串只以脱敏形式作为 Noul 发给 Jev，检查过程本身不会泄露密钥；p ≥ 0.80 拦截，0.30 到 0.80 或 Jev 出错时交给人确认。公开校准中 6 个密钥全部拦截，6 个无害字符串无一被拦截

## 评测与排行榜

先列排行榜，再列单项评测和评测工具。目前大多数评测针对的是 Jev。

### 排行榜

- [Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index) - Hugging Face Space 排行榜：用版本化 benchmark 套件对比 Jev 与开源决策模型，含校准指标和评测方法；开源模型推理耗时与 Jev 托管 HTTPS API 的延迟不可直接比较
- [JevBench](https://github.com/fstandhartinger/jevbench) - MIT 协议的评测框架与排行榜：534 道英文决策题，分公开题和封存题，同时报告准确率、延迟和价格。讨论：[Show HN](https://news.ycombinator.com/item?id=49800574)。
- [Jevals.com](https://jevals.com/) - 独立评测：托管 Jev 与六个 LLM 回答同样的 Noul、Choice、Score 问题，按人工标签打分（PubMedQA、Banking77、HelpSteer2），每次决策的日志公开
- [LangWatch Jev benchmark](https://langwatch.ai/compare/jev-benchmark) - 在 15 个决策任务上对比 Jev 与 7 个 1B 以下开源模型，附 95% 区间、延迟和数据污染检查

### 单项评测

- [typesafe-ai-benchmark](https://github.com/iammrduncan/inference-benchmarks) - 同一套 System One 问题，对比 Jev 与 Cerebras 上的 Qwen 3.8 27B。视频：[Shannon](https://x.com/iamMrDuncan/status/2100467548298899918)。
- [Jev Rerank Bench](https://github.com/anessbelbati/jev-rerank-bench) - 重排序对比：原始 provider 响应、打分代码、不确定区间、写明的局限。
- [Jev Spam Eval](https://github.com/bitnovus/jev-spam-eval) - 探索性零样本垃圾邮件研究，对照训练过的 TF-IDF 基线，并写了事后调参的 caveat。
- [Jev × NASA Kepler](https://gist.github.com/ipaulsmith/e5c3ae3a492a455435d5bfc161404312) - 对 8,054 个历史 Kepler 关注目标（Kepler Objects of Interest）进行的独立回顾性 Jev 1.13 测试；预测期间隐藏 NASA 系外行星档案库分类，档案分类匹配率为 72.5%，固定三规则基线为 64.4%，并公开了完整请求、指标、基线和局限说明
- [Jev Phishing Bench](https://github.com/anisselbd/jev-phishing-bench) - 2000 封邮件：Jev 对 Claude Haiku 4.5 做点不点链接，带校准、延迟和成本。这里准确率是 Haiku 更高。
- [jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark) - Who&When Pro（注入的 Agent 故障）：Jev 对强 LLM，预测是谁 / 哪一步 / 哪类错误。
- [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) - 公开语料上的盲测：提示注入和漏洞代码检测，基于 jev-go。
- [ASSAY-001](https://github.com/jourdanlabs/assay-001) - 独立预注册核验：Banking77 / CLINC150 上测 Jev 校准与类型安全。结论分裂，日志全公开。文章：[donttrustme.ai](https://donttrustme.ai/assay-001.html)
- [Jev search rerank eval](https://github.com/zhuyansen/jev-search-rerank-eval) - 9831 对标注：Jev rerank 对照 BM25 / bge-m3，并量化评委循环偏差。融合最好；Jev 单独打不过 embedding
- [吸烟史抽取评测](https://github.com/vclic/smoking-extraction-benchmark) - 1000 条合成病历：Jev 对 OpenAI structured outputs，比准确率、成本和延迟
- [jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench) - 用 2976 次经 OpenRouter 的请求比较一次批量提问和拆开提问：每次请求大约有 261 个固定输入 token，费用与公布的 token 单价一致，答案差异和重复请求的噪声相当

### 评测工具

- [System One Playground](https://github.com/goodboybeau/system-one-playground) - 本地 Apple Silicon 决策模型工作台，可并排比较 Laya、Decider、Kev、Jev 等引擎，附公开数据集上的准确率与校准评测、输入截断诊断，以及延迟、内存和负载测试
- [Jev DSPy Lab](https://github.com/jmanhype/jev-dspy-lab) - 非官方 DSPy 配套评测：录制并重放 TypeSafe 调用，测量校准、选择性风险、置信度弃权、延迟、token 和建模成本。
- [jevcal](https://github.com/abhixhek/jevcal) - 非官方命令行工具：用你自己的标注数据按目标准确率为每个问题拟合置信度阈值，在留出集上验证，给出仍需回退到 LLM 的流量比例，并在 Jev 更新导致已锁定阈值失效时让 CI 失败
- [jevals](https://github.com/openlayer-ai/jevals) - Openlayer 把 Agent 评测和护栏写成决策模型问题：一条 trace 的工具选择、依据性、相关性和注入检查在一次请求中完成，可用 Jev，也可在本地用 Kev、Laya 或 Eikos。`pip install jevals`。

## 论文

- [Typed Decision Models: An Early Evidence Audit and Evaluation Checklist](https://arxiv.org/abs/2609.32160) - 综述 Jev 发布后头几天的 28 篇论文：类型化读出相比同类标签概率读出没有显示出独立的准确率优势，最明确的收益是延迟和成本；并据此给出 14 条评测检查清单
- [Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](https://arxiv.org/abs/2609.30216) - 首个 Jev 应用生态综述与分析：覆盖 2,170 个公开 GitHub 项目，记录早期快速增长、应用领域与决策用途分布
- [Evaluating and Benchmarking the System One Model Jev](https://arxiv.org/abs/2609.37647) - 在 37 个数据集上零样本评测 Jev 1.13（346,009 次请求，花费不到 10 美元），对照 Qwen3.8-27B 和 Gemma-4-E4B 的选项概率：Jev 在 27/37 个数据集上胜过 Qwen，37 个全部胜过 Gemma；Choice 概率校准良好，但二元概率相对 0.5 阈值的位置偏差较大。代码和原始响应已公开。
- [Beyond Calibration: Do a Typed-Decision Model's Probabilities Obey the Probability Axioms?](https://arxiv.org/abs/2609.33209) - 无需标签的一致性检验：Jev 对「是 X」与「不是 X」的概率之和平均偏离 1 达 0.064，Qwen3.8-27B 首 token 读出为 0.293；Jev 三个单标签概率之和平均为 1.14
- [Evaluating System One Models for Agent Security Decisions](https://arxiv.org/abs/2609.33401) - 在提示注入和风险筛查上，把 Jev、Laya、Decider、Nimble 与专用分类器和 LLM 评委对比：整体校准良好，也可能掩盖集中在特定攻击类别上的高置信错误
- [JevAdvBench](https://arxiv.org/abs/2609.31142) - 第一个面向决策模型的对抗 benchmark：812 道类型化问题、9,744 个单点修改攻击。在 Jev 1.13 上，往状态里追加一句未经核实的观点就能翻转 12.1% 的决策，因此状态应被视为不可信输入。
- [From Text Decisions to Pixels](https://arxiv.org/abs/2609.29283) - PixelJev：基于小型开源多模态模型的原生图像决策接口；64-shot 适配把 Pets 准确率从 60.13% 提升到 92.40%，但校准并不随准确率一起提升
- [Chinese-Jev](https://arxiv.org/abs/2609.36965) - 面向中文的 encoder-only System One 模型：在 1000 万条样本上预训练，再分别针对医疗、法律、金融微调，并发布 CJ-Bench；作者报告通用领域准确率高于 Jev，速度快 20 倍
- [Calibrated Decision Models for Autonomous Penetration-Testing Harnesses](https://arxiv.org/abs/2609.28940) - 探讨 Jev 与 Laya 在 LLM 渗透测试 Agent 中的位置：漏洞判定、严重度校正、Agent 剪枝和确认循环，并附一个探索性案例

## 文章

独立实测与实验。

- [Jev 搜索场景：三项实测](https://zc277584121.github.io/rag/2026/09/22/jev-search-deep-evaluation.html) - 停搜、记忆重排与多跳关系筛选的独立实测，附实现链接，并说明私有数据、样本数差异与速度动画为模拟等限制
- [Mini-Vibe Check: TypeSafe's Jev Judged Everything I’ve Written in 0.7 Seconds](https://every.to/vibe-check/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) - Every 的 Mike Taylor 用 Jev 扫过自己的写作语料。
- [TypeSafeのJevを正しく驚く、それってLLMでできませんか？](https://zenn.dev/nwn/articles/824026c76116e0) - 用 Gemma 的 logit 并行复现 JSON 捷径，并在公开 Mario harness 上对比 Jev 与 LLM。
- [Jev: one judge call, or twelve dimension scores? I measured both on three tasks](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/) - 独立实测：三个分类任务上，每行一次直接提问 vs 12–14 个 Jev 维度加本地拟合权重，附 token 成本、置信区间与误报率。
- [Testing Jev on public and private data: classifier or filter?](https://amankumar.ai/blogs/jev-measured) - 16000 次调用对照 gpt-5.4-mini 与 gpt-5.6-luna：哪里赢、哪里崩、阈值怎么定
- [Is Jev as Accurate as Frontier Models at Classification?](https://openrouter.ai/blog/insights/jev-vs-claude-opus-5-classification/) - OpenRouter 用全部 3080 条 Banking77 测试集对比 Jev 1.13 与 Claude Opus 5：准确率 81.0% 对 84.4%，中位延迟 175 ms 对 2266 ms，每千次约 $0.11 对 $2.42
- [We Tested Jev on 791 Labeled Decisions Against Four LLMs](https://www.ayautomate.com/blog/jev-vs-llm-benchmark) - 独立评测，经 OpenRouter 跑 8 类和 77 类 Banking77 路由以及提示注入检测：Jev 与中小模型接近，77 类路由上落后 GPT-5.6 Terra 约 5 个点；置信度不低于 0.80 才采用、其余交给 Terra 时，准确率与 Terra 单独跑对齐，成本大约是其四分之一
- [Jev × LexGLUE](https://github.com/chepyle/jev-test) - 可复现的零样本评测：Jev 1.13（`typesafe/jev-1.13-20260917`）跑完全部七个 LexGLUE 任务、23607 条测试样本，平均 micro-F1 69.9、花费 $4.02；对照 GPT-5.6 Luna 的对话 JSON 为 71.3、$16.45
- [Jev Does Not Play Dice: 83% probability, 19% accuracy on a hidden fair die roll](https://kantahayashiai.github.io/posts/jev-does-not-play-dice/) - 独立校准实测：用真实概率已知的公平骰子、硬币和转盘，以及合成预测文档测试 Jev；在 400 次隐藏六面骰实验中，Jev 每次都选择 1，平均报告概率为 82.9%，实际命中率为 19.0%。代码和原始响应见 [GitHub](https://github.com/KantaHayashiAI/jev-does-not-play-dice)。

社区实践教程。

- [Milvus Search with Jev](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) - 9 篇可运行的社区 Notebook，结合 Gemini 嵌入、Milvus 检索与 Jev 判断，覆盖重排、过滤、停搜、路由、缓存复用、数据筛选、护栏和评估

## 相关

- [awesome-jev-prompts](https://github.com/vicfei/awesome-jev-prompts) - 43 个经过实践检验的 Jev 问题设计模式（Choice/Score/Noul），含模板、阈值与失败模式，另有 10 条反模式。CC0，双语 EN/中文。
- [MrJev/awesome-jev](https://github.com/MrJev/awesome-jev) - 另一份更严的列表（10 星门槛），[mrjev.com](https://mrjev.com/best-jev-tools/) 上有动手评测，记录每个工具发了什么、发到哪。
- [Awesome TypeSafe Jev](https://github.com/AbdelStark/awesome-typesafe-jev) - 非官方、附源码链接的 Jev 入门与项目目录，包含类型化判断示例、社区项目卡片、独立评测链接及新贡献者入口
- [laya.tools](https://laya.tools) - 非官方目录：收录约 950 个基于开源 Laya 模型的项目，来自 GitHub、npm、Hugging Face 和 X，可按平台和用途浏览，并附 Laya 与 Jev 对比。与 TypeSafe 和 ConvAI 无隶属关系
- [AgentPlugins JEV 目录](https://agentplugins-2v1.pages.dev/jev-plugins/) - 跨生态 JEV 插件与工具目录：收录 browser-use/jev-ultrafast、Laya、Kev、fast-jev-compaction 等，按 GitHub 星标排序，附[实用 JEV 教程](https://agentplugins-2v1.pages.dev/typesafe/)与 [Laya / Jev / Kev 对比](https://agentplugins-2v1.pages.dev/laya-vs-jev/)。与 TypeSafe 无隶属关系

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。简而言之：开一个 PR，加上项目链接和一句话简介。项目应当有用、有趣，并且基于或围绕决策模型。

## 许可证

[CC0 1.0](LICENSE) — 本列表贡献到公有领域。
