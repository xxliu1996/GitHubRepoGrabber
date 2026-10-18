# GitHub 周报：机器人（2026-10-11 – 2026-10-18）

本周机器人赛道的看点几乎都落在"具身智能的训练与数据管线"上：有开放权重的 VLA 大模型、把机器人当成一等资源的强化学习训练框架、能从经验里自我进化的物理智能体 OS，再加上仿真引擎和多模态数据可视化这两块长期底座。可以看出，开源社区正在把 LLM 时代那套"模型 + 训练基建 + 数据工具"的完整栈复刻到物理世界。另一端则是接地气的 DIY 硬件——一台全开源、可自己 3D 打印的扫地机器人提醒我们，机器人并非只有实验室叙事。本周来源均为 topic 搜索，星标为总量，涨星增量未实测。

---

## 1. [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)

> Multi-Joint dynamics with Contact. A general purpose physics simulator.

- ⭐ 总计 15733 ⭐（本周增量未测得）｜ C++ ｜ Apache-2.0
- 主页：https://mujoco.org

高性能物理仿真引擎，专注含接触的多关节动力学，可快速精确地模拟机器人和生物力学等铰接结构，提供 C API、Python 绑定和原生可视化 GUI。相比同类，它兼顾底层 C 的极致性能与 Python 的易用性，并通过基于 JAX 的 MuJoCo XLA 提供可微分物理与解析梯度，还能经 Unity 插件和 WebAssembly 跨平台运行，是具身智能训练的主力仿真器之一。

---

## 2. [makerspet/oomwoo](https://github.com/makerspet/oomwoo)

> Open-source vacuum robot cleaner

- ⭐ 总计 12060 ⭐（本周增量未测得）｜ Python ｜ Apache-2.0
- 主页：https://oomwoo.com

一台可自己动手搭建的开源家用扫地机器人，开放软件、固件与硬件设计，支持 2D LiDAR 建图、基于 ROS2 的自主导航，并接入 Home Assistant 做纯本地控制，面向 DIY 玩家、创客和机器人爱好者。与 Valetudo 等去云方案相比，它提供的是软硬件全开源、3D 打印模块化底盘、仿真先行（Gazebo）且追求"产品级"而非原型级的完整可造方案。

---

## 3. [rerun-io/rerun](https://github.com/rerun-io/rerun)

> Visualize, query, and stream to train on multimodal robotics data.

- ⭐ 总计 11608 ⭐（本周增量未测得）｜ Rust ｜ Apache-2.0
- 主页：https://rerun.io/

定位为"物理 AI 的数据层"，用于摄入、可视化、查询并流式处理图像、点云、时序、变换、视频等多模态传感器数据，自带实时同步渲染的查看器并支持 dataframe/SQL 查询，主要给机器人、计算机视觉和仿真方向做调试与分析。相比 RViz 等同类，它用专为多速率多模态设计的列式存储保留端到端数据关系，支持时间轴回放，还能把数据直接喂给模型训练而无需导出搬运。

---

## 4. [RLinf/RLinf](https://github.com/RLinf/RLinf)

> RLinf: Reinforcement Learning Infrastructure for Embodied and Agentic AI

- ⭐ 总计 5430 ⭐（本周增量未测得）｜ Python ｜ Apache-2.0
- 主页：https://rlinf.readthedocs.io/en/latest/

面向具身智能和智能体的开源强化学习训练框架，把分布式并行的复杂度隐藏起来，让 VLA 模型和机器人策略能跨多节点多 GPU 规模化训练，支持 PPO/GRPO/SAC 等算法。亮点在于把机器人当作与 GPU 同级的"一等资源"统一在线/离线训练，混合执行模式号称最高 2.43 倍吞吐，并跨 NVIDIA/AMD/华为昇腾等硬件、兼容 30+ 仿真器与 π₀、GR00T、OpenVLA 等多模型家族。

---

## 5. [PhyAgentOS/PhyAgentOS-core](https://github.com/PhyAgentOS/PhyAgentOS-core)

> PhyAgentOS is a Recursive Self-Improving (RSI) physical agent operating system that enables agents to recursively self-improve through agentic workflows.

- ⭐ 总计 2980 ⭐（本周增量未测得）｜ Python ｜ MIT
- 主页：https://phy-agent-os.x-era.com/

面向具身智能的"自我进化"智能体框架，把规划、物理执行与结果校验串成闭环，让机器人从成功经验中沉淀可复用的工作流和经验教训并持续精进，支持从仿真到真机、通用大模型推理与动作模型（如 π0.5）混合控制。相比同类，亮点在"受验证的经验驱动的递归自我改进"——带守护式晋升和修订历史，并把环境相关技能做成可版本化的独立模块。

---

## 6. [dexmal/opendm](https://github.com/dexmal/opendm)

> An Open-World Foundation Model for General-Purpose Embodied Intelligence.

- ⭐ 总计 2312 ⭐（本周增量未测得）｜ Python ｜ Apache-2.0

开源的视觉-语言-动作（VLA）机器人大模型 DM0.5 完整框架，提供权重、训练/推理脚本与评测流程，面向做具身操作的研究者与开发者，可在多种本体和平台上微调部署，并已对接 LeRobot 生态与 AgileX 等真机。相比同类，它专攻开放指令、长程任务、动态干扰和多本体控制，并在 RoboColiseum、LIBERO、RoboTwin2.0 等多个榜单上拿到领先成绩。
