# GitHub 周报：LLM / Agent（2026-08-02 – 2026-08-09）

这一周的热榜有个清晰的转向：单纯"能对话的 Agent"已经不够看了，大家在抢的是 Agent 的基础设施层——记忆怎么持久化和共享、多个 Agent 之间怎么交接进度、模型和工具怎么被稳定路由到。TencentDB-Agent-Memory 和 loopx 分别在解决"记忆资产化"和"长任务状态管理"这两个此前被忽视的问题；OmniRoute 则说明"一个端点打通全部模型"仍是刚需。与此同时，Google 和阿里都在把 Agent 能力产品化封装成可复用的 Skills / 评审工具，说明 Agent 正在从个人生产力工具走向团队基础设施。

---

## 1. [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)

> TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph), that are governed, shared, and equipped across agents and frameworks.

- ⭐ 本周 +8046 ｜ 总计 18272 ｜ TypeScript ｜ NOASSERTION

面向团队场景的 AI Agent 记忆中枢：把对话、文档、代码库统一沉淀为 Chat Memory、Skill、Wiki 知识图谱、CodeGraph 四类可复用"记忆资产"，供团队多个 Agent 按角色（如 Scout/Builder/Reviewer）按需调用。相比单纯的对话记忆或传统 RAG，它多了资产化的版本、所有权、权限管控与团队共享层，官方给出的 PersonaMem 测试提升达 48%→76%。

---

## 2. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

> Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 500+ contributors

- ⭐ 本周 +6559 ｜ 总计 43517 ｜ TypeScript ｜ MIT
- 主页：https://omniroute.online

一个免费开源（MIT）的 AI 网关，用单一端点聚合 290+ 提供商、500+ 模型（含 90+ 免费额度），兼容 Claude Code/Cursor 等主流编码工具接入。相比同类路由网关，它强调"零成本可用"（约 15.3 亿免费 token/月）、19 种路由策略加配额感知自动降级，以及多引擎 token 压缩（宣称平均节省约 89% token）。

---

## 3. [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)

> DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

- ⭐ 本周 +4704 ｜ 总计 33186 ｜ Go ｜ MIT
- 主页：http://reasonix.io/

一个面向终端/CLI 的开源编码 Agent，以单一 Go 二进制分发，零外部依赖，适合独立开发者或需要轻量部署的用户。区别于同类工具的亮点在于配置驱动（reasonix.toml 声明提供商、工具、插件）、支持双模型协同（执行器+规划器分离会话）以及针对 prefix-cache 稳定性优化的上下文维护机制，减少缓存失效导致的重复计算。

---

## 4. [huangruiteng/loopx](https://github.com/huangruiteng/loopx)

> Lightweight loop engineering state kernel for long-running AI agent teams. Agent-loop agnostic across Codex, Claude Code, and other coding agents, with durable goals, quota-aware auto-wake, executable todos, evidence logs, and verifiable handoffs.

- ⭐ 本周 +3398 ｜ 总计 3594 ｜ Python ｜ MIT
- 主页：https://my.feishu.cn/wiki/CaL5wMk9ui17ngkWzeUcMlAYnZg

这是一个轻量、与具体 agent-loop 实现无关的"状态内核"，用来给长时间运行的多智能体工作流（Codex、Claude Code 等）提供持久目标、配额感知、可执行 todo 和证据日志。面向需要跨多天、多轮次维护进度且要求人类保留关键决策权（owner/safety gate）的工程/研究团队。与一般的自动化编排框架不同，它不替换 agent 框架本身、也明确不做"自主生产控制器"，而是专注让多 agent 交接和进度对非工程人员也可读可验证。

---

## 5. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

> Fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible.

- ⭐ 本周 +2345 ｜ 总计 19738 ｜ Go ｜ Apache-2.0
- 主页：https://open-codereview.ai

阿里巴巴出品的 AI 代码评审 CLI 工具，读取 Git diff，通过可配置的 LLM Agent 生成行级精度的结构化评审意见，并支持 GitHub Actions/GitLab 等 CI 集成。面向需要更深层代码质量保障的开发团队，尤其是大型代码库场景。相比纯 LLM Agent 方案，它用"确定性 pipeline + Agent"混合架构，在同等模型下实现更高的精确率和 F1，且 token 消耗仅约为纯 Agent 方案的 1/9，是以精度换召回的取舍思路。

---

## 6. [google/skills](https://github.com/google/skills)

> Agent Skills for Google products and technologies

- ⭐ 本周 +1143 ｜ 总计 16784 ｜ Python ｜ Apache-2.0

Google 官方维护的 Agent Skills 合集，面向 Google Cloud 等 Google 产品与技术栈，通过 `npx skills add` 一键安装到 Claude Code、Codex 等主流 agent 工具中。面向 GCP 开发者、AI/ML 工程师、云架构师、DevOps 等需要 agent 与 Google 生态交互的用户。与通用教程型技能库不同，它偏"问题导向"（成本优化、故障排查、迁移等），覆盖 100+ 技能且仍在积极扩充中。

---

## 7. [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)

> A super fast Graph Database uses GraphBLAS under the hood for its sparse adjacency matrix graph representation. Our goal is to provide the best Knowledge Graph for LLM (GraphRAG).

- ⭐ 本周 +578 ｜ 总计 5441 ｜ Rust ｜ NOASSERTION
- 主页：https://www.falkordb.com/

基于稀疏矩阵和线性代数运算的高性能图数据库，用 Rust 实现，专为 LLM 知识图谱、Agent 记忆等场景优化低延迟查询。面向构建 GraphRAG、生成式 AI 应用的开发者。与传统图数据库相比，其新意在于是首个用稀疏矩阵表示邻接矩阵的可查询属性图数据库，兼容 OpenCypher 但性能架构完全不同。

---

## 8. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

> Browser automation CLI for AI agents

- ⭐ 本周 +541 ｜ 总计 40216 ｜ Rust ｜ Apache-2.0
- 主页：https://agent-browser.dev

纯 Rust 实现的浏览器自动化 CLI 工具，专为 AI Agent 设计，无需 Node.js/Playwright 依赖，可用于无服务器环境。面向构建 Agent 自动化系统的开发者。相比 Puppeteer/Playwright，新意在于用语义定位（ARIA 角色、文本等）替代脆弱的 CSS 选择器，更贴合 LLM 的理解方式，并内置域名白名单、凭证保险箱、会话加密持久化等面向 Agent 安全场景的能力。

---

## 9. [livekit/agents](https://github.com/livekit/agents)

> A framework for building realtime voice AI agents 🤖🎙️📹

- ⭐ 本周 +1170 ｜ 总计 12762 ｜ Python ｜ Apache-2.0
- 主页：https://docs.livekit.io/agents

用于构建可在服务器端运行的实时、多模态语音 Agent 的开源框架，支持"能听会说会看"的对话式 Agent。面向做语音 AI、实时交互应用（含电话/SIP 场景）的开发者。相比同类框架，新意在于可自由组合任意厂商的 STT/LLM/TTS/Realtime API、原生支持电话接入与任务调度分发、内置基于 Transformer 的语义断句减少打断，以及带 judge 评估的内置测试框架。

---

## 10. [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)

> 18 Lessons to Get Started Building AI Agents

- ⭐ 本周 +784 ｜ 总计 71657 ｜ Jupyter Notebook ｜ MIT
- 主页：https://aka.ms/ai-agents-beginners

微软出品的零基础 AI Agent 入门课程，各课独立可任意顺序学习，涵盖设计模式、多智能体系统、RAG、生产部署与安全等内容。面向完全没有 Agent 开发经验的初学者。相比一般技术教程，新意在于深度绑定 Microsoft Agent Framework/Foundry Agent Service，支持 50 多种语言的自动化翻译，且每课整合图文、视频、代码示例与 Discord 社区支持的多媒体学习体验。
