# GitHub 周报：AI 智能眼镜（2026-10-25 – 2026-11-01）

本周 AI 智能眼镜赛道呈现出极其鲜明的「硬件自制、私有化反叛与跨设备破壁」共识。随着日常佩戴型智能眼镜的保有量持续上升，开发者社区对大厂封闭生态、云端隐私滥用以及协议碎片化的反弹全面具象化：macedonga/visor 与 straff2002/OpenGlasses（Avenkin）双管齐下，通过逆向协议彻底瓦解了 Ray-Ban Meta 的云端锁喉，让用户自主掌控第一人称视觉数据并换装私有模型；MentraOS 在开源操作系统与跨品牌微应用层持续领跑，Turbo-IO 为雷鸟 iO 打通了双端原生扩展；更具开拓性的是，Iam5tillLearning/OpenSource-Ai-Glasses 带来了基于嵌入式 Linux 的全套自制眼镜软硬件方案，而 Brilliant Labs 则将 Halo 的 Zephyr RTOS 底层固件全量开源。AI 智能眼镜正加速摆脱科技巨头的花园围墙，走向硬件自研、模型自由与隐私第一的硬核创客时代。

---

## 1. [Mentra-Community/MentraOS](https://github.com/Mentra-Community/MentraOS)

> MentraOS is the leading smart glasses OS. See live captions, stream your view, talk to AI, and capture photos hands-free on compatible glasses.

- ⭐ 总计 2395 ⭐（本周增量未测得） ｜ TypeScript ｜ Apache-2.0
- 主页：https://Mentraglass.com

开源智能眼镜全功能操作系统与微应用生态平台，已原生适配 Even Realities G1、雷鸟 RayNeo、Vuzix 等多款主流智能眼镜硬件。面向智能眼镜佩戴者与可穿戴应用开发者。它为低功耗眼镜光波导显示屏提供了统一的实时双语字幕、第一人称视角流媒体直播与端云协同多模态 AI 对话体验，并建有开放的微应用商店（Miniapp Store），免去了开发者为每款眼镜重复适配驱动的困扰。

---

## 2. [Turbo1123/Turbo-IO](https://github.com/Turbo1123/Turbo-IO)

> 雷鸟 iO / RayNeo iO 非官方 SDK：原生鸿蒙 HarmonyOS SDK/客户端、iOS 客户端及 iOS/Android 官方 App 扩展。自有模型、联网搜索、眼镜导航、录音研究、Codex 与 Web 预览，各平台能力以文档为准。面向开发者，仅供非商业学习研究；只提供源码，不提供 IPA/APK/HAP 或签名包。

- ⭐ 总计 311 ⭐（本周增量未测得） ｜ Objective-C ｜ 其他许可

针对雷鸟 RayNeo iO 智能眼镜的非官方跨平台 SDK 与深度扩展项目，全量开放了 Android 与 iOS 双端完整源码。面向希望深度挖掘雷鸟眼镜硬件潜力的开发者与可穿戴极客。它突破了原厂封闭生态的限制，提供了可自定义的眼镜端 HUD 仪表盘、非官方插件扩展、外挂自有大语言模型、联网搜索与独立录音研究工具。

---

## 3. [Iam5tillLearning/OpenSource-Ai-Glasses](https://github.com/Iam5tillLearning/OpenSource-Ai-Glasses)

> Open-source standalone AI glasses platform built on embedded Linux, with system-level customization, C/C++ SDK, RTSP video streaming, BLE, audio, camera, and optional display support.

- ⭐ 总计 300 ⭐（本周增量未测得） ｜ C ｜ Apache-2.0

基于嵌入式 Linux 的全栈开源独立 AI 智能眼镜硬件与软件平台，涵盖底层内核、驱动、C/C++ SDK 及应用框架。面向硬件创客、嵌入式工程师与医疗/工业领域的定制化可穿戴研发团队。与多数依赖手机蓝牙桥接的轻量方案不同，它在眼镜本体上实现了完整的系统级控制，支持 RTSP 低延迟视频流、板载音频管线、摄像头采集与微显示屏驱动，为社区提供了一套真正自主可控的硬件级原型参考。

---

## 4. [macedonga/visor](https://github.com/macedonga/visor)

> A de-metaified Meta Glasses client.

- ⭐ 总计 146 ⭐（本周增量未测得） ｜ Kotlin ｜ AGPL-3.0

面向 Ray-Ban Meta 与 Oakley 智能眼镜的去 Meta 化开源 Android 客户端，旨在彻底替代官方 Meta AI 配套应用。面向极度看重个人隐私且不想被 Meta 云端生态绑架的眼镜用户。它通过逆向蓝牙通信协议接管眼镜数据，保证眼镜拍摄的全部照片与音视频流仅保存在手机本地，并允许将默认的 "Hey Meta" 语音助手替换为用户自定义的云端或本地大模型。

---

## 5. [straff2002/OpenGlasses](https://github.com/straff2002/OpenGlasses)

> Making Meta Ray-ban / Oakley glasses smarter. Non-Meta Model selection, agentic features, smart guidance. 

- ⭐ 总计 127 ⭐（本周增量未测得） ｜ Swift ｜ 其他许可
- 主页：https://testflight.apple.com/join/1dcAytte

让 Ray-Ban Meta / Oakley 智能眼镜更加开放智能的 iOS 开源辅助工具（Avenkin），提供第一人称视觉下的私有化 Agent 体验。面向拥有智能眼镜并希望接入高智商前沿模型的苹果生态用户。它让用户能够自由切换 Claude、OpenAI 或端侧离线模型，利用手机算力对眼镜回传的场景图像进行第一人称多模态推理与智能指引，且个人记忆与对话历史全量本地加密保存。

---

## 6. [brilliantlabsAR/halo-firmware](https://github.com/brilliantlabsAR/halo-firmware)

> Firmware for Halo, Brilliant Labs' AI glasses — Zephyr RTOS on the Alif Balletto, with a Lua runtime for on-device apps and BLE OTA updates

- ⭐ 总计 64 ⭐（本周增量未测得） ｜ C ｜ 其他许可

Brilliant Labs 为其下一代轻量化 AI 眼镜 Halo 打造的开源嵌入式固件系统，基于 Zephyr RTOS 并运行于 Alif Balletto（Cortex-M55 + Ethos-U55 NPU）芯片架构。面向嵌入式工程师与可穿戴硬件极客。系统内置轻量级 Lua 运行时以支持端侧轻应用秒级开发，具备端侧硬件回声消除语音管线，并依托 MCUboot 实现了极低刷砖风险的全无线 BLE OTA 固件更新。
