# GitHub 周报：LLM / Agent（2026-07-24 – 2026-07-31）

这一周的主线不是"又出了个新 agent"，而是**大家开始给已有的 agent 打补丁**。涨得最猛的十个项目里，有六个压根不是 agent 本身，而是围着 Claude Code、Codex 这些既有工具做的外挂：教它怎么说话的（i-have-adhd）、教它怎么干活的（skills）、给它配浏览器的（ego-lite）、给它建代码地图的（code-review-graph）、帮它并行跑的（orca）。Agent 本体的竞争降温了，**harness 层的竞争刚开始**。

第二条暗线是省钱和去锁定。OmniRoute 一周涨 8.4k，卖点直白到没有技术含量——290 家服务商、一个端点、别被单一厂商绑死。同一周 sub2api 也在榜上。当 agent 一天烧掉的 token 比人还多，网关就从基础设施变成了刚需。

值得注意的是本周有两个同名 "ADHD" 主题的 agent skill 同时上榜（另一个是 `UditAkhourii/adhd`，本周 +791），这种撞车通常意味着一个真实痛点被同时命中：**没人受得了 agent 把答案埋在第三段**。

---

## 1. [mattpocock/skills](https://github.com/mattpocock/skills)

> Skills for Real Engineers. Straight from my .agents directory.

- ⭐ 本周 +12,147 ｜ 总计 196,222 ｜ Shell ｜ MIT

Matt Pocock 把自己 `.agents` 目录里在用的一套编码 agent 技能直接开源，包含 `/grill-me`、`/tdd`、`/diagnosing-bugs`、`/improve-codebase-architecture` 等工作流，可以从 Claude Code 插件市场装，也可以直接拷文件。它不是泛用提示词合集，而是针对 agent 的四类典型失效（对齐不足、输出啰嗦、代码质量差、架构腐化）逐一给对策，坚持小而可组合、把控制权留给开发者，而不是搞一整套接管式流程。

---

## 2. [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

> 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

- ⭐ 本周 +9,304 ｜ 总计 27,357 ｜ Python ｜ Apache-2.0

李博杰这本书的完整仓库，含全文、可自行构建的 PDF/EPUB，以及按章节配套的 94 个可调参实验。以「Agent = LLM + Context + Tools」为主线，覆盖上下文工程、记忆、多模态、模型训练到多智能体协作，强调 harness 工程而不是单纯选模型，还附了成本核算和评测框架。Apache 2.0 开源加十种语言版本，在同类 agent 教程里相当少见。

---

## 3. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

> Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models

- ⭐ 本周 +8,464 ｜ 总计 35,130 ｜ TypeScript ｜ MIT
- 主页：https://omniroute.online

一个本地优先的 AI 网关，把 290 多家模型服务商聚合到单一 OpenAI 兼容端点，自动处理路由、故障切换和请求压缩。适合想摆脱厂商锁定、控制账单的独立开发者和团队，尤其是同时用多种编码 agent 的人。和 OpenRouter、LiteLLM 比，差异点在于服务商目录更广且每两周重新核验免费额度，提供 19 种路由策略和十多个可叠加的压缩引擎，同时坚持自托管、零遥测、密钥本地加密。

---

## 4. [stablyai/orca](https://github.com/stablyai/orca)

> Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription.

- ⭐ 本周 +6,647 ｜ 总计 33,832 ｜ TypeScript ｜ MIT
- 主页：https://onOrca.dev

一个"Agent 开发环境"，能把 Claude Code、Codex、OpenCode 等 30 多种 CLI 编码 agent 同时跑在互相隔离的 git worktree 里，让你并行执行、横向对比，再挑最好的合并进主干。面向重度使用 AI 编码、希望多路并发又不被单一工具锁死的开发者和团队，支持桌面、移动端和 VPS 部署。相比只绑定单个 agent 的 IDE，它主打"用你自己的订阅跑任意 agent"，另配了 WebGL 终端、内嵌 Chromium、GitHub/Linear 集成和手机端查看进度的伴侣应用。

---

## 5. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

> Open-source & free — Battle-tested at Alibaba's scale. Hybrid architecture code review tool.

- ⭐ 本周 +5,322 ｜ 总计 16,569 ｜ Go ｜ Apache-2.0
- 主页：https://open-codereview.ai

命令行 AI 代码评审工具，读取 Git diff 后交给可配置的大模型 agent 分析，产出精确到行的结构化评审意见，也支持对整个代码库做全文件扫描审计。原本是阿里内部服务数千名开发者的官方评审助手，现在开源给需要规模化自动评审的团队。特点是把工程化确定性和 agent 灵活性结合：靠精准选文件、智能打包和外置定位模块保证覆盖率、消除行号漂移。官方基准称同底座模型下准确率和 F1 都高于通用 agent，token 消耗只有约九分之一（厂商自测数据，未经第三方验证）。

---

## 6. [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)

> The fastest browser for AI agents to run browser automation, built for sharing your logged-in browser state.

- ⭐ 本周 +5,037 ｜ 总计 6,497 ｜ JavaScript ｜ MIT
- 主页：https://lite.ego.app

一款 macOS 浏览器，给 AI agent 提供各自独立的工作区（Spaces），让 Claude Code、Codex、Cursor 等 agent 在后台自动化操作网页的同时，你还能照常用同一个浏览器上网。和 Browser-Use 那类需要另开浏览器的方案不同，它人机共用一个浏览器，agent 直接调 JavaScript 函数而不是命令行，首次启动会继承 Chrome 的登录态、Cookie、扩展和书签，内核级定制的页面快照还能处理嵌套 iframe。完全免费、数据本地存储。

---

## 7. [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

> A skill for your coding agent to stop it from burying the answer. ADHD-friendly output.

- ⭐ 本周 +4,978 ｜ 总计 14,214 ｜ Python ｜ MIT

给 Claude Code、Codex 等编程助手用的 skill，通过十条硬性格式规则把 AI 冗长发散的回答压成直给的行动指令：开口先说下一步干什么，多步骤编号，列表不超过 5 条，去掉铺垫和客套话。作者强调这种输出风格对所有想要信息干净利落的人都成立，不需要真的确诊 ADHD。与其说是工具，不如说是一份可以 fork 并按个人口味改写 SKILL.md 的沟通风格约定——切入点是助手的表达方式，而不是能力本身。

---

## 8. [earendil-works/pi](https://github.com/earendil-works/pi)

> AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI

- ⭐ 本周 +4,799 ｜ 总计 80,919 ｜ TypeScript ｜ MIT

一套自主编程 agent 的完整工具链：可自我扩展的交互式命令行 agent、负责工具调用与状态管理的运行时内核 Pi Agent Core、统一封装 OpenAI/Anthropic/Google 的 Pi AI 接口，外加一个支持差分渲染的终端 UI 库。面向要自建编程自动化又不想被单一模型厂商锁定的团队。相比同类框架，它把安全性摆在明面上：公开权限模型、三种容器隔离方案、依赖锁定到精确版本并定期审计，同时鼓励社区提交真实开源项目的工作会话记录，而不是只靠 benchmark 数据证明效果。

---

## 9. [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)

> Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase.

- ⭐ 本周 +2,061 ｜ 总计 27,765 ｜ Python ｜ MIT
- 主页：https://code-review-graph.com

用 Tree-sitter 解析源码并构建一张持久化的代码结构图，记录调用链、依赖关系和测试覆盖，改动发生时只把真正受影响的"波及范围"喂给 AI 编程助手。面向在大型或单体仓库里用 Claude Code、Cursor、Copilot 的团队。和依赖向量检索或纯文本搜索的方案不同，它靠语法树的结构化边回答"谁调用了这个方法""哪些测试覆盖了它"这类多跳问题，全程本地运行，图数据存在本地 SQLite，无需云服务。官方称中位数可省约 82 倍 token（自测数据）。

---

## 10. [infiniflow/ragflow](https://github.com/infiniflow/ragflow)

> RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine.

- ⭐ 本周 +698 ｜ 总计 86,443 ｜ Go ｜ Apache-2.0
- 主页：https://ragflow.io

开源的检索增强生成引擎，专注把 PDF 扫描件、图文混排这类复杂格式的非结构化文档解析、切分并组织成可检索的知识，再让大模型给出带引用出处的回答。个人开发者和需要接入多源异构数据的企业团队都在用。特别之处在于"深度文档理解"和模板化分块——切分结果可视化、可人工干预，加上强调可追溯的引用链来抑制幻觉，同时把 Agent 编排和 RAG 统一在一套框架里，支持云端托管与私有化部署。

---

## 附注

- 数据来源：`github.com/trending?since=weekly`（全站页 + Python / TypeScript / Jupyter / Rust / Go 六个页面）+ GitHub Search API 按 topic 兜底，本周共 201 个去重候选，30 个通过关键词过滤，最终取前 20 再人工挑 10。
- 十个项目全部来自 trending，`stars_this_week` 是 GitHub 实测的本周涨星数，非估算。
- 落选的高分候选：`CoreBunch/Instatic`（+2,872，本质是 CMS，"agentic" 是营销词）、`agegr/pi-web`（+1,027，是 pi 的 Web UI，与第 8 条重复）、`UditAkhourii/adhd`（+791，与第 7 条撞方向）。
- 各项目 README 中的自述数据（准确率、token 节省倍数、star 数等）均未经第三方验证，已在正文中标注。
