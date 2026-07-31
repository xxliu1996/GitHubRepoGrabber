# 配图 Prompt（2026-07-30）

> 风格来源：`config/style.md`。改风格只改那个文件，不要改这里。
> 参考图：`config/reference/style_default.png`　→　**喂给图片生成器时请连同这张参考图一起提交**（用 PNG 那份，别用 AVIF）
> 目标生成器：GPT-Image
> 画幅：3:4 竖版，1080 × 1440，四边留 8% 安全边距
>
> ⚠️ 参考图本身是 3:2 横版，只用来传画风（纸张质感、铅笔线条、红黑配色），构图以下面每条 prompt 的 `Aspect ratio` 和构图描述为准。

---

## 封面

```text
Use case: xiaohongshu-cover
Aspect ratio: 3:4 vertical (1080x1440)
Primary request: A person sitting at a desk with a laptop, looking up thoughtfully at a vertical constellation of small floating interface cards arranged in a tall column above and around them — a browser window, a terminal panel, a code diff card, a book, a routing diagram with branching lines. The floating elements stack upward to fill the tall frame rather than spreading sideways. Convey the idea of tools orbiting and augmenting a single developer.
Chinese labels: Add 2 short Simplified Chinese labels as clean printed callouts: "本周 GitHub" near the top, "10 个 Agent 项目" beneath it. Keep them horizontal, large, high-contrast, and well inside the safe margins.
Composition/framing override: vertical 3:4 composition for a Xiaohongshu card; central figure in the lower third, floating elements filling the upper two thirds; generous safe margins on all four sides; nothing important within 8% of any edge; full subject visible, no crop.
Style/medium: A delicate, hand-drawn pencil illustration on textured cream paper. The style is minimalist with a limited, muted color palette (creams, charcoal black, soft terracotta reds). The artwork features fine, detailed linework, soft pencil shading, and a clean, graphic composition.

- **Illustration Type:** Pencil sketch, mixed media illustration, clean line art.
- **Color Palette:** Monochrome black, red, and cream/off-white background. No gradients.
- **Texture:** Fine paper grain texture, soft pencil smudges, charcoal-like shading for depth.
- **Composition:** Central figure surrounded by abstract, floating elements. Flat perspective with linear details.
- **Vibe:** Sophisticated, calm, contemplative, artisanal.

Constraints: no watermark, no logo, no signature, no English body text, no fake UI screenshots, no gradient background, no photorealistic rendering, no additional accent colors beyond the terracotta red.
```

---

## 内容卡 1：Agent Skills（对应 mattpocock/skills、ayghri/i-have-adhd）

```text
Use case: xiaohongshu-content-card
Aspect ratio: 3:4 vertical (1080x1440)
Primary request: A tall stack of small labeled cards or tags being slotted one by one into a simple robot-like figure or a stylized terminal window, as if installing modular abilities. Beside it, a long rambling paper scroll is being cut down by scissors into three short crisp lines — showing verbose output compressed into direct instructions. Arrange the two ideas vertically, the installing motif on top, the trimming motif below.
Chinese labels: Add 2 short Simplified Chinese labels: "技能即插即用" and "让 AI 说人话". Place each near its matching motif, horizontal and high-contrast.
Composition/framing override: vertical 3:4 composition for a Xiaohongshu card; two stacked vignettes filling the tall frame; generous safe margins on all four sides; nothing important within 8% of any edge.
Style/medium: A delicate, hand-drawn pencil illustration on textured cream paper. The style is minimalist with a limited, muted color palette (creams, charcoal black, soft terracotta reds). The artwork features fine, detailed linework, soft pencil shading, and a clean, graphic composition.

- **Illustration Type:** Pencil sketch, mixed media illustration, clean line art.
- **Color Palette:** Monochrome black, red, and cream/off-white background. No gradients.
- **Texture:** Fine paper grain texture, soft pencil smudges, charcoal-like shading for depth.
- **Composition:** Central figure surrounded by abstract, floating elements. Flat perspective with linear details.
- **Vibe:** Sophisticated, calm, contemplative, artisanal.

Constraints: no watermark, no logo, no signature, no English body text, no fake UI screenshots, no gradient background, no photorealistic rendering, no additional accent colors beyond the terracotta red.
```

---

## 内容卡 2：并行编码 Agent（对应 stablyai/orca、earendil-works/pi）

```text
Use case: xiaohongshu-content-card
Aspect ratio: 3:4 vertical (1080x1440)
Primary request: A single trunk line at the bottom splitting upward into four parallel vertical branches, each branch ending in a small isolated workspace card containing a tiny sketched robot working. At the top, the four branches converge back into one line marked with a small terracotta checkmark, showing that only the best result gets merged back. The branching structure should read clearly as a git graph rendered in pencil.
Chinese labels: Add 2 short Simplified Chinese labels: "并行跑" near the branches and "择优合并" near the convergence point at top.
Composition/framing override: vertical 3:4 composition for a Xiaohongshu card; the branching diagram runs bottom to top filling the tall frame; generous safe margins on all four sides; nothing important within 8% of any edge.
Style/medium: A delicate, hand-drawn pencil illustration on textured cream paper. The style is minimalist with a limited, muted color palette (creams, charcoal black, soft terracotta reds). The artwork features fine, detailed linework, soft pencil shading, and a clean, graphic composition.

- **Illustration Type:** Pencil sketch, mixed media illustration, clean line art.
- **Color Palette:** Monochrome black, red, and cream/off-white background. No gradients.
- **Texture:** Fine paper grain texture, soft pencil smudges, charcoal-like shading for depth.
- **Composition:** Central figure surrounded by abstract, floating elements. Flat perspective with linear details.
- **Vibe:** Sophisticated, calm, contemplative, artisanal.

Constraints: no watermark, no logo, no signature, no English body text, no fake UI screenshots, no gradient background, no photorealistic rendering, no additional accent colors beyond the terracotta red.
```

---

## 内容卡 3：模型网关与成本（对应 diegosouzapw/OmniRoute）

```text
Use case: xiaohongshu-content-card
Aspect ratio: 3:4 vertical (1080x1440)
Primary request: Many thin lines entering from the top edge of the frame, funnelling down through a single small hexagonal gateway node in the middle, then continuing as one clean line to a laptop at the bottom. Beside the gateway, a small coin or price tag drawn in terracotta red, and a tiny pruned branch indicating a failed route being bypassed. The funnel shape should read as many providers collapsing into one endpoint.
Chinese labels: Add 2 short Simplified Chinese labels: "290+ 服务商" near the top lines and "一个接口" beside the gateway node.
Composition/framing override: vertical 3:4 composition for a Xiaohongshu card; the funnel runs top to bottom filling the tall frame; generous safe margins on all four sides; nothing important within 8% of any edge.
Style/medium: A delicate, hand-drawn pencil illustration on textured cream paper. The style is minimalist with a limited, muted color palette (creams, charcoal black, soft terracotta reds). The artwork features fine, detailed linework, soft pencil shading, and a clean, graphic composition.

- **Illustration Type:** Pencil sketch, mixed media illustration, clean line art.
- **Color Palette:** Monochrome black, red, and cream/off-white background. No gradients.
- **Texture:** Fine paper grain texture, soft pencil smudges, charcoal-like shading for depth.
- **Composition:** Central figure surrounded by abstract, floating elements. Flat perspective with linear details.
- **Vibe:** Sophisticated, calm, contemplative, artisanal.

Constraints: no watermark, no logo, no signature, no English body text, no fake UI screenshots, no gradient background, no photorealistic rendering, no additional accent colors beyond the terracotta red.
```

---

## 内容卡 4：代码理解与 RAG（对应 tirth8205/code-review-graph、infiniflow/ragflow、alibaba/open-code-review）

```text
Use case: xiaohongshu-content-card
Aspect ratio: 3:4 vertical (1080x1440)
Primary request: In the upper half, a node-and-edge graph of small connected boxes representing a codebase map, with one node and its immediate neighbours highlighted in terracotta red while the rest stay faint pencil grey — showing that only the affected blast radius is selected. In the lower half, a thick stack of paper documents being sliced into neat labelled cards, with a thin red thread running from one card back up to its source page, indicating a citation link.
Chinese labels: Add 2 short Simplified Chinese labels: "只喂相关代码" near the graph and "答案可溯源" near the document stack.
Composition/framing override: vertical 3:4 composition for a Xiaohongshu card; two stacked vignettes filling the tall frame; generous safe margins on all four sides; nothing important within 8% of any edge.
Style/medium: A delicate, hand-drawn pencil illustration on textured cream paper. The style is minimalist with a limited, muted color palette (creams, charcoal black, soft terracotta reds). The artwork features fine, detailed linework, soft pencil shading, and a clean, graphic composition.

- **Illustration Type:** Pencil sketch, mixed media illustration, clean line art.
- **Color Palette:** Monochrome black, red, and cream/off-white background. No gradients.
- **Texture:** Fine paper grain texture, soft pencil smudges, charcoal-like shading for depth.
- **Composition:** Central figure surrounded by abstract, floating elements. Flat perspective with linear details.
- **Vibe:** Sophisticated, calm, contemplative, artisanal.

Constraints: no watermark, no logo, no signature, no English body text, no fake UI screenshots, no gradient background, no photorealistic rendering, no additional accent colors beyond the terracotta red.
```
