# GitHub 周报：AR / VR（2026-10-11 – 2026-10-18）

本周 AR/VR 赛道动静不大，没有爆款新项目，涨星主力仍是"把 VR 内容搬到更多地方跑"的基础设施：PC 游戏无线串流进一体机、把非 VR 游戏移植进新头显、给 RE 引擎游戏加体感。值得单拎出来的新信号有两个——一是 Valve 的 Steam Frame 头显刚问世就冒出了社区移植工具，二是 Google 把 Gemini 直接塞进了 WebXR 原型库，"XR + 多模态 AI"开始从概念变成可上手的脚手架。本周来源均为 topic 搜索，星标为总量，涨星增量未实测。

---

## 1. [alvr-org/ALVR](https://github.com/alvr-org/ALVR)

> Stream VR games from your PC to your headset via Wi-Fi

- ⭐ 总计 8005 ⭐（本周增量未测得）｜ Rust ｜ MIT

把 PC 上的 VR 游戏通过 Wi-Fi 无线串流到一体机头显，省掉数据线束缚，面向拥有 Quest、Pico、Vive Focus 等一体机又想玩 PC VR 游戏的玩家。相比同类方案，它开源、兼容的头显平台更广（连 Apple Vision Pro 都支持），并有活跃社区持续适配新设备与系统。

---

## 2. [praydog/REFramework](https://github.com/praydog/REFramework)

> Mod loader, scripting platform, and VR support for all RE Engine games

- ⭐ 总计 5649 ⭐（本周增量未测得）｜ C++ ｜ MIT
- 主页：https://reframework.praydog.com/

面向 Capcom RE 引擎游戏的模组框架、Lua 脚本平台和改造工具，内置 VR（含体感控制器）支持以及自由视角、FOV、画面比例修正等常用增强。它的独特之处在于用一套框架同时覆盖脚本平台、插件系统、VR 和现成增强，并横跨 RE2-4、RE7-8、鬼泣5、怪物猎人崛起/荒野、街霸6 等众多作品，而非把这些功能拆成多个独立工具。

---

## 3. [pmndrs/xr](https://github.com/pmndrs/xr)

> 🤳 VR/AR for react-three-fiber

- ⭐ 总计 2617 ⭐（本周增量未测得）｜ TypeScript ｜ 其他许可
- 主页：https://pmndrs.github.io/xr/docs/

一个让 React Three Fiber 应用借助 WebXR 快速变成 VR/AR 沉浸式体验的库，面向用 React 做 3D 网页、想低成本加上空间计算能力的前端开发者。新意在于接入极简——建 store、包一个 `<XR>` 组件、加个入口按钮三步即可，同时内置手部/手柄追踪、空间锚点、命中测试、传送等完整能力，支持渐进式采用。

---

## 4. [playcanvas/supersplat-viewer](https://github.com/playcanvas/supersplat-viewer)

> User-friendly, high-performance viewer for 3D Gaussian splats

- ⭐ 总计 596 ⭐（本周增量未测得）｜ TypeScript ｜ MIT
- 主页：https://superspl.at

SuperSplat 平台的官方查看器，用于高性能展示 3D 高斯泼溅（Gaussian Splat）场景，可编译成自包含的静态网页，面向使用高斯泼溅技术、需要在浏览器中可视化和交互的开发者。亮点是默认 WebGPU 并自动回退 WebGL、支持 WebXR（AR/VR），提供丰富的 URL 参数在不改代码的情况下控制加载与界面，并以 NPM 包和 API 形式方便嵌入。

---

## 5. [google/xrblocks](https://github.com/google/xrblocks)

> XR Blocks is a lightweight WebXR + AI library for rapidly prototyping advanced AI + XR experiences.

- ⭐ 总计 486 ⭐（本周增量未测得）｜ TypeScript ｜ Apache-2.0
- 主页：https://xrblocks.github.io

Google 出品的轻量级跨平台库，用于快速原型化融合 XR 与 AI 的体验，可跑在 Galaxy XR、XREAL Aura 乃至桌面 Chrome 上。区别于传统 WebXR 库，它原生集成 Gemini 带来多模态理解与实时对话，并附带手势识别、深度感知、空间 UI 组件，还提供免代码的云端 Gem 工具和无需头显的桌面模拟器。

---

## 6. [spoopyghosty0/frameport](https://github.com/spoopyghosty0/frameport)

> Port games to work with the Steam Frame

- ⭐ 总计 186 ⭐（本周增量未测得）｜ Python ｜ GPL-3.0
- 主页：https://frameport.app/

把 Quest 游戏、安卓/Linux 应用以及 PC VR 游戏安装到 Valve Steam Frame 头显上的工具，会自动打补丁做兼容并把游戏连同封面整合进 Steam 库，面向想突破原生游戏阵容的 Steam Frame 玩家。相比同类的 FrameDrop，它主打开源免费、跨平台（Win/macOS/Linux，对手仅限 Windows）、已为 120+ 款 Quest 游戏做过转换适配，且只需在头显终端敲一行命令即可完成安装。
