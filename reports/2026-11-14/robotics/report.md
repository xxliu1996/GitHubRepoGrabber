# GitHub 周报：机器人（2026-11-08 – 2026-11-15）

本周机器人与具身智能领域呈现出「大规模 GPU 物理仿真底座重构」与「消费级低成本开源硬件繁荣」的双向共振态势。在顶层基础设施与具身策略训练层面，产业界与学术界正加速统一底层技术栈：Linux 基金会联手 Disney Research、DeepMind 与 NVIDIA 推出 GPU 物理仿真引擎 Newton，以可微计算与 MuJoCo Warp 后端重塑机器人动力学模拟；NVIDIA 官方推出 Isaac Lab 3.0，深度打通多物理后端与传感器仿真管线；RLinf 则为具身智能大模型（VLA）与强化学习交互搭建起分布式并行基础设施；Rerun 持续作为多模态感知流与传感器时空数据的统一可视化标准。而在底层开源硬件方面，去中心化与本地优先理念深植家庭场景：OOMWOO 带来了基于树莓派、ROS2 与 2D 激光雷达的全开源扫地机器人参考设计；芝麻机器人（Sesame Robot）则以低廉的 ESP32 芯片和舵机架构让微型四足机器狗真正走进创客桌面。

---

## 1. [newton-physics/newton](https://github.com/newton-physics/newton)

> An open-source, GPU-accelerated physics simulation engine built upon NVIDIA Warp, specifically targeting roboticists and simulation researchers.

- ⭐ 总计 5956 ⭐（本周增量未测得） ｜ Python ｜ Apache-2.0
- 主页：https://newton-physics.github.io/newton/stable/

由 Linux 基金会托管、联合 Disney Research、Google DeepMind 与 NVIDIA 共同发起的开源 GPU 加速物理仿真引擎。专为机器人研究者与物理仿真专家设计，旨在提供高吞吐、可微分且极具扩展性的通用动力学仿真底座。它基于 NVIDIA Warp 架构重构，原生支持 OpenUSD 场景标准并以 MuJoCo Warp 作为核心计算后端，支持大规模并行物理演化与快速算法迭代。

---

## 2. [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab)

> Unified framework for robot learning with multi-physics/renderer support

- ⭐ 总计 8647 ⭐（本周增量未测得） ｜ Python ｜ NOASSERTION
- 主页：https://isaac-sim.github.io/IsaacLab

NVIDIA 官方开源的下一代轻量化机器人强化学习与策略训练统一框架，最新 3.0 版本深度适配 Isaac Sim 6.2。面向需要在大规模虚拟场景中训练机械臂操作、双足步态与四足越障的具身智能算法工程师。它创新性地支持 Newton、OVPhysX 等多物理引擎与 RTX 传感器渲染管线，通过极高的 GPU 并行吞吐率大幅加速 Sim-to-Real（仿真到现实）的策略迁移。

---

## 3. [RLinf/RLinf](https://github.com/RLinf/RLinf)

> RLinf: Reinforcement Learning Infrastructure for Embodied and Agentic AI

- ⭐ 总计 5652 ⭐（本周增量未测得） ｜ Python ｜ Apache-2.0
- 主页：https://rlinf.org

专为具身智能与智能体系统设计的大规模强化学习训练基础设施（Reinforcement Learning Infrastructure）。面向从事视觉-语言-动作（VLA）多模态大模型微调与端到端机器人策略优化的学术与工业界研发团队。系统突破了传统强化学习框架在异步环境交互、分布式 Rollout 调度与长序列多模态 Token 处理上的吞吐瓶颈，为物理世界智能体提供高并发、高容错的分布式训练底座。

---

## 4. [makerspet/oomwoo](https://github.com/makerspet/oomwoo)

> Open-source vacuum robot cleaner

- ⭐ 总计 13099 ⭐（本周增量未测得） ｜ Python ｜ Apache-2.0
- 主页：https://oomwoo.com

完全开源且可由个人组装搭建的智能扫地机器人参考方案，整机依托树莓派、3D 打印结构件、Arduino 与 ROS2 构建。面向热爱 DIY 智能家居与移动机器人开发的创客及高校师生。它采用性价比极高的 2D 激光雷达实现全屋精准建图与自主 SLAM 路径规划，所有传感器数据与清扫任务均完全运行于家庭局域网与 Home Assistant 中，坚决杜绝商业扫地机频繁将家庭室内户型与视觉隐私上传云端的隐患。

---

## 5. [dorianborian/sesame-robot](https://github.com/dorianborian/sesame-robot)

> An open and affordable mini quadruped robot based on ESP32.

- ⭐ 总计 5069 ⭐（本周增量未测得） ｜ C ｜ Apache-2.0
- 主页：https://www.doriantodd.com/sesame

基于微控制器 ESP32 与低成本舵机构建的超高性价比微型四足开源机器狗（Sesame）。面向机器人初学者、高校机器人社团与嵌入式硬件爱好者。项目不仅完整开源了 3D 打印外壳模型与电路接线图，还提供经过精心调校的反向运动学（IK）运动控制算法与步态生成固件，配合详尽的手把手视频组装教程，让百元级低成本机器人开发成为现实。

---

## 6. [rerun-io/rerun](https://github.com/rerun-io/rerun)

> Visualize, query, and stream to train on multimodal robotics data.

- ⭐ 总计 11798 ⭐（本周增量未测得） ｜ Rust ｜ Apache-2.0
- 主页：https://rerun.io/

机器人学与计算机视觉领域被广泛采用的多模态时空数据可视化与流式回放引擎，采用 Rust 编写具备极高性能。面向处理机械臂轨迹、多目立体视觉、LiDAR 点云与深度图对齐的具身智能开发者。它能够以微秒级延迟将传感器实时流与内部张量数据同步记录并在三维交互界面中流式呈现，支持灵活的时间轴拖拽与跨模态查询，是机器人算法调试与训练数据集检查的得力利器。
