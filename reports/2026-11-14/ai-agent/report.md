# GitHub 周报：AI / Agent（2026-11-08 – 2026-11-15）

本周 AI / Agent 领域呈现出从「单一代码生成」向「全栈交付与自主协作基础设施」全面演进的深层趋势。智能体的应用场景不再局限于命令行内的代码拼装，而是迅速向外拓展：Meta 开源历经八年打磨的 astryx 设计系统，以开放基元与 swizzle 机制让 AI 深度参与界面工程；pingdotgg 的 t3code 与 Vercel Labs 的 agent-browser 分别在跨端控制平面与极简浏览器自动化 CLI 上奠定敏捷操控基石；Google 的 EGM 创新性地引入“大象上下文 + 金鱼独立盲审”双角色消除架构盲区；Google Chrome 联合各浏览器厂商推出的 modern-web-guidance 与 Addy Osmani 的 agent-skills 则以确定性规范与六阶段工程门禁重塑 AI 交付标准；morluto/rea 将逆向工程提升至二进制级自动化，CopilotKit 的 OpenBot 开启企业级虚拟同事自主沙箱，配合智能家居 MCP（ha-mcp）与垂直金融投研（daily_stock_analysis），展示出开源智能体生态向企业级落地、跨端互联与端到端交付的强劲推进力。

---

## 1. [meta/astryx](https://github.com/meta/astryx)

> An open source design system that's fully customizable and agent ready

- ⭐ 本周 +13660 ｜ 总计 28243 ｜ TypeScript ｜ MIT
- 主页：http://astryx.atmeta.com

Meta 开源的内部沿用 8 年的现代化企业级设计系统，全面拥抱 React 19+ 与 StyleX。面向需要构建复杂 Web 应用且希望让 AI 编码智能体深度参与 UI 设计与组件拼装的前端工程师与全栈团队。它打破了传统设计系统的黑盒封装，提供开放的底层基元与一键源码迁出机制（swizzle），让开发者与 AI Agent 能使用同一套统一、类型完备的组件库无缝协作。

---

## 2. [pingdotgg/t3code](https://github.com/pingdotgg/t3code)

> The best way to control Claude Code, Codex and more from any computer or phone

- ⭐ 本周 +9668 ｜ 总计 60704 ｜ TypeScript ｜ MIT
- 主页：https://t3.codes

由知名全栈工程师 Theo 开源的编码智能体跨设备控制面板（Control Plane），支持从任何电脑、网页端或手机无缝操控终端里的 Claude Code 与 Codex。面向经常在移动中或多台工作设备间切换、希望远程监控与下达 Agent 编程任务的现代开发者。它彻底打破了终端命令行工具受限于单台本地机器的藩篱，提供即时会话流式同步、远程权限批准与多模型协同编排体验。

---

## 3. [morluto/rea](https://github.com/morluto/rea)

> Reverse engineer anything with agents, from app behavior down to native binaries.

- ⭐ 总计 460156 ⭐（本周增量未测得） ｜ TypeScript ｜ MIT
- 主页：https://rea.tools

专为逆向工程打造的端到端 Agent 工具链与统一 MCP 服务，能够逆向拆解从上层应用交互到底层原生二进制程序的任意软件系统。面向安全研究员、漏洞挖掘者与需要深入分析第三方闭源软件架构的极客工程师。它将静态反编译、动态运行时行为捕获与大模型推理闭环打通，让智能体能够自主识别程序逻辑脉络、生成强化学习验证环境并自动化还原核心实现。

---

## 4. [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)

> Open-source plugin for designing and reviewing software with agents

- ⭐ 本周 +5539 ｜ 总计 19259 ｜ Python ｜ Apache-2.0
- 主页：https://egm.dev

Google 团队开源的软件架构设计与代码评审智能体插件，提出创新的“大象记忆 + 金鱼盲审”（EGM）双角色认知模型。面向大型复杂软件项目的架构师与工程团队，解决长期会话中模型受历史上下文思维定势干扰、遗漏架构盲区的问题。它通过高记忆容量的“大象 Agent”结合完整上下文沉淀设计规范，再交由毫无历史偏见的“金鱼 Agent”进行冷启动独立交叉盲审，由人类工程师把关最终决策。

---

## 5. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

> Browser automation CLI for AI agents

- ⭐ 本周 +4601 ｜ 总计 51274 ｜ Rust ｜ Apache-2.0
- 主页：https://agent-browser.dev

Vercel Labs 推出的原生 Rust 极速浏览器自动化 CLI 工具，专为 AI 智能体设计高效的网页交互接口。面向开发端到端自主 Web 任务、自动化测试或网络数据采集智能体的软件开发者。它抛弃了沉重复杂的通用浏览器自动化协议，采用极简的无障碍树快照提取页面结构并为可交互元素打上紧凑短标号（如 `@e1`），智能体单次 Shell 调用即可精准点击输入且保持浏览器持久会话，大幅降低 Token 消耗并提升执行速度。

---

## 6. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)

> LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。  LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs.

- ⭐ 本周 +4526 ｜ 总计 72282 ｜ Python ｜ MIT
- 主页：https://dsa.zhulinsen.tech

专注于量化金融与自选股投资分析的垂直领域智能体系统，支持 A股、港股、美股等多市场行情与实时资讯的自动化采集。面向个人量化投资爱好者与金融数据分析师，旨在免去每日繁琐盯盘与手动研报检索。系统集成多源实时行情、财报异动分析与大模型决策推演，能够全自动生成结构化决策看板，并通过 GitHub Actions 零成本定时运行，将每日投资晨报直推至企业微信、飞书、Telegram 等渠道。

---

## 7. [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

> Keep your coding agent up to date with the latest web best practices

- ⭐ 本周 +4363 ｜ 总计 6192 ｜ TypeScript ｜ Apache-2.0
- 主页：https://goo.gle/modern-web-guidance

由 Google Chrome、Microsoft Edge、Mozilla Firefox 与 MDN 官方团队联合发起的现代 Web 开发技能规范库，专为纠偏 AI 编码智能体的陈旧习惯而生。面向经常被模型产出的过时 HTML/CSS 技巧或废弃 JavaScript API 困扰的现代前端开发者。它将最新的浏览器原生标准、基线能力（Web Baseline）与无障碍规范封装为高质量 Agent Skills，从源头杜绝 AI 生成过时冗余的垫片代码。

---

## 8. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

> Production-grade engineering skills for AI coding agents.

- ⭐ 本周 +3670 ｜ 总计 117620 ｜ JavaScript ｜ MIT
- 主页：https://skills.addy.ie

资深前端架构师 Addy Osmani 提炼开源的工业级工程规范技能集，覆盖现代软件开发的完整生命周期。面向使用 Claude Code、Cursor、Codex 等主流智能体进行产品研发的工程团队。它将“定义需求（/spec）、规划架构（/plan）、编码实现（/build）、测试验证（/test）、代码审查（/review）、发布上线（/ship）”六个核心阶段固化为确定性质量门禁与工程工作流，确保智能体交付的代码兼具健壮性、可测试性与生产就绪度。

---

## 9. [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp)

> Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.

- ⭐ 本周 +2348 ｜ 总计 7837 ｜ Python ｜ MIT
- 主页：https://homeassistant-ai.github.io/ha-mcp/

为主流开源智能家居平台 Home Assistant 打造的官方 MCP（Model Context Protocol）服务器实现。面向拥有丰富智能家居设备、渴望通过大模型实现高阶自然语言家庭自动化控制的技术极客。它向 Claude、ChatGPT 等智能体暴露了超过 80 种细粒度控制与状态检索工具，不仅能精准执行跨设备联动，更能让模型自主诊断家庭自动化脚本配置中的逻辑冲突与语法异常。

---

## 10. [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)

> Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.

- ⭐ 本周 +1900 ｜ 总计 12297 ｜ TypeScript ｜ MIT
- 主页：open.bot

CopilotKit 团队开源的企业级可自托管 AI 虚拟同事工作空间，为每个智能体分配独立的虚拟运行环境（包含专属浏览器、文件系统与工具链）。面向希望在企业内网安全部署协作型智能体、要求全流程审计合规的技术负责人与研发组织。它基于开源 AG-UI 协议实现，要求智能体在采取任何操作前明确意图并完整记录执行轨迹，支持热插拔任意基础模型并轻松部署于 Kubernetes 集群。
