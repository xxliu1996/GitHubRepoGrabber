# GitHub 周报：AI / Agent（2026-11-01 – 2026-11-08）

本周 Agent 赛道呈现出向「工业级协作范式」与「专业工程治理体系」纵深演进的鲜明特征。开发者与大厂生态不再停留于让 Agent 盲目写单文件代码，而是从并发架构、数据底座、审美约束到领域垂直交付展开全面升级：max-sixty/worktrunk 从底层以 Git Worktree 实现多 Agent 并发隔离，Donchitos 则直接将 Claude Code 升级为容纳 49 个岗位角色的虚拟游戏工作室；NVIDIA 推出 auto-ontology 为智能体注入确定性企业本体与知识图谱，打破“算得快但算错”的指标幻觉；pbakaus/impeccable 与 mattpocock/skills 则以静态规则和意图追问建立起代码交付的设计与工程防线；再加上 Anthropic 官方正式开源 Agent Skills 规范库、thedotmack/claude-mem 攻克跨会话持久记忆、freellmapi 聚合海量免费推理算力，以及 claude-seo 与 video-shotcraft 深入垂直领域的确定性交付，整个开源生态正在加速构建一套严谨、可控、高并发的工业化智能体生产体系。

---

## 1. [mattpocock/skills](https://github.com/mattpocock/skills)

> Skills for Real Engineers. Straight from my .agents directory.

- ⭐ 本周 +9664 ｜ 总计 317832 ｜ Shell ｜ MIT
- 主页：https://aihero.dev/skills

TypeScript 权威导师 Matt Pocock 开源的专业开发者 AI 编码技能集，直出个人日常高频使用的 `.agents` 目录。面向在 Claude Code、Cursor、Copilot 等环境中从事复杂软件研发的资深工程师。它主张轻量可组合与保留人类最终控制权，通过意图对齐追问（如 `/grill-me` 交互式需求访谈）与领域术语建模等机制，有效消除 Agent 在执行大任务时的交付偏差与失控跑偏。

---

## 2. [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)

> Auto Ontology is a Python framework for building semantic, graph-based reasoning layers over data. It enables deterministic query generation, better context retrieval, and more explainable AI for LLM and agent workflows.

- ⭐ 本周 +9044 ｜ 总计 9838 ｜ Python ｜ Apache-2.0

NVIDIA 开源的企业级语义上下文层构建框架，通过自动解析企业元数据构建语义本体与知识图谱。面向企业数据工程师与智能体开发者，服务于对业务指标准确性与可解释性要求极高的高价值数据智能场景。它直击传统 Text-to-SQL 与 RAG 方案“回答快但算错”的核心痛点，通过本体对齐跨系统口径与数据血缘，并通过标准 MCP 接口为各类 Agent 注入确定性、可验证的语义推理依据。

---

## 3. [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

> The design vocabulary for your coding agent. Steer with polish and bolder, review with critique and audit, catch AI slop before it ships.

- ⭐ 本周 +7623 ｜ 总计 105639 ｜ Rust ｜ Apache-2.0
- 主页：https://impeccable.style

为 AI 编码 Agent 打造的专业前端审美指令集与静态评审引擎。面向使用 Claude Code、Cursor 等工具开发 Web 界面、渴望根除千篇一律“AI 塑料感（AI slop）”的前端工程师与独立开发者。它通过 `bolder`、`polish`、`critique` 等具象化设计动作引导模型定向精修，并内置 62 条无需调用 LLM 的本地确定性规则，在代码交付前秒级拦截对比度缺失、排版混乱等低级审美缺陷。

---

## 4. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

> Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

- ⭐ 本周 +7482 ｜ 总计 114553 ｜ TypeScript ｜ Apache-2.0
- 主页：https://claude-mem.ai

为 Claude Code 等智能体打造的跨会话持久记忆伴生系统，兼容 Codex、Gemini CLI、Copilot 等主流平台。面向长期依赖 AI 编程工具进行复杂多会话项目维护的开发者，解决模型在新会话中“瞬间失忆”、重复读取代码库与重复踩坑的痛点。它颠覆了粗暴堆叠历史记录的低效做法，采用“后台观察者 Agent 实时压缩 + 主会话按需渐进召回”的双 Agent 协同架构，在保留完整开发记忆的同时大幅削减 Token 开销。

---

## 5. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)

> Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.

- ⭐ 本周 +5719 ｜ 总计 36645 ｜ Shell ｜ MIT

将单个 Claude Code 会话升级为全功能虚拟游戏开发工作室的编排系统，整合了 49 个分层智能体与 72 种专属技能。专为渴望端到端独立打造完整商业游戏、但缺乏全职专业团队的独立开发者与技术创作者设计。它突破了单 Agent 编码缺乏全局架构与代码容易腐化的局限，完整复刻了工业级游戏工作室策划、程序、美术、测试的三级岗位协同机制与自动化质量门禁。

---

## 6. [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi)

> 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint, plus any custom OpenAI-compatible endpoint. Smart routing, automatic failover, encrypted keys. Personal experimentation only.

- ⭐ 本周 +3780 ｜ 总计 48904 ｜ TypeScript ｜ MIT
- 主页：https://freellmapi.co

开源的大模型免费推理配额聚合与智能调度网关，将 34 家服务商、635 个免费模型端点统一收敛为单个标准的 OpenAI 兼容 `/v1` 接口。专为高频调用大模型运行实验性 Agent、追求极致低成本原型验证的个人开发者打造。系统内置了跨服务商的速率限制智能熔断、自动故障重试与细粒度配额追踪，让开发者无需手动管理数十把 API Key 即可稳定调用数十亿免费 Token 算力。

---

## 7. [anthropics/skills](https://github.com/anthropics/skills)

> Public repository for Agent Skills

- ⭐ 本周 +2796 ｜ 总计 188881 ｜ Python ｜ None

Anthropic 官方开源的 Agent Skills 规范标准与核心技能范例库。面向使用 Claude Code、Claude.ai 或 Claude API 构建垂直业务流程与自动化任务的开发者及企业团队。该仓库不仅确立了基于 `SKILL.md` 的开放可插拔技能标准，还首次完整开源了 Claude 官方同款的高保真复杂办公文档（Word、PDF、PPT、Excel）代码化生成与数据提取核心能力。

---

## 8. [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

> Universal SEO skill for Claude Code. 26 sub-skills + 19 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, agent readiness (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local SEO, e-commerce, international SEO, Google APIs, and PDF/Excel reporting. 9 optional extensions for live SEO data.

- ⭐ 本周 +2375 ｜ 总计 27287 ｜ Python ｜ MIT
- 主页：skool.com/ai-marketing-hub-pro

专为 Claude Code 打造的企业级自动化 SEO 与 GEO 审计技能，内置 19 个专业子 Agent 与 26 项专项检测能力。适用于需要全面诊断与重构网站可见性的独立开发者、站长与增长营销团队。它将深度多 Agent 并发分析嵌入终端开发流中，除了覆盖传统技术 SEO 与 E-E-A-T 质量评估外，更率先将针对 ChatGPT、Perplexity、Google AI Overviews 等生成式引擎的引用优化（GEO）纳入核心审计体系。

---

## 9. [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)

> Worktrunk is a CLI for Git worktree management, designed for parallel AI agent workflows

- ⭐ 本周 +2292 ｜ 总计 11972 ｜ Rust ｜ NOASSERTION
- 主页：https://worktrunk.dev

专为多 AI 编程智能体并发作业设计的 Git Worktree 极简管理 CLI 工具。面向需要同时调度多个 Agent 实例（如 Claude Code、Codex）并行处理不同功能分支、紧急修复或重构任务的工程师团队。它彻底消除了原生 Git Worktree 复杂的路径配置与分支管理心智负担，支持秒级创建完全隔离的工作树环境，结合自动化钩子有效避免并发 Agent 互相覆盖代码。

---

## 10. [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)

> AI video skill for Claude Code & Codex — cinematic, editable product promos with Remotion: 124 shot recipe cards, 150 motion previews, beat sync, sound design, Motion Workbench & JianYing (CapCut CN) export.

- ⭐ 本周 +2260 ｜ 总计 17665 ｜ TypeScript ｜ Apache-2.0
- 主页：https://vincentwei1021.github.io/video-shotcraft/

面向 Claude Code 与 Codex 的代码化产品宣传片生成 Agent 技能，基于 Remotion 框架实现界面录屏与分镜头代码化自动渲染。面向需要低成本、高效率产出高质感产品演示与发布短片的产品经理、独立开发者与内容创作者。它摒弃了不可控且容易形变的传统文生视频扩散模型，依托 150+ 模块化动效预设实现像素级保真、字体无失真的视频生成，并原生支持无损导出至剪映/CapCut 进行时间线二次微调。
