# GitHub 周报：机器人（2026-10-19 – 2026-10-26）

本周机器人赛道没有项目登上 Trending，入选项目都来自 topic 搜索，星数为总量，本周增量未测得，整体动静不大，只选出五个。从这几个项目看，「大模型驱动」正在从高层规划往下渗透：Jumper 用 AI 编程助手一句话训练螃蟹机器人的步态，PhyAgentOS 让 Agent 自己验证任务、失败后重新规划，并把经验沉淀成技能。支撑这些上层玩法的，依然是 MuJoCo 这类仿真底座、openpilot 这样已在真车上跑了多年的开源系统，以及 PythonRobotics 这种经典算法教材。上层换得快，底层几乎没变。

---

## 1. [KingKongRobotics/jumper](https://github.com/KingKongRobotics/jumper)

> 🦀 Jumper — an crab robot.

- ⭐ 总计 2889 ⭐（本周增量未测得） ｜ Python ｜ Apache-2.0
- 主页：https://kingkong.tech/jumper

22 自由度螃蟹机器人 Jumper 的配套 AI 工具包，可以设计外观、训练行走、跳跃、抓取、跳舞等动作，也能搭建仿真场景，面向机器人爱好者、创客和强化学习入门者。它的新意在于整个流程由 AI 编程助手驱动，一句话就能完成。底层基于 mjlab、rsl_rl 和 MuJoCo 训练，产出的动作、外观、场景分别打包成 .app、.skin、.map，大幅降低了足式机器人做内容的门槛。

---

## 2. [PhyAgentOS/PhyAgentOS-core](https://github.com/PhyAgentOS/PhyAgentOS-core)

> PhyAgentOS is a Recursive Self-Improving (RSI)  physical agent operating system that enables agents to recursively self-improve through agentic workflows.

- ⭐ 总计 2978 ⭐（本周增量未测得） ｜ Python ｜ MIT
- 主页：https://phy-agent-os.x-era.com/

面向具身智能体的「递归自我改进」框架，把大模型的认知规划、实体执行和任务验证串成闭环，适合要把大模型或动作模型接到真实或仿真机器人上的研究者。和一般机器人 Agent 框架相比，它会根据观测验证任务是否真的完成，失败时在限定次数内重新规划。验证过的经验会沉淀成带版本的技能供以后复用，规划和具体机器人的对接也是分开的。

---

## 3. [commaai/openpilot](https://github.com/commaai/openpilot)

> openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars.

- ⭐ 总计 63992 ⭐（本周增量未测得） ｜ Python ｜ MIT
- 主页：https://comma.ai/openpilot

comma.ai 的开源「机器人操作系统」，目前主要用途是给 300 多款量产车升级驾驶辅助，需要配合 comma 的设备使用，面向车主和自动驾驶开发者。它是少有的在大量真实车辆上落地的开源端到端驾驶系统，遵循 ISO 26262 指南，安全约束由独立的 C 代码（panda）强制执行。对研究「从仿真到真车」的人来说，它是最好的现成参照。

---

## 4. [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)

> Multi-Joint dynamics with Contact. A general purpose physics simulator.

- ⭐ 总计 15879 ⭐（本周增量未测得） ｜ C++ ｜ Apache-2.0
- 主页：https://mujoco.org

DeepMind 维护的通用物理引擎，专门快速、准确地模拟多关节结构与环境之间的接触，是机器人和强化学习研究的事实标准之一。和 Gazebo、PyBullet 相比，它的 JAX 分支 MJX 能在 GPU/TPU 上大规模并行仿真，并支持可微物理。它还新增了用代码编辑模型的 mjSpec 和多线程批量仿真。本期的 Jumper 等项目就构建在它之上。

---

## 5. [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)

> Python sample codes and textbook for robotics algorithms.

- ⭐ 总计 30803 ⭐（本周增量未测得） ｜ Python ｜ 其他许可
- 主页：https://atsushisakai.github.io/PythonRobotics/

用 Python 写的经典机器人算法合集，配有在线教材，覆盖定位、SLAM、路径规划与跟踪、机械臂、无人机和双足机器人，面向学习机器人算法的学生和工程师。和 ROS、OMPL 这类工程框架不同，它只依赖 NumPy、SciPy 等少数库，每个算法一个能直接运行、带动画的脚本，并附数学推导，是入门和查阅算法的首选读物。
