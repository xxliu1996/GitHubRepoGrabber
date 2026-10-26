# GitHub 周报：AI 智能眼镜（2026-10-19 – 2026-10-26）

本周智能眼镜赛道仍处早期，入选项目都来自 topic 搜索，星数为总量，本周增量未测得，合格项目只凑出五个。值得注意的是，讨论开始从「眼镜能做什么」转向「眼镜看到的东西归谁」。星数最高的新面孔 nearbyglasses 是一款反智能眼镜的隐私工具，能侦测附近有没有人戴着智能眼镜。与此同时，VModal 的推流 SDK、开源 AI 眼镜平台和 Spectacles 控制机器人的项目，都在把眼镜的第一视角画面接进后端视觉 AI 和实体设备。眼镜正在变成一个摄像头加传感器的入口，隐私边界的争论会越来越多。

---

## 1. [yjeanrenaud/yj_nearbyglasses](https://github.com/yjeanrenaud/yj_nearbyglasses)

> attempting to detect smart glasses nearby and warn you

- ⭐ 总计 2491 ⭐（本周增量未测得） ｜ Kotlin ｜ AGPL-3.0

开源 Android/iOS 应用，读取附近蓝牙 BLE 广播里的厂商 ID 来判断周围是否有人戴着智能眼镜，并发出提醒，面向担心被偷拍或被人脸识别的普通人。别的项目都在做眼镜本身，它反过来做「反眼镜」的隐私防护，不收集数据、没有遥测。作者坦言误报可能较多（比如把同厂商的 VR 头显当成眼镜），并提醒不要因此骚扰他人。

---

## 2. [v-modal/vmodal_sdk_smartglass](https://github.com/v-modal/vmodal_sdk_smartglass)

> SDK for Visual Memory Search with  Smart Glasses

- ⭐ 总计 360 ⭐（本周增量未测得） ｜ Rust ｜ 无许可证

VModal 推出的 Android SDK，把 Meta 智能眼镜（经由 Meta Wearables DAT）拍到的第一视角画面实时推流到自建接收端。它面向做远程专家协助、现场巡检和培训应用的开发者。比起自己拼凑推流方案，它用 Kotlin 封装接口、Rust 内核处理媒体，提供加密 SRT 传输、背压控制和自动重连。推流地址由后端签发且短期有效，账号凭证不必放在设备上。

---

## 3. [Iam5tillLearning/OpenSource-Ai-Glasses](https://github.com/Iam5tillLearning/OpenSource-Ai-Glasses)

> Open-source standalone AI glasses platform built on embedded Linux, with system-level customization, C/C++ SDK, RTSP video streaming, BLE, audio, camera, and optional display support.

- ⭐ 总计 297 ⭐（本周增量未测得） ｜ C ｜ Apache-2.0

基于嵌入式 Linux 和瑞芯微 RV1106B 的开源 AI 眼镜平台，开放了系统软件和应用栈，可以用自备开发板，也可以买官方套件，适合想从固件到应用全链路自研 AI 眼镜的嵌入式开发者。v0.7.0 新增了 Android 配套客户端、可直连云端视觉 AI 的 RTSP 视频流、BLE 文本通道和显示 SDK。项目仍属早期，README 自称文档完成度约 45%。

---

## 4. [V4C38/spectacles-dimensional-os](https://github.com/V4C38/spectacles-dimensional-os)

> Snap Spectacles AR integration with Dimensional OS - contoller for Unitree GO2 and G1 robots.

- ⭐ 总计 188 ⭐（本周增量未测得） ｜ TypeScript ｜ MIT

把 Snap Spectacles AR 眼镜当作实体机器人的操作界面：戴着眼镜就能导航、手动控制 Unitree Go2 四足或 G1 人形机器人，还能直接在真实空间里看到 LiDAR 等传感器数据。它面向研究 AR 加机器人交互的开发者。同类眼镜项目多半只做信息显示或 AI 助手，它用 AprilTag 把眼镜和机器人的坐标系对齐，让眼镜成为机器人的空间控制台，并提供基于 OpenAI 的 Agent 模式。

---

## 5. [BasedHardware/omi](https://github.com/BasedHardware/omi)

> AI that sees your screen, listens to your conversations and tells you what to do

- ⭐ 总计 13815 ⭐（本周增量未测得） ｜ Python ｜ MIT
- 主页：https://omi.me

完全开源的 AI「第二大脑」，记录屏幕内容和对话，实时转写，生成摘要和待办，再用一个记得你看过、听过一切的 AI 和你对话，可以在桌面、手机和可穿戴设备上使用。和闭源的 AI 记录挂件相比，它从固件、自制眼镜方案 Omi Glass 到后端和 SDK 全部开源，同一套记忆系统同时接入可穿戴设备和桌面端，已有应用生态和 30 万以上用户。
