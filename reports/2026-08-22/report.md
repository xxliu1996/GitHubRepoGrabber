# GitHub 周报：LLM / Agent（2026-08-16 – 2026-08-23）

这周的热榜有一个明显转向：单纯"能聊天的 Agent"已经不够看了，大家在拼的是 Agent 的**基础设施层**——怎么给它一个可审计的记忆/上下文数据库（OpenViking）、怎么把代码库变成图而不是文本喂给它（gortex）、怎么统一多 Agent 编排和治理（agent-framework、maka）、怎么在企业侧管好网关和安全边界（new-api、AI-Infra-Guard）。与此同时，"Agent Skills"作为一种轻量扩展协议正在快速铺开，从画图到设计稿生成都在往这个方向收敛。换句话说，行业焦点已经从"能不能跑起来"转移到"跑起来之后怎么管、怎么记、怎么审"。

---

## 1. [openai/codex](https://github.com/openai/codex)

> Lightweight coding agent that runs in your terminal

- ⭐ 本周 +6673 ｜ 总计 113670 ｜ Rust ｜ Apache-2.0

OpenAI 官方推出的编码 Agent CLI，可在本地终端运行，帮助开发者用自然语言驱动代码编写、调试和重构，也提供 IDE 插件、桌面应用及云端版本（Codex Web）多种形态。与其他 AI 编程助手不同的是它由 OpenAI 原生打造并与 ChatGPT 账号体系（Plus/Pro/Business 等）深度绑定，主打"本地优先、多入口统一体验"。适合已有 ChatGPT 订阅、希望在命令行或编辑器中直接调用 GPT 编码能力的开发者。

---

## 2. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

> 38 editorial diagram types for Claude Code, Codex, and Pi. Self-contained HTML + SVG. No shadows. No Mermaid slop.

- ⭐ 本周 +7368 ｜ 总计 25521 ｜ HTML ｜ MIT
- 主页：https://cathrynlavery.github.io/diagram-design/

一个面向 Claude Code、Codex 等 AI 编码助手的技能（skill），能生成 39 种"编辑级"图表类型（架构图、流程图、Sankey、鱼骨图等），输出为无需构建步骤的纯 HTML+SVG 静态文件。与常见的 Mermaid/AI 生成的"圆角方框"风格不同，它强调极简密度、品牌色自动匹配、语义化图案，主要面向写博客、做技术文档的独立开发者和内容创作者，替代 Figma 手工画图或忍受千篇一律的 AI 图表。

---

## 3. [volcengine/OpenViking](https://github.com/volcengine/OpenViking)

> Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills.

- ⭐ 本周 +3447 ｜ 总计 32115 ｜ Python ｜ AGPL-3.0
- 主页：https://openviking.ai/

字节跳动旗下火山引擎开源的"AI Agent 上下文数据库"，将记忆、资源和技能统一存成一个虚拟文件系统（viking:// 协议），Agent 可以像用 ls/tree/find 一样浏览自己的上下文，而不是依赖黑盒向量库检索。内容按 L0 摘要/L1 概览/L2 详情三级分层按需加载，且每次检索都会留下可观察、可调试的轨迹，适合构建长期记忆、多技能 Agent 系统的开发者。

---

## 4. [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)

> A full-stack AI Red Teaming platform securing AI ecosystems via Agent Scan, Skills Scan, MCP scan, AI Infra scan and LLM jailbreak evaluation.

- ⭐ 本周 +906 ｜ 总计 5534 ｜ Python ｜ Apache-2.0
- 主页：https://tencent.github.io/AI-Infra-Guard/

由腾讯朱雀实验室推出的 AI 红队安全平台，集成了 Agent 扫描、AI 基础设施漏洞扫描、MCP Server 与 Agent Skills 安全扫描、越狱评测等能力，帮助企业和个人对自身 AI 系统做安全自查。适合安全团队和 AI 基础设施运维者使用，可通过 Docker 一键部署或作为独立 CLI 调用。其特色在于覆盖面广（漏洞库超 2000 条规则、支持多轮越狱攻击检测），区别于单一维度的漏洞扫描工具。

---

## 5. [QuantumNous/new-api](https://github.com/QuantumNous/new-api)

> A unified AI model hub for aggregation & distribution. It supports cross-converting various LLMs into OpenAI-compatible, Claude-compatible, or Gemini-compatible formats.

- ⭐ 本周 +756 ｜ 总计 45945 ｜ Go ｜ AGPL-3.0
- 主页：https://www.newapi.ai

一款新一代 LLM 网关与 AI 资产管理系统，提供组织级鉴权、多模型统一接入、用量分析、成本核算及私有化部署能力。面向需要统一管理多个大模型 API（及下游客户/团队访问权限）的企业和开发者。相比同类网关项目，它更强调资产管理与合规使用边界，并已被 Cherry Studio、AionUi 等下游应用采用为信任伙伴。

---

## 6. [apache/maka](https://github.com/apache/maka)

> Apache Maka (Incubating) is a local-first AI agent workspace. Model messages, tool calls, tool results, permission decisions, and termination events are recorded as an append-only log.

- ⭐ 本周 +810 ｜ 总计 2172 ｜ TypeScript ｜ Apache-2.0

Apache 孵化中的本地优先 Agent 工作台，在沙箱边界内运行工具，并把模型消息、工具调用等执行过程完整记录为可恢复的"执行事实"，通过统一的 Runtime Host 支撑桌面端、终端 CLI 和评测三种入口。面向希望在自己机器上、自带模型运行 Agent 的开发者。区别于普通聊天类 Agent 工具，它强调数据不出本地、执行记录可审计恢复，目前仅支持 macOS Apple Silicon。

---

## 7. [zzet/gortex](https://github.com/zzet/gortex)

> High-performance code-intelligence engine for AI agents and IDE, supports 257 languages, multi repositories, based on graph, with access via CLI, MCP Server, and API.

- ⭐ 本周 +318 ｜ 总计 1459 ｜ Go ｜ Apache-2.0
- 主页：https://gortex.dev/

面向 AI 编程助手和 IDE 的高性能代码智能引擎，通过 tree-sitter 解析 257 种语言，把代码构建成持久化的知识图谱（函数、类、调用链、跨服务契约），并以 CLI、MCP Server、Web UI 三种形式暴露给 AI Agent 使用。适合需要在大型/多仓库代码库中让 AI 编程助手减少上下文读取量的团队。其差异化在于图原生查询替代整文件读取，号称单次响应节省高达 50 倍 token。

---

## 8. [microsoft/agent-framework](https://github.com/microsoft/agent-framework)

> A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET.

- ⭐ 本周 +235 ｜ 总计 13055 ｜ Python ｜ MIT
- 主页：https://aka.ms/agent-framework

微软推出的开源多语言（Python、.NET，另有独立 Go SDK）框架，用于构建生产级 AI Agent 和多 Agent 工作流。面向要把 Agent 从原型推向生产的团队，提供顺序、并发、交接、群协作等基于图的编排模式，并内置持久化、可恢复、可观测性、人机协同治理能力。相比一般的单次对话式框架，它统一了 Semantic Kernel 与 AutoGen 的能力路径，并支持声明式 YAML 定义 Agent、OpenTelemetry 可观测性。

---

## 9. [eneskirca/nodeterm](https://github.com/eneskirca/nodeterm)

> Node-based terminal manager for AI coding agents — tmux-backed terminals and parallel agent sessions as draggable nodes on an infinite pan/zoom canvas.

- ⭐ 本周 +424 ｜ 总计 1057 ｜ TypeScript ｜ NOASSERTION
- 主页：https://nodeterm.dev

基于节点的终端管理器，将多个真实终端和 Claude Code/Codex 等 AI Agent 会话以可拖拽节点的形式放在一个可无限缩放平移的画布上，同时可切换为看板视图管理多个实时 Agent 会话。面向多任务并行、容易在标签页中迷失上下文的开发者，支持 tmux 会话持久化、跨重启恢复、手机端接续会话。其新意在于用空间化画布+看板双视图取代传统堆叠终端标签。

---

## 10. [ZSeven-W/openpencil](https://github.com/ZSeven-W/openpencil)

> The world's first open-source AI-native vector design tool and the first to feature concurrent Agent Teams. Design-as-Code.

- ⭐ 本周 +628 ｜ 总计 5577 ｜ Rust ｜ MIT
- 主页：https://op.zseven.tech

一款开源的"AI 原生"矢量设计工具，面向设计师和开发者，主打用自然语言在无限画布上生成 UI，并支持多个 AI Agent 并发协作完成页面不同区块的设计。相较于同类工具，其特色在于设计文件以 JSON 形式存储（Design-as-Code，可 Git 版本管理和 diff）、内置 MCP Server 可直接接入 Claude Code/Codex 等终端 Agent 进行设计操作，并支持一键导出为 React/Vue/Flutter/SwiftUI 等多平台代码。
