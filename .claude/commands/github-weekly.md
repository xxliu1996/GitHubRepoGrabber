---
description: 抓取过去一周 GitHub 上四个赛道的热门项目，各生成一份周报，并重建 GitHub Pages 站点
argument-hint: [YYYY-MM-DD 可选，默认今天]
---

生成本周的 GitHub 周报。**四个主题各一份**，然后重建网站。

**第 0 步：定位仓库根目录 `<ROOT>`**（本地和云端 sandbox 路径不同，必须先确定）：

```bash
if [ -d /Users/xingxingliu/Projects/CluadeProjects/GitHubRepoGrabber/scripts ]; then
  echo /Users/xingxingliu/Projects/CluadeProjects/GitHubRepoGrabber
else
  git rev-parse --show-toplevel
fi
```

后续所有路径都以 `<ROOT>` 为基准，不要写死绝对路径。

**重要：无条件重新生成。** 如果 `<ROOT>/reports/<DATE>/` 已经存在，**照样从第 1 步开始全部重跑并覆盖**，不要因为"文件已存在"就跳过、也不要反问用户要不要重做。定时任务是无人值守的，静默跳过会伪装成成功。

约定：
- `<DATE>` = `$ARGUMENTS`，为空就用今天（`date +%F`）
- 四个主题 `<THEME>`：`ai-agent`、`ar-vr`、`smart-glasses`、`robotics`
- 本周产物落在 `<ROOT>/reports/<DATE>/<THEME>/`，每个主题目录里两个文件：`raw.json`、`report.md`

各主题的收录目标（口径写在 `config/topics.json` 的 `pick` 字段，以那里为准）：

| 主题 | 标题 | 收录 |
|---|---|---|
| `ai-agent` | AI / Agent | 10 个 |
| `ar-vr` | AR / VR | 6 个 |
| `smart-glasses` | AI 智能眼镜 | 6 个 |
| `robotics` | 机器人 | 6 个 |

---

## 1. 抓数据（四个主题依次跑）

```bash
cd <ROOT> && for T in ai-agent ar-vr smart-glasses robotics; do
  python3 scripts/fetch_trending.py --theme "$T" --out "reports/<DATE>/$T/raw.json" > /dev/null
done
```

- 脚本纯标准库，不需要 venv。四个主题合计约 3–6 分钟。
- **把 stderr 的 `[grab]` / `WARN:` 日志展示给用户**。如果出现 `parsed 0 repos - markup may have changed`，说明 GitHub 改版了，要先修 `scripts/fetch_trending.py` 里的正则再继续，不要拿残缺数据往下走。
- 某个主题退出码为 2，表示这周该赛道合格项目太少。**这不算整体失败**：跳过那个主题（不写它的 `report.md`），继续做其余三个，最后在汇报里说明哪个主题本周没出报告。
- 如果环境里有 `GITHUB_TOKEN`，脚本会自动用上（限额从 60/小时 提到 5000/小时）。

## 2. 每个主题选出最终名单

读 `reports/<DATE>/<THEME>/raw.json`（不大，可以直接 Read）。按上表的数量挑选，判断标准：

- 必须真的属于这个主题 —— 打分只是启发式，有漏网之鱼就手动剔掉。跨主题的项目（比如一个 VR 里的 AI agent）放进最贴切的那一份，**不要在两份报告里重复出现**。
- `source: "trending"` 的条目 `stars_this_week` 是 GitHub 实测的本周涨星数，优先。`source: "search"` 的只有 `stars_this_week_estimated`（用总星数除以仓库年龄估的），可信度低，写进周报时**不要说成"本周新增"**。
- 尽量覆盖不同子方向，不要一份报告里全是同一类工具。
- 明显的营销号仓库、纯 awesome-list、翻译 repo 直接跳过。
- **冷门主题宁缺毋滥**：`ar-vr` / `smart-glasses` / `robotics` 这三个赛道单周未必凑得满 6 个真正值得写的项目。凑不满就少写几个，在导语里说明"本周该赛道动静不大"，不要为了凑数把几十星的玩具项目写进去。

## 3. 并行子 agent 读 README

**不要**自己去 WebFetch 二十多个 README —— 原文一旦进主上下文就会一直占用后续所有轮次的 token。

在**同一条消息里并行发起**多个 Agent 调用（`subagent_type: general-purpose`，`run_in_background: false`），每个 agent 负责 3–4 个仓库，**一个 agent 只处理同一个主题的仓库**，方便后面对号入座。每个子 agent 的 prompt 里要写清：

- 仓库全名列表和对应的 `https://github.com/<full_name>` 链接
- 让它读 README（`https://api.github.com/repos/<full_name>/readme` 拿 base64 后解码，或直接 WebFetch 仓库主页）
- **明确要求：每个仓库只返回 2–3 句中文提炼** —— 这个项目做什么、给谁用、和同类比新在哪。不要复述 README、不要贴代码块、不要列安装步骤。
- 如果 README 读不到，就说明"读取失败"，不要瞎编。

子 agent 返回的是精简笔记，基于这些笔记写正文。

## 4. 写四份 `report.md`

每个主题写入 `reports/<DATE>/<THEME>/report.md`。**格式必须严格照抄下面的骨架** —— `scripts/build_site.py` 靠这个结构把 Markdown 转成网页，改了格式网站就会渲染错：

```markdown
# GitHub 周报：<主题标题>（<week_start> – <week_end>）

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

硬性要求：

- **H1 只有一行，紧跟着的段落就是导语**，建站脚本把导语渲染成高亮块。
- **每个项目的 H2 必须是 `## <序号>. [owner/repo](url)` 这个形式**，序号从 1 连续编号。建站脚本用这行正则提取项目清单，格式不对网站上就显示成 0 个项目。
- 只有 `source: "trending"` 的才写"本周 +N"。`search` 来源的写成"总计 N ⭐（本周增量未测得）"。
- 每个链接都必须是 `raw.json` 里的 `html_url`，不要手拼。
- 导语要针对**这个主题**写，四份导语不要互相抄。

## 5. 重建网站

```bash
cd <ROOT> && python3 scripts/build_site.py
```

它会清空并重建 `docs/`（GitHub Pages 的发布目录）：首页放最近三个月、`archive.html` 放全部历史、每篇报告一个 `docs/r/<DATE>-<THEME>.html`，主题筛选是纯前端的。

跑完检查一下 `docs/data/reports.json` 里本周四条记录的 `count` 字段：如果哪条是 0，说明那份 `report.md` 的 H2 格式写错了，回第 4 步修，别放着不管。

## 6. 提交

```bash
cd <ROOT> && git add reports/<DATE> docs && \
git commit -m "Weekly GitHub digest: <DATE>"
```

然后 `git push`（远端是 `origin main`）。push 失败就报告错误，不要吞掉 —— 不 push 网站就不会更新。

## 7. 汇报

告诉用户：

- 四个主题各自的 `report.md` 路径，以及哪个主题本周没出（如果有）
- 每个主题收录的项目名单（一行一个，带涨星数）
- 网站地址：https://xxliu1996.github.io/GitHubRepoGrabber/
