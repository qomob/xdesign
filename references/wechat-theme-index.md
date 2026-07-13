# 公众号排版主题注册表

> 本文件是主题信息的**单一来源**。新增主题必须在此登记一行。

| 主题名 | 英文标识 | 主色 | 适用场景 | 组件库文件 | 正文下划线 CSS |
|--------|---------|------|---------|-----------|---------------|
| 翡翠绿 | emerald | `#059669` | 教程/测评/清单/工具盘点/知识整理（信息密度高，卡片丰富） | `wechat-theme-emerald.md` | `border-bottom:2px solid #6EE7B7` |
| 石墨灰 | graphite | `#374151` | 设计/科技评论/专业观点/高端品牌（极简留白） | `wechat-theme-graphite.md` | `border-bottom:2px solid #9CA3AF` |

## 选主题决策树

```
文章类型？
├─ 教程/操作指南/测评/盘点 → emerald（翡翠绿）
├─ 观点/深度分析/力量感话题 → graphite（石墨灰）或 emerald
├─ 设计/科技评论/高端品牌 → graphite（石墨灰）
├─ 禅意/极简/随笔 → graphite（石墨灰）
├─ 数据复盘/报告 → emerald（翡翠绿）
└─ 不确定 → emerald（默认第一行）
```

## 新增主题规范

新主题以 `references/wechat-theme-{英文标识}.md` 命名，必须包含：
1. 设计变量速查表
2. 各组件完整 HTML（内联样式 + `<span leaf="">` 包裹）
3. 完整文章模板骨架
4. 文章类型 → 组件组合配方表
5. Markdown → 组件映射规则表

添加后在本文件登记一行，并跑 `python3 scripts/wechat_component_lint.py .` 确认 0 ERROR。
