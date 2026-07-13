#!/usr/bin/env python3
"""微信公众号 HTML 产物合规校验器。

公众号编辑器是一个极度受限的富文本粘贴器——大量 HTML 标签、CSS 属性
会被直接过滤。本脚本把平台限制从"模型自觉"变成"确定性兜底"。

用法:
    validate_wechat_output.py <file.html>
    validate_wechat_output.py --stdin < file.html

退出码: 1 = 有 ERROR（粘贴后样式会失效）; 0 = 通过。
"""
import argparse
import re
import sys
from html.parser import HTMLParser

# 公众号编辑器会过滤的标签/属性/CSS —— (正则, 说明)
# 这些是微信平台的客观技术限制，不是任何人的 IP
BANNED_PATTERNS = [
    (re.compile(r"<style[\s>]", re.I), "<style> 标签会被过滤，样式必须内联到 style 属性"),
    (re.compile(r"<script[\s>]", re.I), "<script> 标签会被过滤"),
    (re.compile(r"</?div[\s>]", re.I), "<div> 会被改写，请用 <section>"),
    (re.compile(r"<link[\s>]", re.I), "<link> 标签（外部 CSS/字体）会被过滤"),
    (re.compile(r"<meta[\s>]", re.I), "<meta> 标签会被过滤"),
    (re.compile(r"<iframe[\s>]", re.I), "<iframe> 不被支持"),
    (re.compile(r"<form[\s>]", re.I), "<form> 不被支持"),
    (re.compile(r"<input[\s>]", re.I), "<input> 不被支持"),
    (re.compile(r"\sclass\s*=", re.I), "class 属性会被剥离，请用内联 style"),
    (re.compile(r"\sid\s*=", re.I), "id 属性会被剥离"),
    (re.compile(r"position\s*:\s*(fixed|absolute|sticky)", re.I),
     "position: fixed/absolute/sticky 不被支持"),
    (re.compile(r"float\s*:", re.I), "float 不被支持"),
    (re.compile(r"@media", re.I), "@media 媒体查询不被支持"),
    (re.compile(r"@keyframes", re.I), "@keyframes 动画不被支持"),
    (re.compile(r"@import", re.I), "@import 不被支持"),
    (re.compile(r"display\s*:\s*grid", re.I), "display:grid 不被支持，请用 flex"),
    (re.compile(r"var\s*\(\s*--", re.I), "CSS 变量 var(--x) 不被支持，请写死值"),
    (re.compile(r"url\s*\(\s*['\"]?https?://[^)]*\.(woff2?|ttf|otf|euf)", re.I),
     "外部字体 url() 不被支持"),
]

CJK_CHAR = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf]")
# 中文字后紧跟半角标点（应改全角）
HALF_PUNCT_AFTER_CJK = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf][,;!?]")
# 英文直引号
ASCII_QUOTE = re.compile(r"[\"']")
# 代码区特征
CODE_STYLE_HINT = re.compile(r"monospace|white-space\s*:\s*pre|courier|consolas|sf mono", re.I)
# 不参与正文粘贴的区域
SKIP_TAGS = {"head", "title", "style", "script", "meta", "link"}


class LeafSpanChecker(HTMLParser):
    """遍历 DOM 树，检查每个中文文本节点是否被 <span leaf> 包裹。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._stack = []
        self._leaf_depth = 0
        self._code_depth = 0
        self.leaf_count = 0
        self.unwrapped = []
        self.bad_punct = []

    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        is_leaf = tag == "span" and "leaf" in ad
        is_code = bool(CODE_STYLE_HINT.search(ad.get("style", "") or ""))
        if is_leaf:
            self.leaf_count += 1
            self._leaf_depth += 1
        if is_code:
            self._code_depth += 1
        self._stack.append((tag, is_leaf, is_code))

    def handle_endtag(self, tag):
        for i in range(len(self._stack) - 1, -1, -1):
            if self._stack[i][0] == tag:
                for _, was_leaf, was_code in self._stack[i:]:
                    if was_leaf:
                        self._leaf_depth -= 1
                    if was_code:
                        self._code_depth -= 1
                del self._stack[i:]
                break

    def handle_data(self, data):
        stripped = data.strip()
        if not stripped or not CJK_CHAR.search(stripped):
            return
        if any(t in SKIP_TAGS for t, _, _ in self._stack):
            return
        if self._leaf_depth == 0:
            parent = self._stack[-1][0] if self._stack else "(root)"
            snippet = stripped[:30] + ("..." if len(stripped) > 30 else "")
            self.unwrapped.append((snippet, parent))
        if self._code_depth == 0:
            if HALF_PUNCT_AFTER_CJK.search(stripped) or ASCII_QUOTE.search(stripped):
                snippet = stripped[:30] + ("..." if len(stripped) > 30 else "")
                self.bad_punct.append(snippet)


def run_validation(html, source_name="<input>"):
    errors = []
    warnings = []

    for rx, msg in BANNED_PATTERNS:
        count = len(rx.findall(html))
        if count:
            errors.append(f"{msg}（命中 {count} 处）")

    checker = LeafSpanChecker()
    try:
        checker.feed(html)
    except Exception as exc:
        warnings.append(f"HTML 解析中断: {exc}")

    has_cjk = bool(CJK_CHAR.search(html))
    if has_cjk and checker.leaf_count == 0:
        errors.append(
            "全文没有任何 <span leaf=\"\"> 包裹——"
            "粘贴到公众号后样式会大面积丢失"
        )
    elif checker.unwrapped:
        preview = "；".join(
            f"「{s}」(在 <{p}> 内)" for s, p in checker.unwrapped[:5]
        )
        warnings.append(
            f"{len(checker.unwrapped)} 处中文文本未被 <span leaf> 包裹，"
            f"样式可能丢失。例：{preview}"
        )

    if checker.bad_punct:
        preview = "；".join(f"「{s}」" for s in checker.bad_punct[:5])
        warnings.append(
            f"{len(checker.bad_punct)} 处正文疑似半角标点或英文引号，"
            f"应改中文全角（代码块内不计）。例：{preview}"
        )

    return errors, warnings, checker.leaf_count


def main():
    ap = argparse.ArgumentParser(description="微信公众号 HTML 合规校验")
    ap.add_argument("file", nargs="?", help="HTML 文件路径")
    ap.add_argument("--stdin", action="store_true", help="从标准输入读取")
    args = ap.parse_args()

    if args.stdin or not args.file:
        html = sys.stdin.read()
        name = "<stdin>"
    else:
        with open(args.file, encoding="utf-8", errors="replace") as f:
            html = f.read()
        name = args.file

    errors, warnings, leaf_n = run_validation(html, name)

    print(f"📋 公众号 HTML 合规校验: {name}")
    print(f"   <span leaf> 包裹: {leaf_n} 处")

    if errors:
        print(f"\n❌ ERROR x{len(errors)}（必须修复，否则粘贴后失效）:")
        for e in errors:
            print(f"   - {e}")

    if warnings:
        print(f"\n⚠️  WARNING x{len(warnings)}（建议检查）:")
        for w in warnings:
            print(f"   - {w}")

    if not errors and not warnings:
        print("\n✅ 完全合规，可直接粘贴到公众号编辑器")
    elif not errors:
        print("\n✅ 无致命问题，可粘贴（warning 请人工确认）")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
