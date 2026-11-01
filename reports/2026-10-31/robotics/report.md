# GitHub 周报：机器人（2026-10-25 – 2026-11-01）

本周机器人与具身智能赛道呈现出「软硬件双轮驱动、向物理智能底层纵深扎根」的强烈趋势。过去模型大多停留在数字仿真与静态逻辑中，而本周开源社区的触角已经伸展至从机械形态创造到端到端物理自进化的全链路：earthtojake/text-to-cad 让生成式 AI 直接接管机械结构与 DFM 可制造性检测；makerspet/oomwoo 与 KingKongRobotics/jumper 分别展示了开源家用扫地机器人与高动态多自由度仿生机器人的软硬件自制魅力；在智脑中枢与系统基建层，PhyAgentOS 提出了面向物理世界的递归自进化操作系统，RLinf 搭建起适配具身大模型的百倍加速强化学习训练底座，而 rerun-io 则稳固了多模态机器人空间传感器流的可视化基石。具身智能正快速完成从虚拟演示向真机硬件落地与自主闭环的技术蜕变。

---

## 1. [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)

> Design physical products with AI

- ⭐ 总计 24544 ⭐（本周增量未测得） ｜ Python ｜ MIT
- 主页：https://www.texttocad.dev

将生成式 AI 引入物理产品与机器人结构设计的开源 CAD 工作流插件，支持直接生成 STEP、GLB、STL 和 3MF 等工业级 3D 格式。面向机器人机械工程师、创客与智能硬件开发者。它不仅能将自然语言设计意图转化为精密的实体几何模型，还内置了面向制造的设计（DFM）合规性检查、自动化工程制图生成，并无缝对接主流 3D 打印与 CNC 数控加工服务。

---

## 2. [makerspet/oomwoo](https://github.com/makerspet/oomwoo)

> Open-source vacuum robot cleaner

- ⭐ 总计 12906 ⭐（本周增量未测得） ｜ Python ｜ Apache-2.0
- 主页：https://oomwoo.com

一套完全开源、支持用户纯手工 DIY 自制的家用扫地机器人全栈项目，基于树莓派、ESP32、Arduino 与 ROS 2 架构打造。面向机器人硬件爱好者、ROS 开发者与开源创客。它利用消费级低成本 2D 激光雷达实现全屋 SLAM 建图与自主路径规划，所有 3D 结构件均支持家用 3D 打印机制造，并能完全无缝接入 Home Assistant 实现本地局域网无云化私密控制。

---

## 3. [RLinf/RLinf](https://github.com/RLinf/RLinf)

> RLinf: Reinforcement Learning Infrastructure for Embodied and Agentic AI

- ⭐ 总计 5561 ⭐（本周增量未测得） ｜ Python ｜ Apache-2.0
- 主页：https://rlinf.readthedocs.io/en/latest/

专为具身智能（Embodied AI）与决策智能体打造的高性能分布式强化学习系统基础设施，已开源学术论文与完整工程代码。面向机器人学习研究员、运动控制算法工程师与具身大模型团队。它针对多任务机械臂抓取、双足人形机器人步态运动等复杂连续控制场景进行了底层并行仿真与梯度更新的系统级加速，打通了从物理模拟到真机部署的端到端训练闭环。

---

## 4. [PhyAgentOS/PhyAgentOS-core](https://github.com/PhyAgentOS/PhyAgentOS-core)

> PhyAgentOS is a Recursive Self-Improving (RSI)  physical agent operating system that enables agents to recursively self-improve through agentic workflows.

- ⭐ 总计 2991 ⭐（本周增量未测得） ｜ Python ｜ MIT
- 主页：https://phy-agent-os.x-era.com/

专为物理实体智能体打造的递归自进化（Recursive Self-Improving, RSI）操作系统内核，致力于让机器人在物理交互中持续自我迭代。面向具身智能研发团队与自主机器人系统架构师。它通过模块化的 Agent 工作流连接机器人感知、决策、执行与环境反馈，在遇到未知物理接触或任务失败时能自主反思、修正动作策略并优化底层驱动，探索物理世界的自监督持续演进。

---

## 5. [KingKongRobotics/jumper](https://github.com/KingKongRobotics/jumper)

> 🦀 Jumper — an crab robot.

- ⭐ 总计 3023 ⭐（本周增量未测得） ｜ Python ｜ Apache-2.0
- 主页：https://kingkong.tech/jumper

拥有 22 个活动自由度的开源仿生跳跃机械蟹机器人项目，包含完整的硬件结构图纸、步态控制固件与 AI 协同工具套件。面向仿生机器人研究者、动态运动控制工程师与高校实验室。它突破了传统多足机器人仅能缓慢爬行的限制，通过高爆发关节电机与弹力蓄能机构实现了敏捷的跳跃、全向翻滚与崎岖地形跨越，并支持用 AI 辅助外观配色与动作模态设计。

---

## 6. [rerun-io/rerun](https://github.com/rerun-io/rerun)

> Visualize, query, and stream to train on multimodal robotics data.

- ⭐ 总计 11675 ⭐（本周增量未测得） ｜ Rust ｜ Apache-2.0
- 主页：https://rerun.io/

专为具身智能与物理 AI 设计的多模态机器人空间数据可视化与时空查询引擎，使用 Rust 编写核心并提供 Python/C++ 原生接口。面向自动驾驶算法团队、机器人感知工程师与物理 AI 科学家。它能以极高带宽无损流式接收并同步回放机器人运行中的激光雷达点云、深度图像、关节变换（TF 树）与传感器张量流，是机器人仿真验证与具身大模型真机数据采集排查的顶级生产力利器。
