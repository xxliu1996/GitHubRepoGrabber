# GitHub 周报：LLM / Agent（2026-09-13 – 2026-09-20）

本周的十个项目呈现出一个明显转向：单点 Agent 工具已经不够看了,大家在拼"编排"和"体系"——多 Agent 并行调度(orca)、跨 Agent 通用审查层(open-code-review)、把研究流程整体接管(OpenResearch)、把碎片化最佳实践固化成成体系的工程技能包(agent-skills)。同时,LLM 应用正在往更垂直、更真实的业务场景下沉:企业知识库(WeKnora)、CRM 销售自动化(DeskcommCRM)、授权渗透测试(pentagi),说明"Agent 能不能干活"的验证已经从 demo 阶段进入到具体行业落地阶段。

---

## 1. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

> Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible.

- ⭐ 本周 +15028 ｜ 总计 37685 ｜ Go ｜ Apache-2.0
- 主页：https://open-codereview.ai

一款由阿里巴巴开源的 AI 代码审查命令行工具，支持在 Windows、macOS、Linux 上运行，并可与 Claude Code、Codex、Cursor、Kimi Code 等多种 AI 编码助手/Agent 集成。主要面向需要在多种 AI 编程工具之间统一代码审查流程的开发团队，特色在于作为跨平台、跨 Agent 生态的通用审查层，而非绑定单一 IDE 或模型。

---

## 2. [Tencent/WeKnora](https://github.com/Tencent/WeKnora)

> Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.

- ⭐ 本周 +4867 ｜ 总计 27529 ｜ Go ｜ NOASSERTION
- 主页：https://weknora.weixin.qq.com

腾讯开源的企业级 LLM 知识框架，围绕文档理解、语义检索与自主推理构建，核心能力包括快速 RAG 问答、可自主编排检索/MCP 工具/沙箱环境和网络搜索的 ReAct Agent，以及能将原始文档自动整理为可自我维护知识百科的 "Wiki Mode"。适合需要处理企业级复杂文档和多步骤任务的团队，新颖之处在于把传统 RAG 问答、自主 Agent 编排与自动生成/维护知识库融合在同一框架中。

---

## 3. [stablyai/orca](https://github.com/stablyai/orca)

> Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and remote runtime.

- ⭐ 本周 +5404 ｜ 总计 72723 ｜ TypeScript ｜ MIT
- 主页：https://onOrca.dev

一款跨平台 AI 编程编排桌面应用，可让 Codex、Claude Code、OpenCode、Pi 等多个编码 Agent 在各自独立的 Git worktree 中并行运行，并统一在一处追踪管理，支持"一份提示词分发给多个 Agent 并对比合并结果"。还配有手机端伴侣 App，可远程监控进度、接收完成通知并随时补充指令。相比单一 Agent 工具，新颖之处在于面向"多 Agent 并行编排 + 移动端协同"的工作流。

---

## 4. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

> Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

- ⭐ 本周 +3914 ｜ 总计 83496 ｜ Python ｜ MIT

这是一个为 AI Agent 一键接入互联网能力的工具，自动帮用户挑选、安装并"体检"最稳定的联网接入方式，免去手动配置与频繁适配的麻烦。主要面向使用 AI Agent/助手的开发者和普通用户，新颖之处在于把"接入方式随时代更迭"的复杂度封装起来，用户无需关心底层实现变化即可持续获得可靠的联网能力。

---

## 5. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

> Production-grade engineering skills for AI coding agents.

- ⭐ 本周 +3445 ｜ 总计 97105 ｜ JavaScript ｜ MIT
- 主页：https://skills.addy.ie

该项目为 AI 编程助手打包了一套"生产级"工程技能和 9 个覆盖开发全生命周期（从需求定义、规划、编码、测试、审查到上线）的斜杠命令，将资深工程师的最佳实践固化为可复用流程。主要面向使用 Claude Code、Cursor 等 AI 编码工具的开发团队，可通过统一 CLI 一键安装到 70 多种 Agent 工具中。特色在于不是单个提示词，而是成体系的质量门禁与自动化工作流，甚至支持"审批一次、后续自动完成编码与测试"的半自主开发模式。

---

## 6. [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat)

> Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

- ⭐ 本周 +1573 ｜ 总计 44414 ｜ TypeScript ｜ MIT
- 主页：https://librechat.ai/

LibreChat 是一个开源、可自托管的多模型聊天与 Agent 平台，支持接入 OpenAI、Anthropic 等多种大模型，并提供插件、代码执行、Agent 管理 API、可读写文件/执行 Bash 的附加工作区等企业级功能。面向希望在私有环境中部署统一 AI 交互界面的开发者和企业用户。新颖之处在于将传统聊天界面演进为支持多 Agent 管理、机器身份认证与代码审批控制的完整 Agent 运行平台，而不仅是一个聊天前端。

---

## 7. [melgarafael/DeskcommCRM](https://github.com/melgarafael/DeskcommCRM)

> Open-source AI sales OS — self-hosted CRM with native AI agents + WhatsApp (WAHA). Open alternative to Kommo, Octadesk & Intercom for any business that sells by chat. MCP-ready, multi-tenant, LGPD.

- ⭐ 本周 +1745 ｜ 总计 3320 ｜ TypeScript ｜ MIT
- 主页：https://deskcomm.com.br

一款开源自托管的 CRM 系统，核心卖点是让 AI Agent 在 WhatsApp 上自动接待、筛选和促成销售，面向中小企业和不想被 Kommo、Octadesk、Intercom 等收费 SaaS 按功能收费的团队。区别于同类商业 CRM，它强调数据自主可控、无订阅费，并提供一键式 VPS 部署脚本，降低自托管门槛。

---

## 8. [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi)

> Fully autonomous AI Agents system capable of performing complex penetration testing tasks

- ⭐ 本周 +1568 ｜ 总计 24761 ｜ Go ｜ MIT
- 主页：https://pentagi.com

一款面向安全研究人员和渗透测试人员的 AI 自动化渗透测试工具，利用大语言模型驱动的智能体自主完成授权的信息安全测试任务。特色在于支持多种 LLM 后端（OpenAI、Anthropic、Ollama、DeepSeek 等）、具备 Agent 监督机制、可安全隔离在 Docker 中执行，并集成了 Langfuse 可观测性与知识图谱，定位为面向专业授权测试场景的智能化替代传统人工渗透流程。

---

## 9. [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

> 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

- ⭐ 本周 +2731 ｜ 总计 48706 ｜ Python ｜ Apache-2.0

一本围绕"Agent = LLM + 上下文 + 工具"核心公式撰写的开源中文电子书，系统讲解 AI Agent 从原理到工程实践的全过程，面向想深入理解并动手构建 Agent 系统的开发者与研究者。区别于零散的博客教程，全书共 10 章并配有 109 个可复现实验，还提供多语言翻译版本和支持在线高亮笔记的阅读体验，兼具教材的系统性与开源社区的可操作性。

---

## 10. [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)

> Turn your coding agents into research agents

- ⭐ 本周 +4068 ｜ 总计 5397 ｜ Rust ｜ MIT
- 主页：https://openresearch.sh/

OpenResearch 是一个面向研究型智能体的本地优先工作台，可将 Claude Code、Codex、OpenCode、Cursor 或 Google Antigravity 等编码助手转变为能够审阅文献、提出假设、运行实验并产出研究成果的自动化科研代理，主打面向 AI 研究员、科研工程师等需要大规模并行实验管理的用户群体。相比同类工具，独特之处在于原生集成 git worktree 实现多方向并行探索、以 git 原生的实验树追踪可复现的实验版本，并支持本地、SSH、Slurm、K8s、Ray 等多种计算后端，同时坚持数据与代码默认保留在本地。
