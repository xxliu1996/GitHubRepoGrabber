# GitHub 周报：AI 智能眼镜（2026-10-11 – 2026-10-18）

本周智能眼镜赛道仍处早期，合格项目多在几十到几百星，但主题意外地集中：几乎所有热门仓库都在干同一件事——"把眼镜从厂商手里解放出来"。无论是统一跨厂商硬件的开发 SDK、绕开 Meta 官方 App 直连 Ray-Ban 的第三方客户端，还是可自编译刷入的开源固件，共同诉求都是让开发者和用户能自带 AI 模型、不被专有生态绑定。换句话说，这个赛道正在复刻早年安卓刷机社区的剧本。本周来源均为 topic 搜索，星标为总量，涨星增量未实测。

---

## 1. [Mentra-Community/MentraOS](https://github.com/Mentra-Community/MentraOS)

> MentraOS is the leading smart glasses OS. See live captions, stream your view, talk to AI, and capture photos hands-free on compatible glasses.

- ⭐ 总计 2388 ⭐（本周增量未测得）｜ TypeScript ｜ Apache-2.0
- 主页：https://Mentraglass.com

面向智能眼镜开发者的开源操作系统平台，统一封装配对、连接、数据流和对摄像头/麦克风/显示/扬声器的硬件访问，主打"一次编写、跑在任意眼镜上"，同一个 App 可跨 Mentra Live、Even Realities、Vuzix、NIMO 等多家设备运行。相比各家专有 SDK，它用开源打通生态、避免厂商锁定，并自带 MiniApp 商店和手机端运行时支持多应用并行。

---

## 2. [Turbo1123/Turbo-IO](https://github.com/Turbo1123/Turbo-IO)

> 雷鸟 iO / RayNeo iO 非官方 SDK：原生鸿蒙 HarmonyOS SDK/客户端、iOS 客户端及 iOS/Android 官方 App 扩展。

- ⭐ 总计 252 ⭐（本周增量未测得）｜ Objective-C ｜ 其他许可

一套非官方 SDK，让开发者为 RayNeo iO 智能眼镜开发自定义应用与扩展，提供 iOS、Android、HarmonyOS 三端源码，涵盖语音 AI、本地导航、音乐、阅读和可定制仪表盘卡片。明确面向有编译、签名能力的开发者做非商业学习研究。它只改眼镜固件的应用层以降低风险，开放了一套可做自定义卡片/小应用的开发者生态，并诚实区分"代码可用/可编译/已实机验证"三种状态。

---

## 3. [straff2002/OpenGlasses](https://github.com/straff2002/OpenGlasses)

> Making Meta Ray-ban / Oakley glasses smarter. Non-Meta Model selection, agentic features, smart guidance.

- ⭐ 总计 119 ⭐（本周增量未测得）｜ Swift ｜ 其他许可
- 主页：https://testflight.apple.com/join/1dcAytte

一款名为 Avenkin 的隐私优先 AI 助手，运行于 iPhone、Apple Watch 及 Meta Ray-Ban、Oakley 等智能眼镜，支持语音、摄像头识物、实时翻译、记忆与免手操作，既面向个人用户，也面向现场作业、医疗记录和无障碍等专业场景。新在于用户可自由选择 AI 供应商（云端或本地 MLX/llama.cpp 离线模型）、语音引擎与音色，并深度集成眼镜镜片显示，摆脱 Meta 专有 AI 的绑定。

---

## 4. [brilliantlabsAR/halo-firmware](https://github.com/brilliantlabsAR/halo-firmware)

> Firmware for Halo, Brilliant Labs' AI glasses — Zephyr RTOS on the Alif Balletto, with a Lua runtime for on-device apps and BLE OTA updates

- ⭐ 总计 60 ⭐（本周增量未测得）｜ C ｜ 其他许可

Brilliant Labs 的 AI 智能眼镜 Halo 的开源固件，基于 Zephyr RTOS 与 Alif Balletto 芯片，内置 Lua 运行时、带回声消除的语音处理、显示驱动和 OTA 空中升级，让用户无需数据线、开发套件或厂商专用工具就能自行编译刷入定制固件。亮点在于用 MCUboot 的 test-boot 与自动回滚防止变砖，并把 NPU、音频管线、显示和 Lua 脚本整合成一个较完整、可自由改造的端侧 AI 平台。

---

## 5. [macedonga/visor](https://github.com/macedonga/visor)

> A de-metaified Meta Glasses client.

- ⭐ 总计 58 ⭐（本周增量未测得）｜ Kotlin ｜ AGPL-3.0

一款 Android 第三方客户端，通过蓝牙和 Wi-Fi Direct 直连 Ray-Ban Meta（Gen 2）智能眼镜，替代 Meta 官方 App，支持相册导入、实时取景、通知和 AI 助手等功能，面向注重隐私、希望自带 AI 模型的用户。新在于逆向实现了眼镜原生协议、完全无服务器/无数据上报，并可接入 Claude 或任意 OpenAI 兼容接口替代 Meta 的 AI。

---

## 6. [hkust-spark/xg-glass-sdk](https://github.com/hkust-spark/xg-glass-sdk)

> One API for smart-glasses apps - camera, mic, display, audio - across Rokid, Meta Ray-Ban, Brilliant Labs Frame, RayNeo, Even Realities G1, INMO, Omi, and a simulator. Android, iOS, and CLI

- ⭐ 总计 47 ⭐（本周增量未测得）｜ Kotlin ｜ Apache-2.0
- 主页：https://xg.glass

一个统一的智能眼镜开发库，把不同硬件差异抽象成单一 API，提供摄像头、麦克风、显示、音频四类核心能力，一套代码即可覆盖 Rokid、Meta Ray-Ban、Brilliant Labs Frame、RayNeo、Even Realities G1、INMO、Omi 等设备，支持 Android/iOS/CLI。与同类相比，它更强调无硬件也能开发的模拟器和跨平台抽象层，降低集成多家 SDK 的复杂度（目前仍是较早期的小项目）。
