# GitHub 周报：机器人（2026-10-24 – 2026-10-31）

本周机器人赛道最显著的脉搏是「物理 AI（Physical AI）从顶层算法向具身全栈体系纵深渗透」。具身智能的发展不再仅仅停留于上层端到端大模型的学术演示，而是深入到了全流程的基础设施再造：以 RLinf 为代表的大规模强化学习基建全面打通了从仿真到百台真实物理机器人集群的自主策略演化，被 Isaac Lab 和 PyTorch 生态深度集成；专为传感器时空流设计的 Rerun 成为多模态数据对齐与实时回放的事实标准；哈佛开源教材 CS249r 则系统化梳理了从 TinyML 到具身物理系统的系统工程范式。与此同时，在硬件载体与工程落地层面，从能直接生成可量产 STEP/STL 参数化装配体的 text-to-cad，到软硬件全开源、完全本地化运行的 ROS 2 激光扫地机 oomwoo，再到 22 自由度的仿生多足机器人 Jumper，开源力量正推动具身算法与物理机械世界的深度咬合。

---

## 1. [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)

> Design physical products with AI

- ⭐ 总计 24491 ⭐（本周增量未测得） ｜ Python ｜ MIT
- 主页：https://www.texttocad.dev

专为 AI Agent 设计的本地 3D 机械与物理产品 CAD 自动化生成工具，能够直接生成 STEP、STL、GLB 和 3MF 等标准工程文件。面向硬件创业者、机器人结构设计师与工业制造工程师。与只生成不可编辑网格（mesh）的传统 3D 生成模型不同，它利用局部确定性代码和几何内核输出具有精确公差、可直接导入 SolidWorks/Fusion360 或下发 3D 打印机的工业级参数化三维实体。

---

## 2. [makerspet/oomwoo](https://github.com/makerspet/oomwoo)

> Open-source vacuum robot cleaner

- ⭐ 总计 12899 ⭐（本周增量未测得） ｜ Python ｜ Apache-2.0
- 主页：https://oomwoo.com

由创客自主构建的完全开源智能扫地机器人完整软硬件项目（OOMWOO），基于树莓派、ESP32、Arduino 与 ROS 2 构建。面向机器人硬件爱好者、ROS 开发者与智能家居创客。它采用廉价 2D 激光雷达实现端侧自主 SLAM 构图与避障导航，全部机械结构均可 3D 打印，且所有数据与算法均运行于局域网本地，可无缝接入 Home Assistant，无需依赖任何商业云端。

---

## 3. [RLinf/RLinf](https://github.com/RLinf/RLinf)

> RLinf: Reinforcement Learning Infrastructure for Embodied and Agentic AI

- ⭐ 总计 5560 ⭐（本周增量未测得） ｜ Python ｜ Apache-2.0
- 主页：https://rlinf.readthedocs.io/en/latest/

面向具身智能（Embodied AI）与物理 Agent 的大规模强化学习训练基础设施，正式入选 PyTorch 官方生态并被 NVIDIA Isaac Lab 官方采纳。面向从事端到端机器人策略学习与 VLA（视觉-语言-动作）大模型训练的科研团队与工业界实验室。它不仅统一重构了多模态模型与异构机器人硬件驱动层，还提出了群体经验学习（CEL）与在线策略蒸馏算法，支持在几十台上百台真实物理机器人集群上实现无人工干预的自主策略进化。

---

## 4. [rerun-io/rerun](https://github.com/rerun-io/rerun)

> Visualize, query, and stream to train on multimodal robotics data.

- ⭐ 总计 11673 ⭐（本周增量未测得） ｜ Rust ｜ Apache-2.0
- 主页：https://rerun.io/

专为计算机视觉与机器人研发设计的超高性能多模态时空数据可视化与流式回放引擎，核心采用 Rust 编写。面向算法工程师、自动驾驶研发团队与具身智能研究员。它能够以极高吞吐量实时流式采集、同步对齐并三维渲染激光雷达点云、多路相机视频、IMU 姿态传感器以及神经网络张量预测，大幅简化了复杂机器人多传感器数据的联合调试与模型训练评估。

---

## 5. [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book)

> Machine Learning Systems: Foundations, Scaling, Agentic AI, and Physical AI (Vols I–IV) • Harvard CS249r | https://mlsysbook.ai

- ⭐ 总计 29749 ⭐（本周增量未测得） ｜ Python ｜ 其他许可
- 主页：https://mlsysbook.ai

哈佛大学边缘计算实验室开源的四卷本机器学习系统权威教材与课程体系（Harvard CS249r），系统性地串联起从基础算力、集群扩展到 Agent 与物理具身 AI（Physical AI）。面向深入研究机器人系统软硬件协同设计的学生、学者与系统架构师。它填补了业内缺乏端到端工程系统视角的空白，深入剖析了边缘计算设备上的微型机器学习（TinyML）、具身智能动作推理管线与实时计算拓扑。

---

## 6. [KingKongRobotics/jumper](https://github.com/KingKongRobotics/jumper)

> 🦀 Jumper — an crab robot.

- ⭐ 总计 3021 ⭐（本周增量未测得） ｜ Python ｜ Apache-2.0
- 主页：https://kingkong.tech/jumper

具备 22 个自由度的仿生多足螃蟹机器人硬件平台及其配套 AI 具身工具链（Jumper）。面向仿生多足动力学研究者、机器人创客与交互设计师。它打破了传统四足机器狗千篇一律的形态局限，提供了一整套基于大模型的自然语言生成外观色彩、步态动力学轨迹仿真和场景渲染管线，用户仅需一句话即可生成协调的肢体步态运动与皮肤材质。
