# XDesign

> Design Workflow Engine — 把想法变成可交付物，一句话就够。
>
> 告诉 XDesign 你要做什么，它帮你完成 **定向 → 结构 → 高保真** ——  PRODUCT + 设计 + 前端，合体。

**最新版本**：v2.9 | MIT License

---

## 核心哲学

### Human + Agent 同构

XDesign 是**人和 AI agent 用同一套工具、同一份参考做设计**。每张路由表、每条 fallback、每个校验规则，同时服务两类用户。同构承诺：让 agent 更易懂的改动，也让人更易懂。不存在"仅 agent 可读"的隐藏配置。

### Guidance over Enforcement

规则是**扶手不是墙**。用户明确要求破例时，确认一次即放行。唯一不可破例的是无障碍硬要求（对比度、键盘可达、焦点环、reduced-motion）。

### Architecture: Foundations → Components → Patterns

视觉能力三层构建，下层托着上层：

```
Foundations (主题: 调色板 / 字号 / 间距 / 阴影)
    ↓
Components (单页构件: 31 种布局)
    ↓
Patterns (叙事配方: 8 种多页弧)
```

---

## 四模式路由

| 模式 | 触发词 | 输出 |
|------|--------|------|
| **Mode 1 / Presentation** | PPT、slides、演讲、pitch deck、逐字稿 | 36 主题 / 31 布局 / 15 模板 / 47 动效 / 演讲者模式 |
| **Mode 2 / Visual Design** | 落地页、APP、dashboard、原型、组件、UI Kit | 线框图→高保真 / React+Babel / DESIGN.md 抽取 |
| **Mode 3 / Animation** | 动效视频、时间轴、motion design | Canvas + requestAnimationFrame 时间轴动画 |
| **Mode 4 / 公众号排版** | 公众号排版、微信排版、gzh | 2 套主题组件库 / 平台合规内联 HTML / 双关卡校验 |

> ⚠️ 模糊意图时先问一次 —— 30 秒问题省 1 小时返工。

---

## 快速开始

### A. 做演示 PPT

```
做一个产品发布 PPT
听众：技术开发者  风格：暗色科技感  页数：12  带演讲者模式（逐字稿+计时器）
```

→ 选主题 → 3 张预览确认 → 全量生成 → `S` 键进演讲者模式。

### B. 做产品落地页

```
做一个 B2B SaaS 后台落地页
目标用户：运营  风格：简洁冷静  参考：Stripe + Linear  3 种 Dashboard 布局方案
```

→ Brief Inference 定向 → 出方向选择 → 定型后完整页。

### C. 数据可视化

```
把这个 CSV 做成数据看板
[粘贴 CSV]
```

 自动跳过设计系统 → 识别数据结构 → 直接生成图表看板。

### D. 公众号排版

```
把这篇文章排成公众号：article.md
风格：信息密度高的教程
```

 选主题 → 读组件库 → 解析 Markdown → 装配合规 HTML → 校验脚本兜底 → 输出可直接粘贴的正文片段。

**核心：约束优于自由。** 预设主题组件库保证输出下限，双关卡校验脚本（`validate_wechat_output.py` + `wechat_component_lint.py`）确定性兜底平台限制——不靠模型自觉。

**模糊需求？** XDesign 自动用 3 轮多选提问帮你收敛（给谁用 / 转化目标 / 视觉参考）。

---

## CLI 命令

```bash
# 导出
./scripts/xdesign export pdf  deck.html
./scripts/xdesign export pptx deck.html
./scripts/xdesign export social wechat|xhs|x deck.html

# 主题
./scripts/xdesign theme list
./scripts/xdesign theme validate

# 品牌 / 原型
./scripts/xdesign brand add shopify Shopify #95BF47
./scripts/xdesign proto new my-app linear

# v2.8: 弹出可复用子构件（Swizzle）
./scripts/xdesign eject templates/single-page/kpi-grid.html kpi-card my-kpi.html

# v2.9: 公众号排版校验（Mode 4）
./scripts/xdesign wechat validate output.html   # 校验产物合规
./scripts/xdesign wechat lint                   # 扫描组件库源头

# 检查 / 打包
./scripts/xdesign lint
./scripts/xdesign dist
```

---

## v2.9 新能力：公众号排版（Mode 4）

| 能力 | 说明 |
|------|------|
| **平台合规 HTML** | 禁 `<div>`/`class`/`id`/grid/CSS 变量；全内联 `style`；`<span leaf="">` 包裹每个文字节点——粘贴到公众号编辑器后样式不丢失 |
| **双关卡校验** | `validate_wechat_output.py`（产物关：13 条正则 + HTMLParser 遍历 leaf 包裹率 + 半角标点）+ `wechat_component_lint.py`（源头关：扫组件库反模式）构成可复现的"改→验→修"闭环 |
| **2 套主题组件库** | 翡翠绿 emerald（信息密集型，教程/测评/清单）+ 石墨灰 graphite（极简型，设计/科技评论）。每套 17 个原创组件 + 文章类型配方表 + Markdown 映射规则 |
| **通用增量组件** | 代码块（深/浅色，等宽不折行）、图片/GIF（带动图角标）、小标签/步骤标签/金句块——所有主题共用 |
| **内容智能** | 章节自动编号（末章 ∞）、每段 1-3 个关键词下划线、引言卡与目录提取、作者签名去重合并、中文全角标点自动规范 |
| **主题生成器** | 一句话描述或参考图 → 生成 45-75 个区块的完整组件库 → 转标准格式 → 登记 + 校验 |
| **格式归一化** | docx / pdf / 纯文本 → Markdown，非 Markdown 输入自动转格式后再排版 |

## v2.8 能力

| 能力 | 说明 |
|------|------|
| **Human+Agent 同构** | 路由表/fallback/校验规则同时服务人和 agent |
| **三层架构** | Foundations→Components→Patterns，多层复用 |
| **统一 CLI** | 一个 `xdesign` 入口替代 7 个分散脚本 |
| **Swizzle / Eject** | `data-block-id` 标注子构件，`xdesign eject` 一键提取复用 |
| **Delta 主题** | 品牌定制只需 10 行覆盖 `--accent` 等令牌，不 fork 整个文件 |
| **Vibe-tests** | 3 个视觉质量 eval：anti-slop / 叙事节奏 / 动效理由 |
| **Agent Playbook** | agent 决策指南独立成篇，SKILL.md 回归本职 |
| **Guidance > Enforcement** | 规则是扶手，无障碍以外均可破例 |

完整 changelog 见 [SKILL.md](SKILL.md) 底部版本表。

---

## Swizzle / Open internals（v2.8）

核心构件可组合到任何粒度，不需要锁在闭合 API 后面。

| block-id | 来源 | 提取内容 |
|---|---|---|
| `kpi-card` | `kpi-grid.html` | 单张 KPI 卡片 |
| `hero-counter` | `stat-highlight.html` | 巨型动画数字 |
| `process-step` | `process-steps.html` | 单个编号步骤 |
| `cta-buttons` | `cta.html` | 按钮组 |

```bash
./scripts/xdesign eject templates/single-page/kpi-grid.html kpi-card kpi-snippet.html
```

弹出的片段是独立 HTML，自动继承当前主题的 CSS 变量。

---

## Delta 主题（v2.8）

品牌定制不需要 fork 整个主题文件，写 10 行 delta 即可：

```css
/* brand-delta.css */
:root {
  --accent: #YOUR_HEX;
  --accent-2: /* 深一点 */;
}
```

```html
<link rel="stylesheet" href="../assets/themes/minimal-white.css">
<link rel="stylesheet" href="../assets/themes/brand-delta.css">
```

详见 [deck-studio/references/themes.md](deck-studio/references/themes.md)。

---

## 导出格式

| 格式 | 命令 |
|------|------|
| HTML（默认） | 直接输出 |
| PDF | `xdesign export pdf <file>` |
| PPTX（review 用） | `xdesign export pptx <file>` |
| 公众号排版（Mode 4） | `xdesign wechat validate <file>` 校验合规 |
| 微信 juice 内联（旧） | `xdesign export social wechat <file>` |
| 小红书 | `xdesign export social xhs <file>` |
| X/Twitter | `xdesign export social x <file>` |

> Mode 4 公众号排版与旧 `export social wechat` 的区别：前者是完整的排版工作流（主题组件库 + 内容智能 + 双关卡校验），后者仅做 juice CSS 内联（不保证粘贴后不丢样式）。

---

## 文件结构

```
XDesign/
├── SKILL.md                           # 工作流引擎主文档
├── README.md                          # 本文件
├── LICENSE / THIRD_PARTY_NOTICES.md
├── references/
│   ├── patterns.md                    # 8 种叙事配方 + Swizzle 机制
│   ├── agent-playbook.md              # agent 专属决策指南
│   ├── mode-2-prototype.md            # Mode 2/3: 反 slop + Pre-flight
│   ├── mode-4-wechat.md               # Mode 4: 公众号排版工作流
│   ├── animation-standards.md         # Mode 3: 理由清单 + 物理正确性
│   ├── design-direction-advisor.md    # 方向顾问 + Four Dials
│   ├── brand-asset-protocol.md        # 品牌资产 5 步协议
│   ├── workflow-guide.md              # PPAF 循环 + Tweaks
│   ├── wechat-theme-index.md          # 公众号主题注册表（单一来源）
│   ├── wechat-theme-emerald.md        # 翡翠绿主题（信息密集型）
│   ├── wechat-theme-graphite.md       # 石墨灰主题（极简型）
│   ├── wechat-common-components.md    # 公众号通用组件（代码块/图片/标签）
│   ├── wechat-theme-generator.md      # 主题生成器（按描述/参考图造主题）
│   ├── wechat-format-normalize.md     # 格式归一化（docx/pdf → Markdown）
│   └── ...                            # 其余参考文档
├── scripts/
│   ├── xdesign                        # 统一 CLI 入口
│   ├── validate_wechat_output.py      # Mode 4: 公众号产物合规校验
│   ├── wechat_component_lint.py       # Mode 4: 组件库源头检查
│   └── package-export.sh / lint-skill.py / ...
├── evals/                             # 8 个 eval (含 3 个 vibe-test)
├── deck-studio/                       # 静态 PPT 引擎子模块
│   ├── assets/
│   │   ├── themes/                    # 36 主题 + _delta-example.css
│   │   ├── animations/                # 47 动效
│   │   └── base.css / fonts.css / runtime.js
│   └── templates/
│       ├── single-page/               # 31 布局（含 data-block-id 标注）
│       └── full-decks/                # 15 完整模板
└── assets/design-md/                  # 58 品牌 DESIGN.md
```

---

## 常见陷阱

| 坑 | 解决 |
|----|------|
| Prompt 太短 → 输出平庸 | 给目标用户 + 转化目的 + 参考风格 |
| 没喂品牌素材 → 通用设计 | 先上传 brand assets |
| 跳 Design System → 风格不统一 | 先定 tokens 再出页面 |
| 混用两套 token → 颜色跑偏 | deck-studio 用 `var(--text-1)`，brand 用自有 token，二选一 |
| AI slop | v2.6+ 双层反 slop + Pre-flight Check |
| 主题定制太笨重 | v2.8 delta 主题：10 行覆盖即可 |
| 公众号粘贴丢样式 | v2.9 Mode 4：全内联 + `<span leaf>` 包裹 + 双关卡校验脚本兜底 |
| 公众号排版风格飘 | v2.9 Mode 4：预设主题组件库 + 文章类型配方表，不让模型现场发挥 |

---

### 加入群聊

<div align="center">
  <img src="https://qomob.ai/xskill.jpg" width="600" alt="XSkill">
</div>

---

## License

XDesign 自身为 MIT。`deck-studio/` 是 [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) 的快照（© 2026 lewis，MIT）。详见 `THIRD_PARTY_NOTICES.md`。
