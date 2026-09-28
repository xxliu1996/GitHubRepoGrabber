# GitHubRepoGrabber

每周抓一次 GitHub 上最火的开源项目，**四个赛道各出一份周报**，再编译成一个 GitHub Pages 静态站点。

| 主题 slug | 标题 | 收录 |
|---|---|---|
| `ai-agent` | AI / Agent | 10 个 |
| `ar-vr` | AR / VR | 6 个 |
| `smart-glasses` | AI 智能眼镜 | 6 个 |
| `robotics` | 机器人 | 6 个 |

站点：<https://xxliu1996.github.io/GitHubRepoGrabber/> —— 首页是最近三个月，`archive.html` 是全部历史，两页都能按主题筛选。

## 设计

沿用 `TwinCitiesEventNotification` 的分工：**脚本只负责确定性的抓取和排序，输出 JSON；文字由 agent 写。** 这样抓取逻辑可测试可复现，文案质量交给模型。

```
GitHubRepoGrabber/
├── config/
│   └── topics.json        # 四个主题各自的 topic / 关键词权重 / 门槛 —— 调选题方向改这里，不用改代码
├── scripts/
│   ├── fetch_trending.py  # 纯标准库，按 --theme 抓一个主题，JSON 打到 stdout
│   └── build_site.py      # 纯标准库，reports/ → docs/ 静态站
├── reports/
│   └── YYYY-MM-DD/
│       └── <theme>/
│           ├── raw.json     # 脚本原始输出，一并提交，便于复现
│           └── report.md    # 周报正文（build_site.py 靠它的结构渲染，格式别乱改）
└── docs/                  # GitHub Pages 发布目录，由 build_site.py 全量重建，不要手改
```

`docs/` 是**生成物**：`build_site.py` 每次跑都会先 `rmtree` 再重建，手动改的东西下一轮就没了。

## 用法

一条命令跑完整个流程：

```
/github-weekly            # 用今天的日期
/github-weekly 2026-07-30 # 指定日期
```

命令定义在 `/Users/xingxingliu/Projects/CluadeProjects/.claude/commands/github-weekly.md`。

只想看某个主题抓到什么、不生成正文：

```bash
python3 scripts/fetch_trending.py --list-themes
python3 scripts/fetch_trending.py --theme robotics | python3 -m json.tool | head -60
```

常用参数：`--theme <slug>`（必填），`--out <路径>` 同时落盘，`--limit N` 覆盖该主题的输出条数，`--enrich-pool N` 进入 API 富化的候选数（每个候选消耗 1 次 core 配额），`--week-of YYYY-MM-DD` 指定周锚点。不传 `--limit` / `--enrich-pool` / `--min-repos` 时一律用 `topics.json` 里该主题的值。

只重建网站（改了样式或删了某篇报告之后）：

```bash
python3 scripts/build_site.py
open docs/index.html
```

## 数据来源

1. **`github.com/trending?since=weekly`** —— GitHub 唯一公开真实"本周涨星数"的地方。全站页 + `topics.json` 里列出的各语种页，一共 6 个页面，约 100 个仓库。这是主来源。
2. **Search API** —— 按该主题的 `search_topics` 逐个查最近 7 天有推送的仓库。这类条目标记为 `source: "search"`，只有**估算**的周增量（总星数 ÷ 仓库年龄），排序时降权，写周报时不能说成实测值。

   对 `ai-agent` 之外的三个主题，search 实际上是**唯一**来源：冷门赛道几乎不可能上 trending 榜。所以它们的 `trending_languages` 只留了全局榜兜底。

两个来源按 `full_name` 去重，先用关键词打分过滤（省 API 配额），再逐个调 `/repos/{full_name}` 富化 topics / license / homepage 等字段，最后按周涨星数排序。

## 速率限制

- 匿名：core 60 次/小时，search 10 次/分钟。一次完整运行约消耗 **30 次 core + 9 次 search**，单次能跑完，但一小时内跑两次就会撞限额。
- 设 `GITHUB_TOKEN` 环境变量（任意 fine-grained PAT，只读 public 即可）后提到 5000 次/小时。
- 撞限额时 `api_get()` 会读 `Retry-After` / `x-ratelimit-reset` 退避重试，最多 3 次，单次等待封顶 90 秒；仍失败就 `WARN:` 到 stderr 并跳过该仓库，不会中断整轮。

## 出问题时先看这里

**`WARN: trending page for 'X' parsed 0 repos - markup may have changed`**
GitHub 改版了。解析逻辑在 `scripts/fetch_trending.py` 顶部的 `ARTICLE_SPLIT` / `RE_FULLNAME` / `RE_WEEKLY` / `RE_DESC`。抓一份 HTML 下来对着改：
```bash
curl -s -H "User-Agent: Mozilla/5.0" "https://github.com/trending?since=weekly" -o /tmp/t.html
```

**选出来的项目跑偏了**
改 `config/topics.json`：`keywords` 加权重、`exclude_patterns` 加正则（匹配的是仓库名的最后一段）、`min_score` 调阈值、`min_stars` 调门槛。改完直接重跑脚本看效果，不用动代码。

**网站上某篇报告显示「0 个项目」**
说明那份 `report.md` 的 H2 没写成 `## <序号>. [owner/repo](url)`。`build_site.py` 用这行正则提取项目清单，格式不符就提取不到。改 md 再重跑建站脚本。

**想加/删一个主题**
在 `config/topics.json` 的 `themes` 里加一块，再到 `.claude/commands/github-weekly.md` 和 `scripts/run_weekly.sh` 的主题列表里补上 slug。**已有主题的 slug 不要改** —— 它同时是 `reports/<DATE>/<slug>/` 的目录名和网站 URL 的一部分，改了历史报告就对不上。

## 定时任务（本地 launchd）

每周六 22:00 本地时间自动跑一次。

- **plist**：`~/Library/LaunchAgents/com.xingxingliu.githubrepograbber.plist`
- **runner**：`scripts/run_weekly.sh`（日志落在 `logs/<DATE>.log`，已 gitignore）
- **触发时间**：`StartCalendarInterval` Weekday=6 Hour=22。launchd 跟随系统时区，**DST 自动处理**，不需要每年手动改。
- **结果提醒**：跑完会发一条系统通知；失败的话带 Basso 提示音，日志路径写在通知里。

### 部署步骤

换机器、或者 plist 被清掉之后，按这三步重装：

**1. 注册 launchd 任务**

```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.xingxingliu.githubrepograbber.plist
launchctl print gui/$(id -u)/com.xingxingliu.githubrepograbber | grep -E 'state|runs'
```

**2. 设置定时唤醒（需要 sudo）**

launchd 会在 Mac 唤醒后补跑错过的任务，但**关机就直接跳过这一轮**。加一条比任务早 5 分钟的唤醒，保证周六晚上机器是醒的：

```bash
sudo pmset repeat wake MTWRFSU 21:55:00
```

确认生效：

```bash
pmset -g sched
```

说明：
- `MTWRFSU` 是每天都唤醒。只想周六唤醒就用 `S`（`pmset` 里 `S`=周六、`U`=周日），但每天唤醒更保险——万一某周六你人不在、Mac 关着，下次开机 launchd 也能补跑。
- 这条是**系统级设置**，和本仓库无关，重装系统后要重新执行。
- `pmset repeat` 只有一组设置，再执行一次会覆盖上一条，不会叠加。
- 唤醒只是让机器醒着跑任务，屏幕不会亮。

**3. 验证整条链路**

```bash
launchctl kickstart -p gui/$(id -u)/com.xingxingliu.githubrepograbber
tail -f logs/$(date +%F).log
```

日志末尾要看到 `ok: ai-agent/report.md`（这一条是硬性的）、`[site] built N reports -> docs/`，且退出码为 0 才算装好。

三个冷门主题某周没出报告是**正常结果**，不是失败：命令被要求「凑不满就少写几个甚至跳过」，好过拿几十星的玩具项目凑数。runner 只在 `ai-agent` 缺失、或四个主题一个都没产出时才判失败。

手动跑一次：

```bash
launchctl kickstart -p gui/$(id -u)/com.xingxingliu.githubrepograbber
tail -f logs/$(date +%F).log
```

停用 / 重新启用：

```bash
launchctl bootout gui/$(id -u)/com.xingxingliu.githubrepograbber
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.xingxingliu.githubrepograbber.plist
```

### 为什么不用云端 routine

一开始配的是 Claude cloud routine（`trig_01D8VqbrydAm7touznNTGSuH`，现已 `enabled: false`），**实跑失败**。根因是云端出口走共享数据中心 IP：

- `github.com/trending` 6 个语种页面**全部 403** —— GitHub 对数据中心 IP 反爬。同样的请求从家里 IP 是 200。
- 匿名 Search API 配额按 IP 计，早被同出口的其他租户耗尽，9 个 topic 全被限流。
- `git push` 被拒 403 —— sandbox 只有读权限（`TwinCitiesEventNotification` 当初是靠在 push 步骤嵌 fine-grained PAT 绕过的）。

trending 页面是**唯一**能拿到真实"本周涨星数"的地方，而它恰好是最容易被数据中心 IP 拦的一环。所以这个项目天然适合跑在住宅 IP 上。

云端方案还额外要求仓库 public（私有仓库创建 routine 直接 403，需要手动去 https://github.com/settings/installations 授权 Claude 的 GitHub App）。改回本地后这个约束消失，**仓库已改回 private**。

### launchd 踩的坑

- **`claude -p` 在 launchd 环境下会死在 `Not logged in · Please run /login`。** 它靠 `USER`/`LOGNAME` 去 keychain 取 `Claude Code-credentials`，而 launchd 不保证提供这两个变量。`run_weekly.sh` 里已显式 export（连同 `HOME`、`SHELL`、完整 `PATH`）。这是实测出来的，不是推测。
- **GitHub token 不落地。** runner 运行时用 `git credential fill` 从 keychain 直接读，不写 `.env`，避免明文 token 留在磁盘上。
- **Mac 必须醒着。** launchd 会在唤醒后补跑错过的任务，但关机就跳过 —— 用「部署步骤」第 2 步的 `pmset repeat wake` 解决。
- **产物"存在"不等于"生成过"。** 头一次 launchd 实跑时当天已有报告，agent 直接跳过没重做，而 runner 只检查目录存在，于是退出码 0、看起来一切正常。现在 runner 会比对四个文件的 mtime 是否落在本次运行窗口内，命令里也写死了「无条件重新生成」。
- **冷门主题会被热门主题挤死。** 抓取脚本原来按「本周实测涨星数」给候选排序，而 search 来源的条目这个字段是 `None`、一律按 0 处理。结果是 AR/VR、智能眼镜、机器人的候选在进 API 富化之前就被 agent 大仓全部挤出候选池 —— 关键词明明命中一百多个，最终报告里一个都没有。现在 `prerank_key()` 会给 search 条目算一个估算速度，让它们和 trending 条目在同一把尺子上排序。
- **搜索 topic 宁窄勿宽。** robotics 一开始挂了 `reinforcement-learning` 和 `simulation`，把计算机公开课清单、通用 Web UI 框架大批拖进候选；ar-vr 挂 `unity` 则拖进一堆和 XR 无关的普通游戏项目。关键词打分筛不掉这类——它们描述里确实有 `robotics`。已在 `topics.json` 里注明别加回去。

## GitHub Pages

- **发布源**：`main` 分支的 `/docs` 目录（仓库 Settings → Pages）。
- **仓库必须是 public**：免费账号的 Pages 不支持私有仓库。
- `docs/.nojekyll` 关掉 Jekyll 处理，否则以 `_` 开头的路径会被吞掉。
- 站点更新 = `git push`。runner 在校验完报告后会再跑一次 `build_site.py`（幂等，输出确定，不会产生多余 diff）。

### 命令文件的位置

`/github-weekly` 的权威版本在本仓库的 `.claude/commands/github-weekly.md`，`CluadeProjects/.claude/commands/` 下是个 symlink 指回来。文件里的路径在运行时解析 `<ROOT>`，不写死绝对路径——这是当初为了兼容云端 sandbox 做的改动，现在虽然不用云端了，但保留它意味着仓库换个位置也不会坏。
