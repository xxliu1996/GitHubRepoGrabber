---
description: 抓取过去一周 GitHub 上最火的 LLM/Agent 项目，生成周报、小红书文案和配图 prompt
argument-hint: [YYYY-MM-DD 可选，默认今天]
---

生成本周的 GitHub LLM/Agent 项目周报。

**第 0 步：定位仓库根目录 `<ROOT>`**（本地和云端 sandbox 路径不同，必须先确定）：

```bash
if [ -d /Users/xingxingliu/Projects/CluadeProjects/GitHubRepoGrabber/scripts ]; then
  echo /Users/xingxingliu/Projects/CluadeProjects/GitHubRepoGrabber
else
  git rev-parse --show-toplevel
fi
```

后续所有路径都以 `<ROOT>` 为基准，不要写死绝对路径。

**重要：无条件重新生成。** 如果 `<ROOT>/reports/<DATE>/` 已经存在，**照样从第 1 步开始全部重跑并覆盖**，不要因为"文件已存在"就跳过、也不要反问用户要不要重做。定时任务是无人值守的，静默跳过会伪装成成功。四个文件每次都必须是本次运行新写的。

约定：`<DATE>` = `$ARGUMENTS`，如果为空就用今天的日期（`date +%F`）。本周产物全部落在 `<ROOT>/reports/<DATE>/`。

---

## 1. 抓数据

```bash
cd <ROOT> && \
python3 scripts/fetch_trending.py --limit 20 --out reports/<DATE>/raw.json > /dev/null
```

- 脚本纯标准库，不需要 venv，约 30–60 秒。
- **把 stderr 的 `[grab]` / `WARN:` 日志展示给用户**。如果出现 `parsed 0 repos - markup may have changed`，说明 GitHub 改版了，要先修 `scripts/fetch_trending.py` 里的正则再继续，不要拿残缺数据往下走。
- 如果环境里有 `GITHUB_TOKEN`，脚本会自动用上（限额从 60/小时 提到 5000/小时）。

## 2. 选出最终 10 个

读 `reports/<DATE>/raw.json`（这个文件不大，可以直接 Read）。

从 20 个候选里挑 **10 个**，判断标准：
- 必须真的和 LLM / Agent / Agent Skills / MCP / RAG 相关 —— 打分只是启发式，有漏网之鱼就手动剔掉。
- `source: "trending"` 的条目 `stars_this_week` 是 GitHub 实测的本周涨星数，优先。`source: "search"` 的只有 `stars_this_week_estimated`（用总星数除以仓库年龄估的），可信度低，写进周报时不要说成"本周新增"。
- 尽量让 10 个覆盖不同子方向（编码 Agent、Agent Skills、推理/网关、RAG、评测、治理……），不要 10 个全是 Claude Code 插件。
- 明显的营销号仓库、纯 awesome-list、翻译repo 直接跳过。

## 3. 并行子 agent 读 README

**不要**自己去 WebFetch 十个 README —— 原文一旦进主上下文就会一直占用后续所有轮次的 token。

在**同一条消息里并行发起**多个 Agent 调用（`subagent_type: general-purpose`，`run_in_background: false`），每个 agent 负责 2–3 个仓库。每个子 agent 的 prompt 里要写清：

- 仓库全名列表和对应的 `https://github.com/<full_name>` 链接
- 让它读 README（`https://api.github.com/repos/<full_name>/readme` 拿 base64 后解码，或直接 WebFetch 仓库主页）
- **明确要求：每个仓库只返回 2–3 句中文提炼** —— 这个项目做什么、给谁用、和同类比新在哪。不要复述 README、不要贴代码块、不要列安装步骤。
- 如果 README 读不到，就说明"读取失败"，不要瞎编。

子 agent 返回的是精简笔记，我基于这些笔记写正文。

## 4. 写 `report.md`

写入 `reports/<DATE>/report.md`：

```markdown
# GitHub 周报：LLM / Agent（<week_start> – <week_end>）

<一段导语：本周这批项目的共同趋势是什么。要有观点，别写成"以下是本周热门项目"这种废话。>

---

## 1. [owner/repo](https://github.com/owner/repo)

> <一句话原始描述（英文原文即可）>

- ⭐ 本周 +<stars_this_week> ｜ 总计 <stars> ｜ <language> ｜ <license>
- 主页：<homepage，没有就省略这行>

<子 agent 提炼的 2–3 句中文说明>

---

## 2. ...
```

注意：
- 只有 `source: "trending"` 的才写"本周 +N"。`search` 来源的写成"总计 N ⭐（本周增量未测得）"。
- 每个链接都必须是 `raw.json` 里的 `html_url`，不要手拼。

## 5. 写 `rednote.md`（小红书文案）

写入 `reports/<DATE>/rednote.md`。这是要直接复制去发布的，所以**只写正文，不要加"以下是文案"之类的元话术**。

结构：

```markdown
## 标题

<带 emoji 的钩子标题，例如「本周 GitHub 最火的 10 个 Agent 项目 🔥」>

## 正文

<2–3 句开场，说清这是什么、为什么值得存>

1️⃣ **owner/repo**
<1–2 句中文说明，讲人话，说清"能帮你干什么">
🔗 github.com/owner/repo

2️⃣ ...

<结尾一句互动引导，例如「你在用哪个？评论区聊聊」>

## 话题标签

#GitHub #AI编程 #Agent #大模型 #程序员 #开源项目 #ClaudeCode #AI工具
```

硬性要求：
- **中文为主，不要中英混杂的句子。** 仓库名、链接保持英文原样，但描述性文字必须是通顺中文（不要写「这个 repo 提供了 unified 的 API gateway」这种）。
- 每条 2–3 行，小红书是手机端阅读，长段落没人看。
- 不要用 Markdown 的 `**加粗**` 以外的复杂语法（小红书不渲染），列表就用 1️⃣2️⃣3️⃣ 这种 emoji 数字。
- 链接写成 `github.com/xxx` 不带 `https://`（小红书会吞掉带协议头的链接）。
- **字数是硬约束，必须用脚本验证，不能靠估。** 写完立刻运行：

  ```bash
  python3 <ROOT>/scripts/check_rednote.py <ROOT>/reports/<DATE>/rednote.md
  ```

  它会检查标题 ≤20 字、正文 ≤1000 字、模板占位符是否残留、正文里有没有 `https://`。
  **只要它报 FAIL 就必须压缩重写再跑一遍，循环到 OK 为止**，不要交超限的稿子（实测过：不验证的话正文很容易写到 1600+ 字）。
  正文目标 800–950 字，给自己留余量——光 10 条链接就占掉约 340 字。

## 6. 写 `image-prompts.md`（配图 prompt）

先读 `<ROOT>/config/style.md`，取出三样东西：

1. **画幅** —— 「## 画幅」小节里的宽高比和像素建议
2. **参考图** —— 「## 参考图」小节里登记的文件路径和目标生成器（如果还是「待填写」，就在输出里写「暂无参考图」并提醒用户去登记）
3. **风格块** —— 「## 风格块」小节里第一个 ```text 代码块的**完整内容**，逐字使用，不要改写、不要翻译、不要"优化"
4. **补充约束** —— 如果「### 补充约束」小节存在，把它里面那个 ```text 代码块也一并追加到每条 prompt 末尾；小节被删掉了就跳过

参考图是**只传画风**用的（纸张质感、线条、配色），不负责构图。所以：风格块里如果有 `Composition` 之类描述构图的行，照抄没问题，但每条 prompt 必须自带 `Aspect ratio` 行和 3:4 竖版的构图描述，由后者说了算。

写入 `reports/<DATE>/image-prompts.md`，包含 **1 张封面 + 4 张内容卡**：

```markdown
# 配图 Prompt（<DATE>）

> 风格来源：`config/style.md`。改风格只改那个文件，不要改这里。
> 参考图：<路径>　→　**喂给图片生成器时请连同这张参考图一起提交**
> 目标生成器：<从 style.md 读到的>
> 画幅：3:4 竖版，1080 × 1440，四边留 8% 安全边距

---

## 封面

```text
Use case: xiaohongshu-cover
Aspect ratio: 3:4 vertical (1080x1440)
Primary request: <根据本周主题描述画面内容>
Chinese labels: <2–4 个短中文标签，通常是标题里的关键词>
<这里原样粘贴 style.md 风格块的完整内容>
```

## 内容卡 1：<主题>

```text
Use case: xiaohongshu-content-card
Aspect ratio: 3:4 vertical (1080x1440)
...
```
```

`Aspect ratio` 那行要出现在每一条 prompt 里，数值以 style.md 的「## 画幅」为准（用户改了那里就跟着改）。

4 张内容卡按本周项目的子方向分组（比如「编码 Agent」「Agent Skills」「模型网关」「RAG/知识库」），不是一个项目一张卡。

## 7. 提交

```bash
cd <ROOT> && \
git add reports/<DATE> && cd <ROOT> && \
git commit -m "Weekly GitHub LLM/agent digest: <DATE>"
```

如果配了 remote 就 `git push`；没配就跳过，不要报错。

## 8. 汇报

告诉用户：
- 四个文件的绝对路径
- 本周选出的 10 个项目名单（一行一个，带涨星数）
- 把 `rednote.md` 的正文完整展示出来，方便直接复制
