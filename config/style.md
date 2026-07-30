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

- 参考图路径：`config/reference/`_（待填写文件名，例如 `style-ref.png`）_
- 目标图片生成器：_（待填写，例如 GPT-Image / Midjourney / 即梦 / Nano Banana）_

---

## 风格块

把参考图配套的风格 prompt **原样粘贴**进下面的代码块（中英文都可以，照抄即可，不用改写成下面这种分行格式）。这段内容会被逐字内联到每一条 prompt 的风格部分。

```text
Style/medium: clean modern editorial tech illustration, flat vector with subtle depth, off-white paper background, crisp black linework, muted gray surfaces, one saturated accent color used sparingly.
Composition/framing: vertical 3:4 composition sized for a Xiaohongshu (RedNote) card, subject centered with generous safe margins on all four sides, nothing important within 8% of any edge, full subject visible, no crop.
Lighting/mood: even soft studio light, calm and confident, slightly optimistic, not corporate-stocky.
Typography: any text must be large, horizontal, high-contrast Simplified Chinese; no more than 5 short labels per image.
Constraints: no watermark, no logo, no brand marks, no English body text, no gradient mesh background, no decorative blobs, no lens flare, no photorealistic faces, no fake UI screenshots.
```

> 上面是占位内容（尚未替换为用户的实际风格）。替换时把整个代码块的内容换掉即可，保留 ```text 围栏。
