# GitHub 周报：AI 智能眼镜（2026-10-04 – 2026-10-11）

智能眼镜仍是早期赛道，本周没有单周爆发式涨星的项目，上榜条目的星标均来自搜索估算、不代表"本周新增"，但方向感越来越清晰。最突出的共性是"抹平碎片化"：无论是 MentraOS 的跨设备操作系统，还是港科大的 xg-glass-sdk，都在用统一抽象层把 Rokid、Even Realities、Brilliant Labs、Meta Ray-Ban 等各家互不兼容的 SDK 收敛成一套接口——厂商各自为政的局面正催生一层开源中间件。第二条线是"把闭源眼镜盘活"：OpenVision、OpenGlasses 这类项目绕过原厂限制，给 Meta Ray-Ban 接上可自选、可离线的 AI 后端。第三条线则是记忆与感知的研究化，LightMem-Ego、omi 把第一人称视角的日常变成可问答的长期记忆。隐私自控、端侧推理、零 API 成本是这批项目反复强调的卖点。

---

## 1. [Mentra-Community/MentraOS](https://github.com/Mentra-Community/MentraOS)

> MentraOS is the leading smart glasses OS. See live captions, stream your view, talk to AI, and capture photos hands-free on compatible glasses.

- ⭐ 总计 2381 ⭐（本周增量未测得）｜ TypeScript ｜ Apache-2.0
- 主页：https://Mentraglass.com

一套开源智能眼镜操作系统，核心卖点是"一次开发、跨多款眼镜运行"——替开发者封装配对、连接、数据流和硬件访问，支持 Mentra Live、Even Realities G1/G2、Vuzix Z100 等多家设备，并配有应用商店和开发者控制台。相比各厂碎片化 SDK，它用统一抽象层加完全开源来换取跨设备兼容、隐私与可控性。

---

## 2. [hkust-spark/xg-glass-sdk](https://github.com/hkust-spark/xg-glass-sdk)

> One API for smart-glasses apps - camera, mic, display, audio - across Rokid, Meta Ray-Ban, Brilliant Labs Frame, RayNeo, Even Realities G1, INMO, Omi, and a simulator. Android, iOS, and CLI

- ⭐ 总计 46 ⭐（本周增量未测得）｜ Kotlin ｜ Apache-2.0
- 主页：https://xg.glass

港科大团队做的智能眼镜应用开发库，把各家眼镜 SDK 的差异收敛成四个通用接口（摄像头、麦克风、显示、音频），同一份代码无需改动即可跑在 Rokid、RayNeo、Brilliant Labs Frame、INMO、Even Realities 等设备或模拟器上。与 MentraOS 都主打"一次编写跨设备"，但它更偏轻量 SDK/库形态，并内置模拟器以便没有真机时也能开发。

---

## 3. [brilliantlabsAR/halo-firmware](https://github.com/brilliantlabsAR/halo-firmware)

> Firmware for Halo, Brilliant Labs' AI glasses — Zephyr RTOS on the Alif Balletto, with a Lua runtime for on-device apps and BLE OTA updates

- ⭐ 总计 56 ⭐（本周增量未测得）｜ C ｜ NOASSERTION

Brilliant Labs AI 眼镜 Halo 的开源固件，基于 Zephyr RTOS 跑在 Alif Balletto B1（Cortex-M55 + BLE 5.3 + Ethos-U55 NPU）上，带 Lua 运行时、端侧回声消除语音管线、MIPI-DSI 显示和 BLE OTA 升级。最大亮点是普通用户无需数据线、开发套件或厂商工具就能自行编译固件并通过 OTA 刷入，还用 MCUboot 的一次性测试启动/自动回滚做安全兜底，把"自制固件"做成了官方支持的工作流。

---

## 4. [rayl15/OpenVision](https://github.com/rayl15/OpenVision)

> Open-source iOS app connecting Meta Ray-Ban smart glasses to AI — 5 backends (on-device MLX models, Apple Intelligence, OpenAI, Gemini Live, OpenClaw), on-device neural voice, face recognition & live web search.

- ⭐ 总计 159 ⭐（本周增量未测得）｜ Swift ｜ MIT

面向 Meta Ray-Ban 眼镜用户的开源 iOS 应用，把眼镜拍到的画面和语音接入 AI 助手，做翻译、购物比价、识物、免手操作等。最大卖点是同时支持多种后端——既可接 Gemini/OpenAI/Grok 等云端模型，也能用 Apple MLX、Apple Intelligence 在手机上完全离线运行（含离线视频问答），强调隐私自控与零 API 成本的灵活切换。

---

## 5. [zjunlp/LightMem-Ego](https://github.com/zjunlp/LightMem-Ego)

> [EMNLP 2026] LightMem-Ego: Your AI Memory for Everyday Life

- ⭐ 总计 110 ⭐（本周增量未测得）｜ Python ｜ MIT
- 主页：https://lightmem-ego.zjukg.cn/

浙大 NLP 组推出的开源、可自托管多模态记忆系统，面向智能眼镜和手机，把第一人称视角的日常经历变成可追溯、可问答的长期记忆。由已入选 EMNLP 2026 Findings 的 EM²Mem 事件中心记忆引擎驱动，在 Video-MME、Ego-R1、EgoLifeQA 等基准上更优且单次查询快约 4.67 倍，并提供论文、浏览器演示和眼镜端 APK。

---

## 6. [BasedHardware/omi](https://github.com/BasedHardware/omi)

> AI that sees your screen, listens to your conversations and tells you what to do

- ⭐ 总计 13684 ⭐（本周增量未测得）｜ Python ｜ MIT
- 主页：https://omi.me

面向个人与专业人士的完全开源"第二大脑"，在桌面、手机和可穿戴设备上实时转录你看到和听到的内容，自动生成摘要、待办，并提供能记住一切的 AI 对话。差异化在于跨端全覆盖的软硬件一体方案（含可穿戴设备、BLE 接入和开源云后端），且主打极简上手——一条命令连云端即可运行。
