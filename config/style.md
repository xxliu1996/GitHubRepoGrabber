# 图片风格模板（占位）

> **这是唯一需要你手动维护的风格文件。**
> 拿到参考图之后，只改下面那个代码块的内容即可 —— 每周生成 `image-prompts.md` 时会把它**原样内联**进每一条 prompt。
> 不要改标题和分隔线，脚本/命令靠 ```text 代码块定位内容。

## 当前风格块

```text
Style/medium: clean modern editorial tech illustration, flat vector with subtle depth, off-white paper background, crisp black linework, muted gray surfaces, one saturated accent color used sparingly.
Composition/framing: vertical 3:4 composition sized for a Xiaohongshu (RedNote) card, subject centered with generous safe margins on all four sides, nothing important within 8% of any edge, full subject visible, no crop.
Lighting/mood: even soft studio light, calm and confident, slightly optimistic, not corporate-stocky.
Typography: any text must be large, horizontal, high-contrast Simplified Chinese; no more than 5 short labels per image.
Constraints: no watermark, no logo, no brand marks, no English body text, no gradient mesh background, no decorative blobs, no lens flare, no photorealistic faces, no fake UI screenshots.
```

## 参考图（待补充）

用户后续会提供一张风格参考图。拿到之后：

1. 把图片放进 `config/reference/` 目录。
2. 在下面登记路径，生成 prompt 时会在文件顶部提示"请连同这张参考图一起喂给图片生成器"。

- 参考图路径：_（暂无）_
- 图片生成器：_（暂无，例如 GPT-Image / Midjourney / 即梦）_
