# GitHub 周报：AR / VR（2026-10-25 – 2026-11-01）

本周 AR / VR 赛道的核心看点聚焦于「跨平台串流基建的深耕」与「AI 驱动的空间内容生产爆发」。随着空间计算硬件（如 Apple Vision Pro 与 Meta Quest）的技术沉淀，开发者生态正加速摆脱单一厂商平台的封闭锁喉：ALVR 与 WayVR 在 Linux 与无线串流底层持续演进，打通了从 PC 显卡到独立头显的低延迟视听通路；在开发工具链端，Google 推出的 xrblocks 让 WebXR 与生成式 AI 快速拼装成原型，Besty0728 的 Unity-Skills 首次将 LLM Agent 自动化注入工业级 Unity 编辑器，而 PlayCanvas 的 supersplat-viewer 则将 3D Gaussian Splatting（高斯泼溅）的渲染门槛大幅降低至 Web 浏览器。整体而言，开源社区正在用更开放的协议与智能工具，铺平从传统三维制作通往未来空间体验的高速公路。

---

## 1. [Besty0728/Unity-Skills](https://github.com/Besty0728/Unity-Skills)

> AI automation skills specifically designed for Unity

- ⭐ 总计 1909 ⭐（本周增量未测得） ｜ C# ｜ MIT
- 主页：https://www.micostar.cc

专为 Unity 游戏引擎与 XR 内容开发设计的 AI 自动化技能扩展包，基于 REST API 将大语言模型能力深度注入 Unity 编辑器。面向游戏开发者、XR 场景设计师与技术美术。它让 AI 能够直接感知 Unity 场景层级并调用编辑器接口自动化完成 3D 资产摆放、光照烘焙、材质调整与脚本装配，大幅压缩了空间计算与 3D 场景原型制作的重复劳动。

---

## 2. [google/xrblocks](https://github.com/google/xrblocks)

> XR Blocks is a lightweight WebXR + AI library for rapidly prototyping advanced AI + XR experiences.

- ⭐ 总计 503 ⭐（本周增量未测得） ｜ TypeScript ｜ Apache-2.0
- 主页：https://xrblocks.github.io

Google 开源的轻量级 WebXR 与多模态 AI 融合开发库，主打空间智能体验的高速原型设计。面向 Web 前端开发者、XR 交互设计师与多模态应用探索者。它封装了手势追踪、环境感知空间锚点与 Gemini 多模态 API 的无缝联动模块，开发者只需几十行声明式代码即可在 Vision Pro、Quest 等支持 WebXR 的浏览器中跑通手势识别与实时空间交互。

---

## 3. [alvr-org/ALVR](https://github.com/alvr-org/ALVR)

> Stream VR games from your PC to your headset via Wi-Fi

- ⭐ 总计 8037 ⭐（本周增量未测得） ｜ Rust ｜ MIT

开源界标志性的无线 VR 串流解决方案（Air Light VR），支持将 PC 端的高画质 SteamVR/OpenXR 游戏画面通过局域网 Wi-Fi 实时无线串流至一体机头显。面向追求画质自由且不愿受制于官方串流工具的 VR 玩家与跨平台硬件极客。它不仅官方支持 Meta Quest 与 PICO，更率先适配了 Apple Vision Pro 的全手势串流与 Linux 宿主环境，具备极高帧率稳定性与极细粒度的视频编码调优选项。

---

## 4. [wayvr-org/wayvr](https://github.com/wayvr-org/wayvr)

> Your way to enjoy VR on Linux. Run apps inside VR & access your Wayland/X11 screens from Monado/WiVRn/SteamVR.

- ⭐ 总计 1470 ⭐（本周增量未测得） ｜ Rust ｜ GPL-3.0
- 主页：https://wayvr.org

专为 Linux 桌面环境打造的轻量级 OpenXR / OpenVR 空间计算桌面叠加层（前身为 WlxOverlay-S）。面向在 Linux 下开展日常开发与虚拟现实体验的高阶技术极客。它允许用户在保持极低 CPU 与 GPU 开销的前提下，将 Wayland 或 X11 桌面窗口悬浮投射到 Monado、WiVRn 或 SteamVR 空间中，甚至无需脱下头显即可直接在沉浸式空间中操作终端与调试代码。

---

## 5. [praydog/REFramework](https://github.com/praydog/REFramework)

> Mod loader, scripting platform, and VR support for all RE Engine games

- ⭐ 总计 5703 ⭐（本周增量未测得） ｜ C++ ｜ MIT
- 主页：https://reframework.praydog.com/

业界顶级的卡普空 RE 引擎通用模组框架与注入式 6DoF VR 运行时支持平台。面向希望在 PC VR 头显中体验《生化危机》、《怪物猎人》、《龙之信条 2》等 3A 大作的硬核玩家与游戏模组开发者。它通过底层内存 Hook 与立体渲染管线注入，不仅为多款原本仅支持平面的 3A 商业大作赋予了原生级第一人称沉浸式 VR 视角与动作控制器手势追踪，还集成了强大的 Lua 运行时供社区编写更复杂的交互逻辑。

---

## 6. [playcanvas/supersplat-viewer](https://github.com/playcanvas/supersplat-viewer)

> User-friendly, high-performance viewer for 3D Gaussian splats

- ⭐ 总计 608 ⭐（本周增量未测得） ｜ TypeScript ｜ MIT
- 主页：https://superspl.at

PlayCanvas 团队打造的高性能 Web 3D 高斯泼溅（3D Gaussian Splats）轻量化查看器与运行时组件。面向 3D 摄影测量工程师、XR 场景构建者与三维视觉研究团队。它依托 WebGL/WebGPU 极致的排序与并行光栅化算法，能够在浏览器中以极其平滑的 60fps 帧率即时渲染数百万高斯粒子构成的超逼真现实空间，并提供即插即用的轻量 HTML/ZIP 离线导出方案。
