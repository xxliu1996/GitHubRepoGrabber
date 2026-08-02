# GitHub 周报：LLM / Agent（2026-07-26 – 2026-08-02）

本周热榜有一个明显信号：Agent 生态正在从"能跑起来"转向"能被管住、能被信任"。一边是 OmniRoute、ego lite 这类继续在成本和体验上做减法的基础设施，另一边是微软 Agent Governance Toolkit、Tracer-Cloud OpenSRE 这类专门为"Agent 出了问题怎么办"而生的治理与可观测性项目开始冒头，说明大规模落地 Agent 之后，安全边界和故障响应正在变成刚需，而不是可选项。同时 Claude Code 的 Skill 生态继续爆发式增长，i-have-adhd、ego-lite 都在围绕"怎么让 Agent 输出更可控、行为更可靠"做文章。

---

## 1. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

> Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 500+ contributors

- ⭐ 本周 +7259 ｜ 总计 37138 ｜ TypeScript ｜ MIT
- 主页：https://omniroute.online

这是一个免费的 AI 网关，将 290 多个 AI 服务商（其中 90 多个提供免费额度）聚合到一个统一接口，供 Claude Code、Cursor、Copilot 等编码工具使用，主要面向想省钱、又不想在多个 SDK 和限流之间来回切换的开发者。相比同类聚合工具，它的卖点是通过 RTK + Caveman 压缩技术节省 15%-95% 的 token 消耗，并在仪表盘上实时、诚实地展示每月约 15.3 亿免费 token 的额度明细。

---

## 2. [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

> A skill to stop your coding agent from burying the answer. ADHD-friendly output.

- ⭐ 本周 +5232 ｜ 总计 15284 ｜ Python ｜ MIT

这是一个面向 Claude Code、Codex 等编码 AI 助手的技能插件，用于让 AI 的回答更直接、更少废话，面向不希望 AI 长篇铺垫、想要"先给结论再给步骤"的开发者。其独特卖点在于提出了一套明确的 10 条规则（先给下一步动作、多步任务编号、结尾给出具体下一步等），可以直接改变 AI 输出风格，且不要求用户本人有 ADHD。

---

## 3. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

> Open-source & free — Battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in fine-tuned ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible.

- ⭐ 本周 +4708 ｜ 总计 17520 ｜ Go ｜ Apache-2.0
- 主页：https://open-codereview.ai

这是阿里巴巴开源的 AI 代码评审 CLI 工具，脱胎于阿里内部服务了数万名开发者两年、发现百万级代码缺陷的官方 AI 审查助手，配置好模型接口即可读取 Git diff 并生成带精确行号的结构化评审意见。相比通用型 Agent 直接做代码评审，它采用"确定性工程 + Agent"混合架构，对必须保证正确的流程用工程逻辑硬约束而非纯语言模型驱动，同等模型下准确率更高，且仅消耗约 1/9 的 token。

---

## 4. [earendil-works/pi](https://github.com/earendil-works/pi)

> AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI

- ⭐ 本周 +4518 ｜ 总计 81988 ｜ TypeScript ｜ MIT

Pi 是一个可自我扩展的编程 Agent 命令行工具集，面向需要交互式 AI 编程助手的开发者，包含 Agent 运行时、统一多家 LLM 提供商接口的库，以及终端 UI 组件等多个模块化包。其特色在于默认不内置权限限制系统，转而提供容器化/沙箱隔离方案（如 Gondolin 微虚拟机、Docker）供用户按需选择隔离强度，同时在供应链安全上投入较大精力。

---

## 5. [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)

> The fastest browser for AI agents to run browser automation, built for sharing your logged-in browser state with your AI agents, like Codex or Claude Code, without disturbing you. Zero cost, zero config.

- ⭐ 本周 +4090 ｜ 总计 7414 ｜ JavaScript ｜ MIT
- 主页：https://lite.ego.app

ego lite 是一款专为人与 AI 智能体协同使用而设计的浏览器（目前仅支持 macOS），让用户和 AI 代理可以在各自独立的浏览器空间中并行工作，同时共享登录状态、Cookie 和标签页，面向需要频繁进行浏览器自动化任务的开发者。与 browser-use、agent-browser 等传统框架相比，它不需要额外配置，AI 代理可以直接复用用户本人的真实登录态，任务执行更快、消耗的 token 更少。

---

## 6. [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech)

> Build local voice agents with open-source models

- ⭐ 本周 +3772 ｜ 总计 10240 ｜ Python ｜ Apache-2.0

这是一个开源的低延迟语音对话代理管道，串联语音活动检测、语音识别、大语言模型和语音合成四个模块，并通过兼容 OpenAI Realtime 协议的 WebSocket 接口对外提供服务。面向想用开源模型自建语音助手后端的开发者，已被用作 Hugging Face Reachy Mini 机器人的生产级对话后端。其独特之处在于每个环节的组件都可自由替换，可实现完全本地化、开放的语音交互栈。

---

## 7. [openai/codex](https://github.com/openai/codex)

> Lightweight coding agent that runs in your terminal

- ⭐ 本周 +1836 ｜ 总计 103154 ｜ Rust ｜ Apache-2.0

Codex CLI 是 OpenAI 推出的本地运行编程 Agent，供开发者通过命令行使用 AI 辅助编码，也可登录 ChatGPT 账号直接使用，无需单独付费 API。该项目是 OpenAI Codex 生态的本地/CLI 入口，与面向 IDE 的插件版本、桌面 App 版本以及云端版本 Codex Web 形成本地-云端、CLI-IDE-桌面多形态互补的产品矩阵。

---

## 8. [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)

> AI Agent Governance Toolkit — Policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents. Covers 10/10 OWASP Agentic Top 10.

- ⭐ 本周 +652 ｜ 总计 5557 ｜ Python ｜ MIT

这是微软推出的 AI Agent 治理工具包，提供策略执行、身份认证、沙箱隔离和可观测性能力，帮助企业安全地将自主 AI Agent 部署到生产环境。面向需要为多 Agent 系统落地权限控制与合规审计的企业团队。与依赖"提示词约束"的安全方案不同，它在确定性的应用层代码中拦截每一次工具调用，使被禁止的行为在结构上不可能发生。

---

## 9. [infiniflow/ragflow](https://github.com/infiniflow/ragflow)

> RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

- ⭐ 本周 +633 ｜ 总计 86580 ｜ Go ｜ Apache-2.0
- 主页：https://ragflow.io

RAGFlow 是一款开源的检索增强生成引擎，将先进的 RAG 技术与 Agent 能力融合，帮助开发者将复杂的企业数据转化为可用于生产环境的高精度 AI 系统。面向各类规模企业的开发者，提供从文档解析、分块到智能问答的完整工作流。相比同类 RAG 项目，其亮点在于深度融合的上下文引擎、预置的 Agent 模板，以及对多种数据源和多模型的广泛支持。

---

## 10. [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre)

> Build your own AI SRE agents. The open source toolkit for the AI era.

- ⭐ 本周 +523 ｜ 总计 9729 ｜ Python ｜ Apache-2.0
- 主页：https://discord.com/invite/opensre

OpenSRE 是一个开源的 AI SRE 智能体框架，用于自动化调查和处理生产环境故障，可连接 60 余种已有运维工具，在自有基础设施上运行，目前处于公开 Alpha 阶段。面向需要 AI 辅助进行故障根因分析的运维团队。其独特卖点在于将其定位为强化学习训练与评测环境，通过合成故障场景评估根因定位准确率，志在成为 AI SRE 领域的标准基准测试平台。
