# XDesign

> Design Workflow Engine — 将想法到可交付物的全流程压缩为对话。
> 你不是在用"画图工具"，你是在驱动一个 **产品经理 + 初级设计师 + 前端开发** 的合体。

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

---

## 支持的项目类型

| 类型 | 说明 | 输出 |
|---|---|---|
| **Interactive Prototype** | 可交互的产品/UI 原型 | HTML |
| **Pitch Deck** | 演示文稿/幻灯片 | HTML → PPTX/PDF |
| **Landing Page** | 落地页/营销页面 | HTML |
| **Design System** | 品牌设计系统/UI Kit | HTML |
| **Animated Video** | 时间轴动画/动效设计 | HTML |
| **Wireframe** | 低保真线框图/故事板 | HTML |

---

## 快速开始

### 1. 写一个结构化的 Prompt

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

### 2. 正确的设计流程

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

### 技术栈

- **React 18.3.1** + **Babel 7.29.0**（固定版本，含 integrity hash）
- 输出为单 HTML 文件，内嵌 React 组件
- 7 个 Starter Components（deck_stage / design_canvas / ios_frame / animations 等）

### Starter Components

| 组件 | 用途 |
|---|---|
| `deck_stage.js` | 幻灯片演示（自动缩放/键盘导航/讲稿/打印） |
| `design_canvas.jsx` | 并排展示多个静态方案 |
| `ios_frame.jsx` | iPhone 外壳模拟 |
| `android_frame.jsx` | Android 外壳模拟 |
| `macos_window.jsx` | 桌面窗口外壳 |
| `browser_window.jsx` | 浏览器窗口外壳 |
| `animations.jsx` | 时间轴动画（Stage + Sprite + Easing） |

### 导出能力

| 格式 | 说明 |
|---|---|
| **PPTX (editable)** | 原生文本/形状，可在 PowerPoint 编辑 |
| **PPTX (screenshots)** | 逐页截图，像素级精确 |
| **PDF** | 浏览器打印导出 |
| **Standalone HTML** | 单文件自包含，离线可用 |
| **Canva** | 导出为可编辑的 Canva 设计 |
| **React Code** | 转为可开发的 React 组件 |

---

## 内置 Sub-Skills

通过 `invoke_skill` 按需加载：

| 技能 | 触发场景 |
|---|---|
| Animated video | 时间轴动效设计 |
| Interactive prototype | 可交互的产品原型 |
| Make a deck | HTML 幻灯片演示 |
| Make tweakable | 添加设计内调参控件 |
| Frontend design | 品牌系统外的美学方向 |
| Wireframe | 线框图/故事板 |
| Create design system | 创建设计系统/UI Kit |
| Export as PPTX | 导出 PowerPoint |
| Save as PDF | 导出 PDF |
| Save as standalone HTML | 导出独立 HTML |
| Send to Canva | 导出到 Canva |
| Handoff to Claude Code | 开发者交接包 |

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

---

## 常见坑

| 坑 | 后果 | 解决方案 |
|---|---|---|
| Prompt 太短 | 输出平庸 | 用结构化模板 |
| 没喂数据 | 永远"通用设计" | 先上传品牌资料 |
| 一上来追求精致 | 陷入无限微调 | 先 Wireframe 再 Hi-Fi |
| 当 Figma 替代 | 定位错误 | 这是前期+结构设计工具 |
| 跳过设计系统 | 每页风格不统一 | 先建 Design System |

---

## 文件结构

```
XDesign/
├── SKILL.md                          # 核心技能文件（工作流 + 规范）
└── references/
    ├── technical-specs.md             # 技术规范（动画/导出/GitHub/跨项目访问）
    └── workflow-guide.md              # 高手玩法（Prompt 模板/参考输入/迭代技巧）
```

---
