#!/usr/bin/env python3
"""公众号组件库源头检查器 —— 可验证循环的第一道关。

扫描 references/wechat-theme-*.md 和 wechat-common-components.md 里的
```html 代码块，检测会导致排版问题的反模式。只看真实组件 HTML，不被
说明文字干扰。

与 validate_wechat_output.py 配合构成闭环：
  改组件库 → 本脚本扫源头 → 生成产物 → validate_wechat_output.py 扫产物 → 修 → 重复

用法:
    wechat_component_lint.py [skill-dir]   # 默认当前目录
退出码: 1 = 有 ERROR, 0 = 通过。
"""
import glob
import os
import re
import sys

# 在每个 ```html 组件块内检查的反模式
SOURCE_CHECKS = [
    (re.compile(r"white-space\s*:\s*pre", re.I),
     "用了 white-space:pre —— 会把 HTML 源码缩进/换行渲染成大左缩进+空行;"
     "代码块改成每行一个 <p style=\"margin:0\">，缩进用全角空格"),
    (re.compile(r"</?div[\s>]", re.I),
     "出现 <div>，公众号会改写，请用 <section>"),
    (re.compile(r"\sclass\s*=", re.I),
     "出现 class 属性（会被公众号剥离）"),
    (re.compile(r"\sid\s*=", re.I),
     "出现 id 属性"),
    (re.compile(r"<style[\s>]", re.I),
     "出现 <style> 标签"),
    (re.compile(r"<script[\s>]", re.I),
     "出现 <script> 标签"),
    (re.compile(r"<link[\s>]", re.I),
     "出现 <link> 标签"),
    (re.compile(r"position\s*:\s*(fixed|absolute|sticky)", re.I),
     "position: fixed/absolute/sticky 不被支持"),
    (re.compile(r"display\s*:\s*grid", re.I),
     "display:grid 不被支持，请用 flex"),
    (re.compile(r"float\s*:", re.I),
     "float 不被支持"),
    (re.compile(r"var\s*\(\s*--", re.I),
     "用了 CSS 变量 var(--x)，公众号不支持"),
    (re.compile(r"@(media|keyframes|import)", re.I),
     "@media/@keyframes/@import 不被支持"),
]

# 四周虚线框（不含方向性 border-left 等）
FOURSIDE_DASHED = re.compile(r"border\s*:\s*[^;{}]*dashed", re.I)
CENTERED_BLOCK = re.compile(r"text-align\s*:\s*center", re.I)


def lint_single_file(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    name = os.path.basename(path)
    found = []
    seen = set()

    def add(level, msg):
        if msg not in seen:
            seen.add(msg)
            found.append((level, msg))

    for m in re.finditer(r"```html\s*\n(.*?)```", text, re.S):
        html = m.group(1)
        for rx, msg in SOURCE_CHECKS:
            if rx.search(html):
                add("ERROR", msg)
        # 四周虚线框：正文强调勿用；居中块视为"占位/素材"组件可豁免
        if FOURSIDE_DASHED.search(html) and not CENTERED_BLOCK.search(html):
            add("WARN",
                "四周虚线框 border:...dashed（正文强调请用左竖条;"
                "仅居中的素材占位块可用 dashed）")

    return name, found


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    # 匹配 wechat-theme-*.md 和 wechat-common-components.md
    patterns = [
        os.path.join(root, "references", "wechat-theme-*.md"),
        os.path.join(root, "references", "wechat-common-components.md"),
    ]
    refs = set()
    for pat in patterns:
        refs.update(glob.glob(pat))
    refs = sorted(refs)

    if not refs:
        print(f"未找到 {root}/references/wechat-*.md 组件库文件")
        sys.exit(1)

    total_err = total_warn = clean = 0
    print(f"📐 公众号组件库源头检查: {len(refs)} 个库\n")

    for path in refs:
        name, found = lint_single_file(path)
        if not found:
            clean += 1
            continue
        errs = [m for lv, m in found if lv == "ERROR"]
        warns = [m for lv, m in found if lv == "WARN"]
        total_err += len(errs)
        total_warn += len(warns)
        print(f"-- {name} --")
        for m in errs:
            print(f"   ❌ {m}")
        for m in warns:
            print(f"   ⚠️  {m}")

    print(f"\n汇总: {clean}/{len(refs)} 个库干净, ERROR x{total_err}, WARN x{total_warn}")
    if total_err == 0 and total_warn == 0:
        print("✅ 全部组件库源头无反模式")

    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
