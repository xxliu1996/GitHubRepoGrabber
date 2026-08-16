# GitHub 周报：LLM / Agent（2026-08-09 – 2026-08-16）

本周热榜的重心明显从"造一个新 Agent"转向"管好一堆 Agent"——多智能体并行编排(Orca)、跨 Agent 共享记忆(TencentDB-Agent-Memory)、长周期任务治理(LoopX)三条线同时冒头,说明单 Agent 编程助手已经是标配,真正的战场变成了怎么协调、记住和监督一整支 Agent 团队。与此同时 Agent Skills 生态(Anthropic 官方仓库、addyosmani 的工程技能包、diagram-design 配图技能)继续扩张,而 RAG / 模型网关这类"基础设施"项目也在稳步迭代精度和可组合性。

---

## 1. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

> 29 editorial diagram types for Claude Code. Self-contained HTML + SVG. No shadows, no Mermaid-slop.

- ⭐ 本周 +14735 ｜ 总计 18706 ｜ HTML ｜ MIT

这是一个 Claude Code/Codex/Pi 的 Agent Skill,用于自动生成编辑级质感的静态 HTML 图表(架构图、流程图、时序图等),面向需要给博客/官网配图但不想在 Figma 里折腾配色布局的独立创作者和开发者。相比同类图表工具,它强调"编辑级审美+品牌自适应"、语义化图案描述,且默认零构建、零依赖的静态输出。

---

## 2. [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent)

> A self-improving RLM agent for coding workflows and long-running autonomous tasks.

- ⭐ 本周 +8488 ｜ 总计 16310 ｜ TypeScript ｜ MIT

这是一个开源的编程/研究智能体,面向需要长时间运行、自我改进型工作流的开发者,核心基于"递归语言模型(RLM)"和"持续性 Harness"两大抽象。新意在于上下文被当作可编程变量、子智能体可通过代码递归调用,且 Agent 能在会话中对自身操作模式做小幅度、有证据支撑的自我更新,支持后台守护进程式长任务与多智能体协作。

---

## 3. [stablyai/orca](https://github.com/stablyai/orca)

> Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and VPS.

- ⭐ 本周 +6054 ｜ 总计 46160 ｜ TypeScript ｜ MIT
- 主页：https://onOrca.dev

桌面端 AI 编程智能体编排工具,面向希望同时驱动多个编程 Agent(Codex、Claude Code、OpenCode、Pi)并行工作的重度开发者。新意在于让多个 Agent 各自在独立 git worktree 中并行跑同一任务再比较合并结果、配备手机端伴侣 App 远程监控,以及可点选真实浏览器 UI 元素直接注入 Agent 提示词的"设计模式"。

---

## 4. [earendil-works/pi](https://github.com/earendil-works/pi)

> AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI

- ⭐ 本周 +5422 ｜ 总计 90962 ｜ TypeScript ｜ MIT

统一 LLM API + agent loop + TUI 的编程 Agent 工具包,是本周多个 Agent 编排项目(如 Orca)底层可驱动的引擎之一,持续保持极高的关注度和更新频率。

---

## 5. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

> Production-grade engineering skills for AI coding agents.

- ⭐ 本周 +3300 ｜ 总计 87521 ｜ JavaScript ｜ MIT
- 主页：https://skills.addy.ie

一套面向 AI 编程代理的"生产级工程技能"集合,涵盖需求定义、规划、编码、测试、审查到上线全流程,通过 8 个斜杠命令把资深工程师的最佳实践固化下来。新意在于把整条软件交付生命周期串成一套可自动触发、可组合的技能体系,并可通过 CLI 一键安装进 70 多种代理工具。

---

## 6. [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)

> TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.

- ⭐ 本周 +3956 ｜ 总计 22006 ｜ TypeScript ｜ NOASSERTION

腾讯云推出的 AI Agent 记忆管理系统,让 Claude Code、Codex、CodeBuddy 等不同智能体通过统一代理共享同一份记忆,面向需要多智能体协作、长期记忆的开发者和团队。新意在于"零代码接入"——无需插件、Hook 或 MCP Server,把 Agent 的 base URL 指向 Proxy 即可让多种异构智能体共用同一记忆库,并支持团队级记忆。

---

## 7. [anthropics/skills](https://github.com/anthropics/skills)

> Public repository for Agent Skills

- ⭐ 本周 +2682 ｜ 总计 169576 ｜ Python ｜ 无 license 声明

Anthropic 官方维护的 Claude 技能示例仓库,每个技能是包含说明、脚本和资源的独立文件夹,涵盖创意设计、开发技术、企业协作及文档处理等场景。特别之处在于部分技能就是 Claude.ai 文档生成等生产功能背后实际使用的实现,可作为学习和构建复杂技能的官方参考范例。

---

## 8. [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag)

> The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases with the power of AI and knowledge graphs

- ⭐ 本周 +1756 ｜ 总计 4376 ｜ Python ｜ MIT
- 主页：https://code-graph-rag.com

使用 Tree-sitter 解析多语言代码库,并在 Memgraph 图数据库中构建代码结构知识图谱,让用户能用自然语言查询、编辑和优化代码。相比传统基于向量检索的代码 RAG,新意在于以图谱形式表达代码结构关系,并新增运行时调用追踪功能,通过实际运行代码动态捕获调用关系并合并进图谱。

---

## 9. [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard)

> Switchyard lets LLM applications route traffic across models and providers while preserving native OpenAI and Anthropic API compatibility - enabling flexible model selection, benchmarking, and cost/performance optimization.

- ⭐ 本周 +1326 ｜ 总计 1589 ｜ Rust ｜ Apache-2.0

用 Rust 编写的 LLM 流量代理/库,能在 OpenAI Chat、Anthropic Messages、OpenAI Responses 三种 API 格式之间做协议转换,并支持多后端路由。面向想把编码 Agent 接到自建开源模型的开发者,或需要跨模型做 A/B 测试与成本实验的团队;提供可组合的类型化路由算法和 Prometheus 运维指标,目前仍是实验性的 pre-alpha 项目。

---

## 10. [huangruiteng/loopx](https://github.com/huangruiteng/loopx)

> Long-horizon agent control plane for durable, governed work across Codex, Claude Code, and other harnesses.

- ⭐ 本周 +1245 ｜ 总计 4782 ｜ Python ｜ Apache-2.0
- 主页：https://my.feishu.cn/wiki/CaL5wMk9ui17ngkWzeUcMlAYnZg

一个开放、不绑定厂商的"状态控制平面",运行在 Codex、Claude Code、Cursor 等任意 agent 执行框架之上,为长周期任务提供目标、门禁、待办、证据、配额和交接等持久状态管理。与常见的 agent 框架不同,它不做任务执行本身,而是专注做"治理层",把危险权限、发布、生产写入等关键决定始终留给人类。
