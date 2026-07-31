# 配图风格配置

> **这是唯一需要手动维护的风格文件。** 每周生成 `image-prompts.md` 时，下面三块会被读取并注入到每一条 prompt 里。
> 改风格只改这个文件，不要改 `reports/` 里已生成的 prompt，也不要改脚本。
> ⚠️ 三个小节的标题和 ```text 代码块围栏请保持原样 —— `/github-weekly` 靠它们定位内容。

---

## 画幅

- **宽高比：3:4（竖版）**
- 像素建议：1080 × 1440
- 安全边距：四边各留 8%，重要元素和文字不要压边

---

## 参考图

把参考图放进 `config/reference/`，然后在下面登记路径。生成 prompt 时会在 `image-prompts.md` 顶部提示「请连同这张参考图一起喂给图片生成器」。

- 参考图路径：`config/reference/style_default.png`（原始文件 `style_default.avif` 一并保留）
- 目标图片生成器：GPT-Image

> ⚠️ 上传时用 `.png` 那份。原图是 AVIF，多数图片生成器（含 GPT-Image）的参考图上传不吃 AVIF，PNG 是安全格式。
> ⚠️ 参考图本身是 768×512（3:2 横版），而目标产出是 3:4 竖版 —— 它只用来传递**画风**（纸张质感、铅笔线条、红黑配色），不要让它带跑构图。所以下面风格块里的 `Composition` 那行在生成时会被 3:4 的构图要求覆盖。

---

## 风格块

把参考图配套的风格 prompt **原样粘贴**进下面的代码块（中英文都可以，照抄即可，不用改写成下面这种分行格式）。这段内容会被逐字内联到每一条 prompt 的风格部分。

```text
Style/medium: A delicate, hand-drawn pencil illustration on textured cream paper. The style is minimalist with a limited, muted color palette (creams, charcoal black, soft terracotta reds). The artwork features fine, detailed linework, soft pencil shading, and a clean, graphic composition.

- **Illustration Type:** Pencil sketch, mixed media illustration, clean line art.
- **Color Palette:** Monochrome black, red, and cream/off-white background. No gradients.
- **Texture:** Fine paper grain texture, soft pencil smudges, charcoal-like shading for depth.
- **Composition:** Central figure surrounded by abstract, floating elements. Flat perspective with linear details.
- **Vibe:** Sophisticated, calm, contemplative, artisanal.
```

✅ 已替换为实际风格（对应 `style_default.png`）。要再改就整块换掉，保留 ```text 围栏。

### 补充约束

上面的风格块只描述"要什么"，没写"不要什么"。GPT-Image 在没有负面约束时容易自作主张加水印、假英文界面文字、渐变背景。所以生成 prompt 时会自动追加这一行：

```text
Constraints: no watermark, no logo, no signature, no English body text, no fake UI screenshots, no gradient background, no photorealistic rendering, no additional accent colors beyond the terracotta red.
```

如果不想要这行，把这一小节整个删掉即可。
