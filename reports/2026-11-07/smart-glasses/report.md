# GitHub 周报：AI 智能眼镜（2026-11-01 – 2026-11-08）

本周 AI 智能眼镜与穿戴赛道呈现出「全栈自主开源、底层操作系统统一与隐私防御对抗」的三维博弈态势。随着以 Ray-Ban Meta 为代表的商业拍摄眼镜普及，开源社区不仅在积极构建更开放透明的替代方案，也涌现出对隐私滥用的硬核技术反制：BasedHardware/omi 从电路原理图到前后端全面开放，构建起去中心化的随身 AI 挂件生态；MentraOS 则志在成为跨硬件品牌的标准眼镜操作系统，破除厂商私有协议壁垒；DresdenGman 以极致低至 35 美元的硬件方案让视障导航眼镜走向人人可复现的公益普惠；而在隐私防御与模型主权一侧，yjeanrenaud/yj_nearbyglasses 首次推出针对周围偷拍眼镜的被动蓝牙探测预警工具，Sentient 与 open-wearables 则坚守数据全本地私有化与本地模型驱动。智能眼镜生态正在科技巨头的商业阴影之外，迅速构建起兼顾开放自由、身心健康与隐私保护的完整民间开源版图。

---

## 1. [BasedHardware/omi](https://github.com/BasedHardware/omi)

> AI that sees your screen, listens to your conversations and tells you what to do

- ⭐ 总计 13917 ⭐（本周增量未测得） ｜ Python ｜ MIT
- 主页：https://omi.me

全栈开源的 AI 可穿戴设备与“第二大脑”软硬件平台，通过随身挂件及跨平台客户端实时捕获环境音频与屏幕画面，在后台自动完成多模态转录、情境摘要与记忆问答。面向渴望建立全天候数字化记忆库的极客用户与可穿戴 AI 开发者。相比闭源且依赖中心化云端的商业 AI 硬件，它从 PCB 原理图、嵌入式固件到前后端代码全链路采用 MIT 协议开源，支持用户 100% 私有化部署。

---

## 2. [yjeanrenaud/yj_nearbyglasses](https://github.com/yjeanrenaud/yj_nearbyglasses)

> attempting to detect smart glasses nearby and warn you

- ⭐ 总计 2593 ⭐（本周增量未测得） ｜ Kotlin ｜ AGPL-3.0

一款反向探测附近智能拍摄眼镜的移动端隐私防御应用，通过监听周围低功耗蓝牙（BLE）广播中的特定厂商特征码（如 Meta、Snap 等）实时向用户发出防偷拍预警。面向注重公共场所人身隐私、担忧被隐蔽拍摄或未经授权录制的普通大众。它跳出穿戴硬件本身的开发思维，以技术对抗技术扮演隐私“反制者”，全程离线运行且不收集任何数据，填补了针对消费级录制眼镜的被动防御工具空白。

---

## 3. [the-momentum/open-wearables](https://github.com/the-momentum/open-wearables)

> Self-hosted platform to unify wearable health data through one AI-ready API.

- ⭐ 总计 2767 ⭐（本周增量未测得） ｜ Python ｜ MIT
- 主页：https://docs.openwearables.io

开源、可自托管的可穿戴与健康设备数据中台，通过标准化的数据模型与统一 REST API，聚合对接 Garmin、Oura、Apple Health 等多品牌硬件数据。主要面向数字医疗产品、远程患者监控团队以及需要打通各类穿戴式生理数据的开发者。相比商业数据聚合 SaaS，它支持完全私有化部署以确保敏感健康数据合规，并原生内置了供大模型和智能体直接查询的 MCP 服务。

---

## 4. [Mentra-Community/MentraOS](https://github.com/Mentra-Community/MentraOS)

> MentraOS is the leading smart glasses OS. See live captions, stream your view, talk to AI, and capture photos hands-free on compatible glasses.

- ⭐ 总计 2405 ⭐（本周增量未测得） ｜ TypeScript ｜ Apache-2.0
- 主页：https://Mentraglass.com

开源、跨硬件的智能眼镜操作系统，统一抽象了设备配对、音视频低延迟串流与轻量级小程序（Miniapp）运行环境。主要面向智能眼镜应用开发者与穿戴硬件团队，用于快速开发跨品牌的随身生活助手与 AI 视觉应用。相比各厂商封闭碎片化的 SDK，它采用 Apache 2.0 开源协议并已兼容 Even Realities、Vuzix 等多种主流设备，真正实现了“一次开发、跨眼镜通用”。

---

## 5. [existence-master/Sentient](https://github.com/existence-master/Sentient)

> Your personal AI assistant, running on your own computer. Long-running tasks, real memory, proactive help, voice, phones and smart glasses. Any model, local or cloud. No account.

- ⭐ 总计 719 ⭐（本周增量未测得） ｜ Python ｜ NOASSERTION
- 主页：https://existence.technology/sentient

本地优先的开源个人智能体系统，支持通过开放协议直接接入智能眼镜与手机，提供随身免提语音、拍照视觉理解与长程任务自动化。面向注重数据隐私的个人用户与可穿戴 AI 创客，适用于全天候随身助理、情境感知问答与无人值守工作流。相比依赖云端大厂的闭源方案，它支持完全基于本地模型推理与自愈式记忆整理，并提供了开放的可穿戴设备通信协议与参考眼镜固件。

---

## 6. [DresdenGman/AIGlasses_for_navigation](https://github.com/DresdenGman/AIGlasses_for_navigation)

> Open-source AI navigation glasses under $35 — they say what they see, and say 'uncertain' instead of guessing. Safety-first, printable enclosure, community build kit.

- ⭐ 总计 298 ⭐（本周增量未测得） ｜ Python ｜ MIT
- 主页：https://oercommons.org/courses/low-cost-ai-navigation-glasses-bilingual-build-guide-for-assistive-makers

专为视障与低视力人群打造的开源 AI 导航眼镜项目，整合了可 3D 打印的轻量外壳与端到端实时路况视觉引导算法。面向盲人群体日常户外行走、过街识别与障碍物规避场景，也可供助残公益团队及创客二次开发。相比动辄数千美元的商用辅助设备，其整机硬件成本低于 35 美元，且算法核心遵循“宁可报告不确定、绝不盲目下指令”的安全底线原则。
