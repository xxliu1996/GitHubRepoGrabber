# GitHub 周报：LLM / Agent（2026-08-30 – 2026-09-06）

本周的热门项目呈现出一个清晰的信号：Agent 生态正在从"能干活"转向"干活要可控、可信、可省钱"。NVIDIA 出手做技能安全扫描,腾讯云和腾讯分别补上沙箱隔离与企业级知识库治理,多家团队在做模型路由和 token 省钱,连教育场景也开始用多智能体重构。狂热堆功能的阶段正在过去,基础设施和治理层成了新的竞争焦点。

---

## 1. [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)

> Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them.

- ⭐ 本周 +1081 ｜ 总计 16400 ｜ Python ｜ Apache-2.0
- 主页：https://docs.nvidia.com/skills/scanning-agent-skills

一款专门扫描 AI Agent 技能（Claude Code、Codex CLI、MCP 技能包）的安全检测工具，用正则/AST/YARA 静态分析加可选 LLM 语义分析，给出风险评分和"可安装/谨慎/禁止安装"结论。主要面向在安装第三方 Agent 技能前做安全把关的开发者和企业 CI/CD 流程。相比传统代码审计工具，它专注"Agent 技能"这一新型攻击面（提示注入、供应链投毒、越权代理等 71 种漏洞模式），并支持命令行/Docker/MCP 服务器多种接入方式。

---

## 2. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

> Chrome DevTools for coding agents

- ⭐ 本周 +958 ｜ 总计 51154 ｜ TypeScript ｜ Apache-2.0
- 主页：https://developer.chrome.com/docs/devtools/agents

Chrome 官方出品的 MCP 服务器，让 AI 编码助手（Claude、Cursor、Copilot 等）能直接操控和检查一个真实运行的 Chrome 浏览器，做页面自动化、网络/控制台调试和性能追踪分析。面向需要给 Agent 加"浏览器眼睛和手"的开发者，尤其是前端调试、性能优化场景。相比一般的浏览器自动化 MCP，它直接复用 Chrome DevTools 前端能力（源码映射堆栈跟踪、CrUX 真实用户体验数据），调试深度更接近人类工程师，并提供完整版和轻量 `--slim` 版两种模式。

---

## 3. [Tencent/WeKnora](https://github.com/Tencent/WeKnora)

> Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.

- ⭐ 本周 +545 ｜ 总计 21545 ｜ Go ｜ NOASSERTION
- 主页：https://weknora.weixin.qq.com

腾讯出品的开源 LLM 知识库框架，把传统 RAG 问答、ReAct 智能体多步任务编排（检索+MCP 工具+技能沙盒+联网搜索）、以及"文档自动蒸馏成可维护 Wiki 知识图谱"三种能力整合在一起。主打本地/私有云部署、数据完全自主可控的企业用户，内置多租户 RBAC、审计日志等治理能力。相比常见 RAG 项目，差异化在于知识图谱可交互可视化、支持类 Wiki 协作（版本控制、逐行 diff 回滚），以及十余种数据源增量同步。

---

## 4. [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)

> Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

- ⭐ 本周 +435 ｜ 总计 11814 ｜ Go ｜ NOASSERTION
- 主页：https://cubesandbox.com

CubeSandbox 是一个基于 RustVMM 和 KVM 构建的高性能安全沙箱服务，专为 AI Agent 提供硬件级隔离的运行环境，60ms 内即可创建沙箱，内存开销低于 5MB。主要面向需要大规模、高并发运行 AI Agent 代码执行任务的开发者和企业，兼容 E2B SDK 便于迁移；相比同类沙箱方案，新意在于"轻量启动+硬件级隔离"的组合，并支持跨节点暂停/恢复、K8s 部署等企业级运维能力。

---

## 5. [mlc-ai/web-llm](https://github.com/mlc-ai/web-llm)

> High-performance In-browser LLM Inference Engine

- ⭐ 本周 +392 ｜ 总计 19004 ｜ TypeScript ｜ Apache-2.0
- 主页：https://webllm.mlc.ai

WebLLM 是一款可直接在浏览器内运行的高性能 LLM 推理引擎，借助 WebGPU 实现硬件加速，无需任何服务器支持。它面向希望在网页或浏览器插件中构建隐私友好型 AI 助手的前端开发者，支持 Llama、Phi、Gemma、Mistral、Qwen 等多种主流模型；差异化亮点在于完全兼容 OpenAI API（支持流式输出、JSON 模式等），让开发者用熟悉的接口在本地浏览器里跑开源模型。

---

## 6. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

> Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 190,000+ scientists worldwide.

- ⭐ 本周 +5491 ｜ 总计 43268 ｜ Python ｜ MIT
- 主页：https://arxiv.org/abs/2609.00065

该项目是一套包含 163 个即用型科学研究技能的开源集合，覆盖癌症基因组学、药物-靶点结合、分子动力学、时间序列预测等生物、化学、医学等多领域工作流，遵循开放的 Agent Skills 标准。它面向使用 Cursor、Claude Code、Codex、Google Antigravity 等 AI Agent 工具的科研人员和工程师。相比通用型 Agent 技能库，新意在于专注科学领域的"程序性知识"沉淀（并配有论文佐证），同时以 Agent Plugins 包形式打包，可一键整体加载。

---

## 7. [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)

> 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper.

- ⭐ 本周 +1689 ｜ 总计 81815 ｜ Python ｜ Apache-2.0
- 主页：https://crawl4ai.com

Crawl4AI 是一个开源网页爬虫/抓取工具，专门把网页内容转成干净、结构化的 LLM 友好 Markdown，服务于 RAG 系统、Agent 数据管道和结构化信息抽取等场景。目标用户是需要为大模型批量准备网页语料的开发者和数据团队。相比同类爬虫，它强调异步浏览器池、自适应爬取（学习站点结构、按需探索）、以及"零密钥、CLI+Docker 随处部署"，并持续加固 Docker API 安全性。目前是 GitHub 星标最多的爬虫项目，并推出了云端 API 内测。

---

## 8. [weave-os/router](https://github.com/weave-os/router)

> Model router for agentic systems. Routes every prompt to the right model in <50ms. Cut costs 40-70% with just an endpoint change.

- ⭐ 本周 +1378 ｜ 总计 4011 ｜ Go ｜ NOASSERTION
- 主页：https://weaveos.com/products/router

Weave Router 是一个面向 Anthropic、OpenAI、Gemini 等多家模型 API 的"透明代理/路由层"，可直接接入 Claude Code、Codex、Cursor 等编码助手或自研应用，按每次请求自动挑选最合适的模型。它面向需要在多模型间做成本/效果优化的团队，密钥默认本地保存（BYOK），并内置 OTLP 可观测性。与常见"多模型网关"不同，它用一个基于 Avengers-Pro 论文思路的小型本地嵌入分类器按"动作"粒度做路由决策，而非依赖提示词或人工规则，同时原生兼容多家客户端协议并支持一键接入 DeepSeek、Kimi、GLM 等模型。

---

## 9. [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)

> Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click

- ⭐ 本周 +10109 ｜ 总计 32376 ｜ TypeScript ｜ MIT

OpenMAIC 是清华团队开源的多智能体互动课堂平台，输入一个主题或文档即可一键生成幻灯片、测验、交互式模拟和项目式学习内容，并配有会讲课、能讨论的 AI 教师和 AI 同学。面向教育工作者、学习者以及希望做知识科普/培训内容的开发者。相比一般的"AI 生成 PPT"工具，新意在于 v1.0.0 引入的"Agent 工作台"模式——可对话式规划课程、支持服务端持久会话（可中断续跑）、20+ 内置技能（配图、配音、视频导出等），并采用模型/存储/搜索提供商全中立的可插拔架构。

---

## 10. [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer)

> An AI prompt optimizer for writing better prompts and getting better AI results.

- ⭐ 本周 +472 ｜ 总计 34166 ｜ TypeScript ｜ NOASSERTION
- 主页：https://prompt.always200.com

这是一款面向 AI 应用开发者、重度 Prompt 使用者及企业团队的提示词优化工具，能对系统提示词和用户提示词进行一键优化、多轮迭代改进，并支持单结果评估与多结果对比来提升 AI 输出质量。相比一般的 Prompt 调试/模板管理工具，它同时覆盖 Web、桌面、浏览器插件、Docker 等多种部署形态（桌面端可规避浏览器 CORS 限制），并集成了变量管理、Function Calling 调试、多轮对话测试及图像生成等更完整的工程化能力。
