# XDesign

> Design Workflow Engine — 将想法到可交付物的全流程压缩为对话。
>
> 用一句话告诉 XDesign 你要做什么，它帮你完成 **产品定位 → 设计定向 → 结构打磨 → 高保真产出** —— 相当于一个产品经理 + 视觉设计师 + 前端的合体。

**当前版本**：v2.7

---

## 三模式路由

XDesign 根据你的意图分发到 3 种工作模式：

| 模式 | 触发词 | 输出 |
|------|--------|------|
| **Mode 1 / Presentation** | PPT、slides、演讲、pitch deck、带逐字稿 | HTML deck（36 主题 / 31 布局 / 15 full-deck 模板 / 47 动效 / 演讲者模式） |
| **Mode 2 / Visual Design** | 落地页、APP、dashboard、组件、UI Kit、原型 | HTML 原型（React+Babel + 线框图→高保真 + DESIGN.md 抽取） |
| **Mode 3 / Animation** | 动效视频、时间轴、motion design | HTML 动画（Stage + Sprite + Easing） |

> ⚠️ 路由规则：说 "deck / PPT / slides" 走 Mode 1；不明确时先问。

---

## 快速开始

### 路径 A — 做一份演示 PPT

```
做一个产品发布 PPT
听众：技术开发者  风格：暗色科技感  页数：10-12  带演讲者模式（逐字稿+计时器）
```

→ 匹配 `tokyo-night` 主题 → 先出 3 张预览确认方向 → 全量生成 → `S` 键进演讲者模式。

### 路径 B — 做产品落地页

```
做一个 B2B SaaS 后台的落地页
目标用户：运营人员  风格：简洁冷静  参考：Stripe + Linear  Dashboard 优先展示 3 种布局方案
```

→ Brief Inference 定向 → 出方向选择 → 定型后出完整页。

**模糊需求？** XDesign 会自动用 3 轮结构化提问帮你收敛方向（给谁用 / 核心转化目标 / 视觉参考）。

### 路径 C — 数据可视化

```
把这个 CSV 做成数据看板
[粘贴 CSV]
```

→ 自动跳过设计系统 → 识别数据结构 → 直接生成图表看板。

---

## 核心能力一览（v2.4-v2.7）

| 版本 | 能力 | 用途 |
|------|------|------|
| v2.7 | **Progressive Intake** | 模糊需求时 ≤3 轮多选提问，自动推断方向，不让用户做设计决策 |
| v2.7 | **Four Dials** | `DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY / ANIMATION_FREQUENCY`（1-10）从上下文自动推断 |
| v2.7 | **Motion Vocabulary** | "弹一下" → scale pop、"依次出现" → stagger sequence，精确翻译 |
| v2.7 | **Animation Reason Checklist** | Mode 3 每个动画必须服务于功能（空间一致性/状态指示/关系解释/防迷失/反馈），否则删除 |
| v2.7 | **Pre-flight Animation Rules** | 新增动画专项：时长边界、缓动曲线、GPU 层属性、触控安全 |
| v2.7 | **Physical Correctness** | 入场从 `scale(0.96)+opacity:0` 开始；reduced-motion 拆解为 transform=none + preserve color |
| v2.6 | **Anti-AI-Slop** | 双层 slop 纠正（视觉模式层 + 排版/颜色/布局/动效的深层 bias 排查） |
| v2.6 | **Pre-flight Check** | CP4 交付前 10 项机械检查（颜色锁、饱和度、italic 降部、占位符、marquee 数、触控区…） |
| v2.5 | **Design Direction Advisor** | 无品牌时出 3 个差异化方向（Information-first / Conversion-first / Concept-led） |
| v2.5 | **Brand Asset Protocol** | 5 步强制流程：问 → 搜 → 下载 → 验证 → 固化 |
| v2.5 | **Fact-Verify #0** | 先 WebSearch 验证产品设计前提 |
| v2.4 | **Streaming Preview** | >8 页先出 5 页预览，确认后再全量 |
| v2.4 | **Format Auto-Detect** | CSV/JSON/SQL/Markdown 自动识别并跳过设计系统 |

---

## 支持的项目类型

| 类型 | 输出 | 模式 |
|------|------|------|
| Pitch Deck / 演讲 PPT | 自包含 HTML（CND webfont，离线可用） | 1 |
| 小红书图文 | 7 格 bento / hero + Ken Burns | 1 |
| Interactive Prototype | 可交互产品原型 | 2 |
| Landing Page | 营销 / SaaS 落地页 | 2 |
| Design System / UI Kit | DESIGN.md + 组件示例 | 2 |
| URL → Brand | 从网址提取设计令牌 | 2 |
| 数据可视化 | 看板 / 图表 / 仪表板 | 2 |
| Animated Video | 时间轴动画 | 3 |
| Wireframe | 低保真线框图 / 故事板 | 2 |

---

## 导出格式

| 格式 | 说明 | 命令 |
|------|------|------|
| **HTML** | 单文件，离线可用 | 默认输出 |
| **PDF** | 浏览器打印 / headless Chrome | `./scripts/package-export.sh pdf <file>` |
| **PPTX** | pandoc 转换，可在 PowerPoint 编辑（有损，review 用） | `./scripts/package-export.sh pptx <file>` |
| **PNG / slide** | headless Chrome 逐页渲染 | `deck-studio/scripts/render.sh <file> <pages>` |
| **WeChat** | Juice-inlined 公众号粘贴 | `./scripts/package-export.sh social wechat <file>` |
| **小红书 XHS** | 2× retina PNG | `./scripts/package-export.sh social xhs <file>` |
| **X / Twitter** | 2× retina PNG | `./scripts/package-export.sh social x <file>` |

---

## 内置 Sub-Skills

按需加载：

| 子技能 | 场景 |
|--------|------|
| Make a deck (fused) | Mode 1 演示 + 主题循环 + 演讲者模式 |
| Animated video | Mode 3 时间轴动效 |
| Interactive prototype | Mode 2 可交互原型 |
| Make tweakable | 设计内调参控件（TWEAKS 面板） |
| Frontend design | 品牌外设计风格探索 |
| Wireframe | 线框图 / 故事板 |
| Create design system | 从品牌资料生成 DESIGN.md |
| Export as PPTX / PDF / HTML | 多格式导出 |

---

## 技术架构

```
Mode 1 (deck-studio/) — 纯静态 HTML/CSS/JS，零构建，CDN webfont
Mode 2/3 (原 XDesign) — React 18.3.1 + Babel 7.29.0 单 HTML 内嵌

统一输出：单文件 HTML 或自包含目录
运行：Trae IDE / Claude.ai / 任意浏览器 / GitHub Pages / file:// 均可
```

### deck-studio 资源

- **36 主题**：极简 / 商务 / 暗色 / 强调 / 工程 / 社交 6 个类别
- **31 单页布局**：封面、目录、3-列、KPI、图表、代码、流程、路线图…
- **15 full-deck 模板**：pitch / product-launch / tech-sharing / weekly-report / course / xhs…
- **47 动效**：27 CSS 入场动画 + 20 canvas FX（粒子、烟花、矩阵雨、神经网络…）
- **演讲者模式**：`S` 键弹出当前页 / 下一页 / 提词器 / 计时器

### Mode 2/3 资源

- 58 个品牌 DESIGN.md（Stripe / Linear / Notion / Figma / Vercel / Apple / Tesla…）
- deck_stage.js / design_canvas.jsx / animations.jsx + iOS/Android/macOS/Browser frame

---

## 文件结构

```
XDesign/
├── SKILL.md                           # Intent Router + Mode 1/2/3 + Design Direction Advisor
├── README.md                          # 本文件
├── LICENSE                            # MIT
├── THIRD_PARTY_NOTICES.md             # 第三方归属
├── assets/
│   └── design-md/                     # 58 个品牌 DESIGN.md
├── references/
│   ├── design-direction-advisor.md    # 设计方向顾问 + Four Dials + Motion Vocabulary
│   ├── design-system-catalog.md       # 58 品牌索引
│   ├── mode-2-prototype.md            # Mode 2/3：反 slop + Pre-flight + Junior Designer + Intake
│   ├── animation-standards.md         # Mode 3：理由清单 + Pre-flight #11-17 + 物理正确性
│   ├── workflow-guide.md              # 高手玩法（PPAF + 图片前置 + Tweaks）
│   ├── brand-asset-protocol.md        # 品牌资产 5 步协议
│   ├── technical-specs.md             # 技术规范
│   ├── integration-guide.md           # 融合架构 + 路由 + 上游同步
│   ├── deck-studio-catalog.md         # deck-studio 资源速查
│   └── schemas.md                     # DESIGN.md / tokens / evals schema
├── evals/
├── scripts/                           # lint / validate / export / package scripts
└── deck-studio/                       # 子模块（原 html-ppt-skill，MIT）
```

---

## 常见陷阱

| 坑 | 解决 |
|----|------|
| Prompt 太短 → 输出平庸 | 给目标用户 + 转化目的 + 参考风格 |
| 没喂品牌素材 → 通用设计 | 先上传 brand assets |
| 跳 Design System → 风格不统一 | 先建 Design system 再出页面 |
| PPT 词识别错 → 走错模式 | SKILL.md 路由规则：deck/slides/PPT → Mode 1 |
| 混用两套 token → 颜色不统一 | deck-studio 用 `var(--text-1)`，DESIGN.md 用自有 token，二选一 |
| AI slop 问题 | v2.6+ 启用反 slop 双层规则、After-state 采样、Pre-flight Check |

---

### 加入群聊

<div align="center">
  <img src="https://qomob.ai/xskill.jpg" width="600" alt="XSkill">
</div>

---

## License & Attribution

XDesign 自身为 MIT 许可证（见 `LICENSE`）。

`deck-studio/` 子目录是 [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) 的快照（© 2026 lewis，MIT）。详见 `THIRD_PARTY_NOTICES.md` 与 `deck-studio/LICENSE`。
