# XDesign

> Design Workflow Engine — 将想法到可交付物的全流程压缩为对话。
> 你不是在用"画图工具"，你是在驱动一个 **产品经理 + 初级设计师 + 前端开发** 的合体。
> v2.5 已融合 [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) → 内置 **deck-studio/** 子模块（36 主题 + 31 单页布局 + 15 full-deck 模板 + 47 动效 + 演讲者模式），并新增**决策支持层**（设计方向顾问 + 品牌资产协议 + 反 AI slop + 图片前置 + 事实验证）。

---

## 它是什么

XDesign 是一个 AI 驱动的设计流程引擎。它不是一个模板工具，不是 Figma 替代品，而是解决从 **"想法" → "可展示成果"** 这段最痛苦过程的完整工作流。

**核心能力：**
- 🎨 **视觉设计** — 通过 HTML 生成原型、演示文稿、落地页、动画、UI 设计
- 🧠 **设计系统提取** — 从品牌资料自动提取颜色/字体/组件规范
- 📐 **线框图 → 高保真** — 渐进式设计流程，先确认结构再打磨视觉
- 🎛️ **实时调参** — Tweaks 面板让用户在设计中即时调整参数
- 📤 **多格式导出** — PPTX、PDF、独立 HTML、Canva、React 组件代码
- 🌍 **多语言支持** — CJK、RTL、欧洲语言的本地化设计指导
- 💡 **设计解释** — 不仅做设计，还能解释设计逻辑，充当设计导师
- 🎤 **演讲者模式（fused）** — 4 卡片可拖拽的 presenter 视图（当前页/下页/提词器/计时器）

### v2.5 新增：决策支持层

当用户"不知道要什么"或"涉及真实品牌"时，XDesign 不再凭直觉硬做，而是走结构化决策流程：

| 机制 | 触发场景 | 做什么 |
|------|---------|--------|
| **设计方向顾问** | 模糊需求（"帮我做个好看的"），无品牌/参考 | 生成 3 个差异化视觉方向（信息优先 → 平衡 → 概念主导），让用户看着选 |
| **品牌资产协议** | 涉及真实品牌/产品 | 5 步硬流程（问 → 搜官方 → 下载 → 验证 → 固化 brand-spec.md），绝不凭记忆猜品牌色 |
| **反 AI slop 规则** | 所有 Mode 2/3 产出 | 每条 slop 规则附带 WHY 解释 + 合法例外边界，保护品牌识别度 |
| **图片素材前置** | 内容型设计（历史/自然/产品/人物） | PPAF 循环 Phase 1.5：先取真图再设计，不用色块糊弄 |
| **事实验证 #0** | 涉及具体产品/技术 | 开工前 WebSearch 验证产品存在性/版本号，避免基于错误假设返工 |

---

## 三模式路由

XDesign 内部有 **3 种工作模式**，按用户意图自动分发：

| 触发词 | 模式 | 走哪条路 |
|---|---|---|
| 做一份 PPT、slides、keynote、演讲、pitch deck、带逐字稿 | **Mode 1: Presentation / Deck** | `deck-studio/` 子模块（36 主题 + 31 单页布局 + 15 full-deck 模板） |
| 设计 APP、原型、dashboard、落地页、组件、UI Kit | **Mode 2: Visual Design / Prototype** | 原 XDesign 流程（Design System → Wireframe → Hi-Fi + React+Babel） |
| 动效视频、时间轴动画、motion design | **Mode 3: Animation / Video** | 原 XDesign `animations.jsx` 路径 |

> ⚠️ 默认走 Mode 1 的前提：用户说"做一份 deck / PPT / slides"；不明确时询问用户。

详见 [references/integration-guide.md](./references/integration-guide.md) 和 [references/deck-studio-catalog.md](./references/deck-studio-catalog.md)。

---

## 能力速览（v2.4-v2.5 新增）

除了基础的"三模式生成"，XDesign 还内置以下机制来减少返工、提升输出质量：

| 能力 | 版本 | 做什么 |
|------|------|--------|
| **验证第一步必带** | v2.5 | 投入完整交付物前先出最小可验证样本（1-3 张 slides / 1 个关键页面 / 1 帧动效），确认方向对了再做全量 |
| **设计方向顾问** | v2.5 | 模糊需求（"帮我做个好看的"）时生成 3 个差异化视觉方向让用户选，不凭直觉硬做 |
| **品牌资产协议** | v2.5 | 涉及真实品牌时强制走"问 → 搜 → 下载 → 验证 → 固化"5 步流程，不凭记忆猜品牌色 |
| **事实验证 #0** | v2.5 | 涉及具体产品/技术时先 WebSearch 验证，避免为"还没发布的产品"做发布动画 |
| **Format Auto-Detect** | v2.4 | CSV/JSON/SQL/Markdown 表格自动跳过设计系统阶段，直接生成图表或数据看板 |
| **Template Matching** | v2.4 | 按 `scenario` / `recommended` 字段从 15 个 deck 模板中智能推荐最匹配的 |
| **Streaming Preview** | v2.4 | >8 页 deck 拆两轮生成：先出 5 页预览确认方向，再生成完整 deck |
| **Cross-Agent Compatibility** | v2.4 | `deck-studio/` 可被 Claude Code / Cursor / Codex 等其他 agent 独立使用，不依赖 XDesign 路由 |

---

## 支持的项目类型

| 类型 | 说明 | 输出 | 模式 |
|---|---|---|---|
| **Pitch Deck / 演讲 PPT** | 演示文稿/幻灯片（带演讲稿、主题循环、键盘导航） | HTML（自包含、CDN-only） | Mode 1 |
| **小红书图文** | 7 格 bento 网格或全幅 hero + Ken Burns | HTML | Mode 1 |
| **Interactive Prototype** | 可交互的产品/UI 原型 | HTML | Mode 2 |
| **Landing Page** | 落地页/营销页面 | HTML | Mode 2 |
| **Design System** | 品牌设计系统/UI Kit | DESIGN.md + 组件示例 | Mode 2 |
| **URL-to-Brand** | 给一个网址，提取品牌色/字体/设计令牌 | DESIGN.md（可直接复用） | Mode 2 |
| **数据可视化** | CSV/JSON/SQL/Markdown 表格 → 交互图表或数据看板 | HTML（table/chart/dashboard） | Mode 2 |
| **Animated Video** | 时间轴动画/动效设计 | HTML | Mode 3 |
| **Wireframe** | 低保真线框图/故事板 | HTML | Mode 2 |

---

## 快速开始

### 路径 A：做一份演示文稿（Mode 1，默认路由）

最常见的入口。说"做一份 PPT / slides / deck"即可触发。

```
做一个产品发布 PPT
主题：AI 编程助手新产品发布
听众：技术开发者
风格：暗色科技感
页数：10-12 页
需要演讲者模式（逐字稿）
```

XDesign 会：
1. 匹配 `tokyo-night` / `cyberpunk-neon` 等暗色主题
2. 推荐从 `templates/full-decks/product-launch/` 拷贝起始模板
3. 先出 3 张代表性 slides 让你确认方向
4. 确认后生成完整 deck，按 `S` 键进演讲者模式

> **>8 页时**：自动启用 Streaming Preview——先出 5 页预览，确认方向后再生成完整 deck。

### 路径 B：设计一个产品界面（Mode 2）

**不要这样写：**
> 做个APP界面

**要这样写：**
```
做一个 B2B SaaS 后台
目标用户：运营人员，非技术背景
使用场景：日常数据监控 + 客户管理
核心功能：
- 数据看板（实时指标）
- 客户列表（筛选+操作）
- 任务分配
页面结构：
- Dashboard（首页）
- Customer List
- Customer Detail
设计风格：简洁冷静，专业可信
参考：
- Stripe Dashboard
- Linear
输出：
1. Wireframe（低保真）
2. 3种 Dashboard 布局方案
```

### 路径 C：直接喂数据（Format Auto-Detect）

CSV / JSON / SQL / Markdown 表格会自动跳过设计系统阶段，直接生成图表或数据看板：

```
把这个 CSV 做成一个数据看板
[粘贴 CSV 数据]
```

### 正确的设计流程

```
品牌资料上传 → 设计系统提取 → Wireframe（低保真）→ 确认布局 → 高保真设计 → 导出
```

**关键原则：**
1. **Design System First** — 先建立视觉基础（颜色/字体/组件），再做页面
2. **Wireframe Before Hi-Fi** — 先确认布局和信息层级，再升级视觉
3. **多版本生成** — 不要"再改一下"，而是一次给 3 种不同方案

### 3. 三种迭代方式

| 方式 | 适合场景 | 示例 |
|---|---|---|
| 💬 对话修改 | 方向性调整 | "按钮太重，轻一点" |
| 🖊️ 画布批注 | 具体元素修改 | 点击元素 → "改成卡片布局" |
| 🎛️ 滑杆调整 | 参数微调 | 间距/颜色/字号 |

---

## 技术架构

### 总体结构

- **Mode 2/3**（原 XDesign）：React 18.3.1 + Babel 7.29.0（固定版本，含 integrity hash），单 HTML 文件内嵌 React 组件
- **Mode 1**（deck-studio 子模块）：纯静态 HTML/CSS/JS，**零构建**，CDN webfont，所有主题/布局/动画即拷即用
- **双模式统一**：都输出单文件 HTML 或自包含目录，都可在 Trae IDE / Claude.ai artifacts / 任意浏览器 / GitHub Pages / `file://` 打开

### Mode 1 资源（deck-studio/）

- **36 个主题** — 极简（minimal-white, japanese-minimal, nord, rose-pine）/ 商务（corporate-clean, pitch-deck-vc, swiss-grid, editorial-serif）/ 暗色（dracula, catppuccin-mocha, gruvbox-dark, tokyo-night, solarized-light）/ 强调（bauhaus, memphis-pop, cyberpunk-neon, vaporwave, y2k-chrome, rainbow-gradient）/ 工程（blueprint, engineering-whiteprint, sharp-mono, terminal-green）/ 社交（xiaohongshu-white, soft-pastel, sunset-warm, magazine-bold）
- **31 个单页布局** — 封面/目录/章节分隔、bullets/双列/三列、stat-highlight/KPI/表格/Chart 4 种图、代码/diff/终端、流程/架构/思维导图/时间轴/甘特/路线图、hero/grid/CTA/Thanks
- **15 个完整 deck 模板** — product-launch / pitch-deck / tech-sharing / weekly-report / course-module / presenter-mode-reveal / testing-safety-alert / hermes-cyber-terminal / graphify-dark-graph / knowledge-arch-blueprint / obsidian-claude-gradient / dir-key-nav-minimal / xhs-pastel-card / xhs-post / xhs-white-editorial（每个都是目录结构，带 scoped CSS + 扩展 frontmatter 用于场景筛选）
- **47 个动效** — 27 个 CSS 命名入场动画（fade-up / rise-in / zoom-pop / path-draw / parallax-tilt...）+ 20 个 canvas FX（粒子/烟花/矩阵雨/神经网络/知识图谱/星座...）
- **演讲者模式** — S 键弹出 4 卡片：当前页 + 下一页 + 提词器 + 计时器

### Mode 2/3 资源（原 XDesign）

| 组件 | 用途 |
|---|---|
| `deck_stage.js` | 幻灯片演示（自动缩放/键盘导航/讲稿/打印） |
| `design_canvas.jsx` | 并排展示多个静态方案 |
| `ios_frame.jsx` / `android_frame.jsx` / `macos_window.jsx` / `browser_window.jsx` | 各种设备/窗口外壳 |
| `animations.jsx` | 时间轴动画（Stage + Sprite + Easing） |
| 58 个品牌 DESIGN.md | Stripe / Linear / Notion / Figma / Vercel / Apple / Tesla ... 直接拿现成设计系统 |

### 导出能力

| 格式 | 说明 | 模式 | 命令 |
|---|---|---|---|
| **Standalone HTML** | 单文件自包含，离线可用 | Mode 1 + 2 | 直接生成 |
| **PDF** | 浏览器打印 / headless Chrome 导出 | Mode 1 + 2 | `./scripts/package-export.sh pdf <file>` |
| **PPTX (lossy)** | 通过 pandoc 转换，可在 PowerPoint 编辑（有损，适合 review） | Mode 2 | `./scripts/package-export.sh pptx <file>` |
| **PNG (per slide)** | `deck-studio/scripts/render.sh` 走 headless Chrome | Mode 1 | `deck-studio/scripts/render.sh <file> <pages>` |
| **WeChat** | Juice-inlined CSS，粘贴到公众号编辑器 | Mode 1 + 2 | `./scripts/package-export.sh social wechat <file>` |
| **小红书 (XHS)** | 2× retina PNG，适配小红书图文 | Mode 1 + 2 | `./scripts/package-export.sh social xhs <file>` |
| **X / Twitter** | 2× retina PNG | Mode 1 + 2 | `./scripts/package-export.sh social x <file>` |

---

## 内置 Sub-Skills

通过 `invoke_skill` 按需加载：

| 技能 | 触发场景 | 模式 |
|---|---|---|
| **Make a deck（fused）** | HTML 幻灯片演示 + 主题循环 + 演讲者模式 | Mode 1 |
| Animated video | 时间轴动效设计 | Mode 3 |
| Interactive prototype | 可交互的产品原型 | Mode 2 |
| Make tweakable | 添加设计内调参控件（Tweaks 面板） | Mode 2 |
| Frontend design | 品牌系统外的美学方向 | Mode 2 |
| Wireframe | 线框图/故事板 | Mode 2 |
| Create design system | 创建设计系统/UI Kit | Mode 2 |
| Export as PPTX | 导出 PowerPoint（有损） | Mode 2 |
| Save as PDF | 导出 PDF | Mode 1 + 2 |
| Save as standalone HTML | 导出独立 HTML | Mode 1 + 2 |

---

## 多语言支持

XDesign 内置多语言设计指导：

- **CJK 文字**：行高 1.6-1.8，专用字体栈（思源黑体/苹方/游哥特等）
- **RTL 语言**：`dir="rtl"`，镜像布局
- **文本膨胀率**：英→中 ~60-80%，英→德 ~130%，英→日 ~80-100%
- **本地化**：`Intl` API 格式化，`lang` 属性，文本变量化

---

## 高手技巧

### 项目命名 = 隐形上下文
- ❌ "project1" → 生成结果平庸
- ✅ "AI招聘Agent平台" → 后续设计更稳定一致

### 参考输入比 Prompt 更重要
可以喂入：网站链接、Figma 导出、PPT、代码仓库、手绘草图、品牌素材。给它 Stripe/Notion/Linear 的截图，直接生成同级别 UI。

### 让它解释设计逻辑
问"为什么这样布局？"会输出完整的设计思考：信息层级、布局逻辑、色彩选择、交互原理、权衡取舍。相当于白嫖设计导师。

### 设计 → 代码一体化
说"把这个转成 React 组件"，直接从设计稿进入开发流程。

### 做 PPT 时点出"演讲者模式"
说 "我要去给团队讲 xxx" → 自动用 `deck-studio/templates/full-decks/tech-sharing/` 模板，每页生成 150-300 字逐字稿，按 S 键弹 4 卡片 presenter 视图。

### 做 PPT 时先定主题
明确主题能省 3 轮迭代。模糊就给 2-3 候选：
- 投资人 pitch → `pitch-deck-vc` / `corporate-clean` / `bauhaus`
- 技术分享 → `catppuccin-mocha` / `dracula` / `blueprint` / `tokyo-night`
- 小红书 → `xiaohongshu-white` / `soft-pastel` / `rainbow-gradient`
- 学术报告 → `academic-paper` / `editorial-serif` / `minimal-white`

---

## 常见坑

| 坑 | 后果 | 解决方案 |
|---|---|---|
| Prompt 太短 | 输出平庸 | 用结构化模板 |
| 没喂数据 | 永远"通用设计" | 先上传品牌资料 |
| 一上来追求精致 | 陷入无限微调 | 先 Wireframe 再 Hi-Fi |
| 当 Figma 替代 | 定位错误 | 这是前期+结构设计工具 |
| 跳过设计系统 | 每页风格不统一 | 先建 Design System |
| **PPT 触发词识别错** | 走 React+Babel 写了 50 行 deck | SKILL.md 入口路由 → 严格按"PPT/slides/deck"分到 Mode 1 |
| **混用两套 design token** | 主题/组件颜色不统一 | deck-studio 用 `var(--text-1)`，DESIGN.md 用自己的 token，二选一 |

---

## 文件结构

```
XDesign/
├── SKILL.md                          # 核心技能（Intent Router + Mode 1/2/3）
├── README.md                         # 本文件
├── LICENSE                           # XDesign 自身的 MIT 许可证
├── THIRD_PARTY_NOTICES.md            # 第三方归属（html-ppt-skill 等）
├── assets/
│   └── design-md/                    # 58 个品牌 DESIGN.md
│       ├── stripe/
│       ├── linear.app/
│       └── ... 共 58 个
├── references/
│   ├── design-system-catalog.md      # 58 品牌索引
│   ├── design-direction-advisor.md   # v2.5 设计方向顾问（模糊需求 Fallback）
│   ├── brand-asset-protocol.md       # v2.5 品牌资产协议（5 步硬流程）
│   ├── technical-specs.md            # 技术规范
│   ├── workflow-guide.md             # 高手玩法（PPAF + 图片前置 + Tweaks 模板）
│   ├── integration-guide.md          # 融合架构 + 路由表 + 适配层
│   ├── deck-studio-catalog.md        # deck-studio 资源速查
│   ├── mode-2-prototype.md           # Mode 2/3 详细规则（反 slop + Junior Designer + React+Babel）
│   └── schemas.md                    # DESIGN.md / tokens / evals schema
├── evals/
│   ├── evals.json                    # 3 个可执行 evals
│   ├── trigger-queries.json          # 20 个 trigger queries（12 触发 / 8 不触发）
│   └── eval-plan.json                # 遗留：评估设计元数据
├── scripts/
│   ├── lint-skill.py                 # 技能规范检查
│   ├── validate-themes.py            # deck-studio 主题引用校验
│   ├── new-prototype.sh              # Mode 2 原型脚手架
│   ├── add-brand.sh                  # 新品牌 DESIGN.md 脚手架
│   ├── package-export.sh             # HTML → PDF / PPTX
│   └── dist.sh                       # 清洁打包（排除 .git、临时文件）
└── deck-studio/                      # 子模块（html-ppt-skill 完整克隆，MIT）
    ├── SUBMODULE.md                  # 原 SKILL.md 重命名（避免双入口）
    ├── README.md / README.zh-CN.md
    ├── LICENSE                       # 原项目 MIT 许可证保留
    ├── assets/
    │   ├── base.css                  # 设计令牌 + 布局原语
    │   ├── fonts.css                 # webfont imports
    │   ├── runtime.js                # 键盘 + 演讲者 + 主题循环
    │   ├── themes/                   # 36 个主题 CSS
    │   └── animations/               # animations.css + 20 个 FX
    ├── references/                   # themes.md / layouts.md / animations.md / full-decks.md / authoring-guide.md / presenter-mode.md
    ├── templates/
    │   ├── deck.html                 # 最小 6 页 starter
    │   ├── theme-showcase.html       # 主题展示
    │   ├── layout-showcase.html      # 31 布局展示
    │   ├── animation-showcase.html
    │   ├── full-decks-index.html
    │   ├── full-decks/               # 15 个 full-deck 模板
    │   └── single-page/              # 31 个单页布局
    └── scripts/
        ├── new-deck.sh
        └── render.sh                 # headless Chrome → PNG
```

---

## Credits & Attribution

XDesign 是原创工作流引擎（[references/integration-guide.md](./references/integration-guide.md) 详述架构与路由）。

`deck-studio/` 子目录是 [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) 的快照克隆，原作者 © 2026 lewis，原项目使用 MIT 许可证。我们保留原 `LICENSE` 文件，并在 [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md) 中列明所有第三方代码、来源与许可证。

如需重新同步上游或了解我们对 `deck-studio/` 做过的具体修改，参见 [references/integration-guide.md](./references/integration-guide.md) 的 *Upstream Sync Procedure* 章节。

---

## License

XDesign 自身代码以 MIT 许可证发布 — 详见 [LICENSE](./LICENSE)。`deck-studio/` 内的代码、主题、模板、动画遵循原 html-ppt-skill 的 MIT 许可证 — 详见 [deck-studio/LICENSE](./deck-studio/LICENSE)。

---

## 加入群聊

<div align="center">
  <img src="https://qomob.ai/xskill.jpg" width="600" alt="XSkill">
</div>

---
