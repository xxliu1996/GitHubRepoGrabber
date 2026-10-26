# GitHub 周报：AR / VR（2026-10-19 – 2026-10-26）

本周 AR/VR 赛道动静不大，没有一个项目登上 GitHub Trending，入选的五个项目都来自 topic 搜索，星数是总量，本周增量未测得。不过这五个项目的方向出奇一致：都是玩家和社区在补头显厂商没做的事。FramePort 帮新发布的 Steam Frame 补游戏库，WiVRn 把被 Windows 垄断的 PC VR 串流搬上 Linux，GalaxyQuest 用反编译源码把老游戏原生移植进 Quest，nunif 让任意 2D 视频变成立体内容。硬件迭代很快，内容和生态的缺口眼下靠开源社区来填。

---

## 1. [spoopyghosty0/frameport](https://github.com/spoopyghosty0/frameport)

> Port games to work with the Steam Frame

- ⭐ 总计 219 ⭐（本周增量未测得） ｜ Python ｜ GPL-3.0
- 主页：https://frameport.app/

跨平台桌面工具，把 Quest 游戏、Android 应用、Linux 应用和 PC VR 游戏装到 Valve Steam Frame 头显上，面向想把现有 VR 内容搬过去玩的玩家。官方工具只能原样安装，FramePort 则按社区测试过的「配方」，为数百款原本跑不起来的 Quest 游戏打补丁和转换。游戏启动失败时，它会读取日志，建议该打哪个补丁。

---

## 2. [WiVRn/WiVRn](https://github.com/WiVRn/WiVRn)

> The Linux OpenXR streaming application to standalone headsets

- ⭐ 总计 1818 ⭐（本周增量未测得） ｜ C++ ｜ GPL-3.0

完全开源的 PC VR 无线串流方案，把 Linux 电脑上的 VR 游戏传到 Quest、Pico、Vive Focus、Galaxy XR 等一体机上。同类串流方案大多只支持 Windows 或者闭源，WiVRn 以 Linux 为核心、全栈开源，借助 xrizer/OpenComposite 兼容 Steam 和 OpenVR 游戏。它还会把麦克风、手部和眼动追踪等输入转发回 PC。

---

## 3. [bigmak94/GalaxyQuest](https://github.com/bigmak94/GalaxyQuest)

> GalaxyQuest: Super Mario Galaxy in VR on Meta Quest 3, a native port built on the Petari decompilation. Bring your own game files. 100% made by AI (Claude Opus 5.5 in Claude Code).

- ⭐ 总计 119 ⭐（本周增量未测得） ｜ C++ ｜ Unlicense

把《超级马力欧银河》原生移植到 Meta Quest 2/3/3S 上以 VR 方式游玩，需要玩家自备正版游戏文件。它不是模拟器，而是基于 Petari 反编译出的 C++ 源码直接为头显处理器编译，再通过 OpenXR 呈现。关卡可以缩成桌面上的立体模型来玩，也能切到带透视的巨幕模式。README 称代码全部由 AI 编写，这本身就值得关注。

---

## 4. [nagadomi/nunif](https://github.com/nagadomi/nunif)

> Misc; latest version of waifu2x;  2D video to stereo 3D video conversion

- ⭐ 总计 3525 ⭐（本周增量未测得） ｜ Python ｜ MIT

waifu2x 作者的工具集，在 VR 场景里的主角是其中的 iw3：把任意 2D 图片或视频转成左右并排（SBS）的立体 3D 内容，适合想在头显里把普通视频当 3D 看的个人用户。与只能离线转换的同类工具不同，它的 iw3-desktop 能把电脑桌面实时转成 3D 并推流；配套的 iw3-player 用 WebXR 在头显里播放。从转换到观看，整条链路都能在本地完成。

---

## 5. [BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js)

> Babylon.js is a powerful, beautiful, simple, and open game and rendering engine packed into a friendly JavaScript framework.

- ⭐ 总计 26225 ⭐（本周增量未测得） ｜ TypeScript ｜ Apache-2.0
- 主页：http://www.babylonjs.com

老牌开源网页 3D 引擎，面向用 JavaScript/TypeScript 开发网页 3D、游戏和 WebXR 应用的开发者。它支持 ES6 模块和按需打包，类型定义完整，在线 Playground 和大量示例让原型开发很快。对想在浏览器里直接跑 XR 体验、不走应用商店的团队，它仍是 three.js 之外最完整的选择。
