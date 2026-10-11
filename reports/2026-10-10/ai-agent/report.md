# GitHub 周报：AI / Agent（2026-10-04 – 2026-10-11）

本周的主线非常清楚：Agent 正在从"能聊"转向"能干活"，而让它干活的基础设施一个接一个涌出来。给 Agent 接真实浏览器（moli）、接整个互联网（Agent-Reach）、接 CAD（text-to-cad）这类"外接感官/手脚"的项目同时登榜，说明大家默认 Agent 本体已够用，瓶颈在于它能不能稳定地触达外部世界。另一条支线是围绕工程化的收尾：持久记忆（claude-mem）、多 Agent 编排（openrig）、token 成本压缩（caveman），以及把技能/插件打包分发（mattpocock/skills、knowledge-work-plugins）。值得注意的是，几乎所有新项目都不再绑定单一模型或单一 CLI，而是默认"跨 Claude Code / Codex / Cursor / Gemini 多端通吃"——Agent 生态的竞争焦点正从模型转向可移植的能力层。

---

## 1. [lexmount/moli](https://github.com/lexmount/moli)

> Best headless browser for AI agents. Lite, Fast, High-Compatibility. Built in Rust

- ⭐ 本周 +9973 ｜ 总计 15689 ｜ Rust ｜ Apache-2.0
- 主页：https://browser.lexmount.com

面向 AI Agent 的生产级无头浏览器，用 Rust 重写，核心思路是"结构优先、像素按需"——完整浏览器运行时配极轻资源占用，让 Agent 稳定地抓网页、提内容、做自动化。相比传统无头 Chrome 方案开销更低，且支持 CLI / CDP / WebDriver 多种接入，还能直接以 skill 形式交给 Agent 自助安装。

---

## 2. [mattpocock/skills](https://github.com/mattpocock/skills)

> Skills for Real Engineers. Straight from my .agents directory.

- ⭐ 本周 +9179 ｜ 总计 284639 ｜ Shell ｜ MIT
- 主页：https://aihero.dev/skills

TypeScript 知名作者 Matt Pocock 从自己 `.agents` 目录里整理出的一套"做真实工程"的 Agent 技能集，一条命令即可装进 Claude Code、Codex、Copilot、Gemini 等多端。它刻意把技能做得小巧、可改、可组合、与模型无关，专门针对"Agent 没按我意图做事"这类失败模式，而不是像 Spec-Kit 那样强加一整套重流程。

---

## 3. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

> Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

- ⭐ 本周 +6056 ｜ 总计 95512 ｜ Python ｜ MIT

一键给 Agent 装上"联网感官"的工具集：读网页、取 YouTube 字幕、搜 Reddit/Twitter、刷小红书和 B 站，把逐个踩坑的付费 API、反爬、登录态、数据清洗打包成一句话安装。每个平台走"首选+备选"多后端路由并由项目方持续跟进换代，接入失效会替用户无感切换，且强调完全免费、Cookie 只存本地。

---

## 4. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

> Write HTML. Render video. Built for agents.

- ⭐ 本周 +4081 ｜ 总计 60401 ｜ TypeScript ｜ Apache-2.0
- 主页：https://hyperframes.dev

HeyGen 开源的"写 HTML 就能渲染出确定性 MP4"的框架，把 HTML/CSS/媒体和可定位动画编译成视频，可本地 CLI 运行也可作为托管渲染内核。它配套 21 个按需加载的 skill，教 Agent 走完规划、写合法 HTML、接动画、加媒体到 lint/预览/渲染的整条流水线。相比 Remotion 的 React 路线，它以 HTML 为创作载体、强调确定性渲染与 Agent 原生的 skill 体系。

---

## 5. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

> Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions.

- ⭐ 本周 +4035 ｜ 总计 99299 ｜ TypeScript ｜ Apache-2.0
- 主页：https://claude-mem.ai

一个跨会话的持久记忆系统，把历史会话用 AI 压缩成可长期调用的记忆，再在后续会话中按需注入，让 Agent 不再"失忆"。面向重度 Claude Code（及 Codex、Gemini、Copilot 等）用户，相比手动笔记或裸上下文窗口，新意在于自动化的记忆压缩与持久存储并深度嵌入工作流。

---

## 6. [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

> Open source repository of plugins primarily intended for knowledge workers to use in Claude Cowork

- ⭐ 本周 +2644 ｜ 总计 28853 ｜ Python ｜ Apache-2.0

Anthropic 官方开源的一批"知识工作"插件，把 Claude 变成销售、法务、财务、数据、产品等具体岗位的专家，每个插件打包对应岗位的技能、连接器（Slack、Notion、HubSpot、Snowflake 等）、斜杠命令和子 Agent。主要面向 Claude Cowork 用户，也兼容 Claude Code，不同于通用助手之处在于按职能垂直封装、可针对公司自身工具与术语深度定制。

---

## 7. [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi)

> 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint, plus any custom OpenAI-compatible endpoint.

- ⭐ 本周 +2591 ｜ 总计 32966 ｜ TypeScript ｜ MIT
- 主页：https://freellmapi.co

把 34 家免费 LLM 提供商、600 多个免费端点聚合到一个 OpenAI 兼容的 `/v1` 接口后面，内置路由自动挑可用模型、被限流时切换提供商，并按密钥追踪用量守住各家免费额度。面向想零成本调用大模型、或给 Agent/CLI 接免费额度的开发者，相比手动管理多家 key，新意在于统一聚合、自动故障转移与自动更新的模型目录（仅供个人实验用途）。

---

## 8. [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)

> Give your agent CAD superpowers.

- ⭐ 本周 +2369 ｜ 总计 19007 ｜ Python ｜ MIT
- 主页：https://www.texttocad.dev

给 Claude Code、Cursor、Codex、Gemini 等编码 Agent 加装一套本地 CAD 能力：把自然语言生成为 STEP/GLB/STL/3MF 模型，做可制造性检查、出工程图，还能对接 3D 打印、钣金和 CNC 加工服务。它走插件/skills 路线直接嵌进已有 Agent，底层基于 build123d 与 Open CASCADE 开源内核，把参数化建模和制造落地打通成一条本地工作流。

---

## 9. [mvschwarz/openrig](https://github.com/mvschwarz/openrig)

> Build your own network of agents from Claude Code, Codex and Pi: persistent teams with roles, shared context and owned work.

- ⭐ 本周 +2068 ｜ 总计 6743 ｜ TypeScript ｜ Apache-2.0
- 主页：https://openrig.dev

用 YAML 定义、一条命令启动的多 Agent 编排系统，把一堆散乱的编码终端会话（Claude Code、Codex 等）组织成持久、分工明确的 Agent 团队。用户只跟一个"主管 Agent"说清目标，它便协调各专业小组干活并把需要决策的事反馈上来。相比单 Agent 或轻量任务编排，它强调团队的状态、上下文和成果能跨会话长期沉淀在同一处。

---

## 10. [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

> 🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.

- ⭐ 本周 +1642 ｜ 总计 110939 ｜ Go ｜ Apache-2.0
- 主页：https://docs.caveman.so/docs/quickstart

一个给 Agent 省 token 的工具：通过代理层和 skill 把 Agent 输出（以及读入的网页）压缩成极简"原始人式"短句，在保留代码、命令、数字等关键载荷的前提下大幅减少 token。它不靠微调或裁剪能力，而是套用航空维修手册的受控英语规范（ASD-STE100）——答案先行、一句一意、载荷逐字保留，据称已被 Adobe Research、JetBrains 等验证。
