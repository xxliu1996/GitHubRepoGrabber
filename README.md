# GitHubRepoGrabber

每周抓一次 GitHub 上最火的 LLM / Agent / Agent Skills 项目，产出三样东西：一份 Markdown 周报、一篇可直接发布的小红书中文文案、一组配图生成 prompt。

## 设计

沿用 `TwinCitiesEventNotification` 的分工：**脚本只负责确定性的抓取和排序，输出 JSON；文字由 agent 写。** 这样抓取逻辑可测试可复现，文案质量交给模型。

```
GitHubRepoGrabber/
├── config/
│   ├── topics.json        # 关键词权重、抓取语种、排除规则 —— 调整选题方向改这里，不用改代码
│   └── style.md           # 配图风格块（占位，等参考图到位后由用户改写）
├── scripts/
│   └── fetch_trending.py  # 纯标准库，JSON 打到 stdout
└── reports/
    └── YYYY-MM-DD/
        ├── raw.json         # 脚本原始输出，一并提交，便于复现
        ├── report.md        # 周报
        ├── rednote.md       # 小红书文案
        └── image-prompts.md # 配图 prompt
```

## 用法

一条命令跑完整个流程：

```
/github-weekly            # 用今天的日期
/github-weekly 2026-07-30 # 指定日期
```

命令定义在 `/Users/xingxingliu/Projects/CluadeProjects/.claude/commands/github-weekly.md`。

只想看数据、不生成文案：

```bash
python3 scripts/fetch_trending.py --limit 20 | python3 -m json.tool | head -60
```

常用参数：`--out <路径>` 同时落盘，`--limit N` 输出条数，`--enrich-pool N` 进入 API 富化的候选数（每个候选消耗 1 次 core 配额），`--week-of YYYY-MM-DD` 指定周锚点。

## 数据来源

1. **`github.com/trending?since=weekly`** —— GitHub 唯一公开真实"本周涨星数"的地方。全站页 + `topics.json` 里列出的各语种页，一共 6 个页面，约 100 个仓库。这是主来源。
2. **Search API 兜底** —— 按 `topic:llm`、`topic:ai-agent` 等逐个查最近 7 天有推送的仓库，防止某周 trending 被非 AI 项目刷屏时凑不够 10 个。这类条目标记为 `source: "search"`，只有**估算**的周增量（总星数 ÷ 仓库年龄），排序时降权，写周报时不能说成实测值。

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

**配图风格要换**
只改 `config/style.md` 里那个 ```text 代码块。每周生成 `image-prompts.md` 时会原样内联进每一条 prompt。参考图路径也登记在那个文件里。

## 云端定时任务

计划用 Claude cloud routine 每周一次触发 `/github-weekly`。踩过的坑（来自 `TwinCitiesEventNotification`）：

- **网络白名单**：cloud sandbox 的出网走域名白名单，必须放行 `github.com` 和 `api.github.com`。
- **推送凭据**：sandbox 默认的 git credential proxy 对新仓库没有写权限，需要在 routine 的 push 步骤里用 fine-grained PAT（Contents: read/write，只授权这一个仓库）。
- **建议在 routine 里注入 `GITHUB_TOKEN`**，否则匿名配额会让富化步骤频繁退避，整轮变慢。

> 目前尚未创建 routine，也还没配置 remote。要走云端定时，得先在 GitHub 上建好远程仓库。
