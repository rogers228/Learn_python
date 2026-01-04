# textwrap

預設模組

用來換行字串

import textwrap
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(textwrap.fill(text, width=8))
ABCDEFGH
IJKLMNOP
QRSTUVWX
YZ

## initial_indent
第一行前面加縮排
textwrap.fill("hello world", width=20, initial_indent=">>> ")
>>> hello world

## subsequent_indent
從第二行開始加縮排
s = "Python textwrap can format long text across multiple wrapped lines"
print(textwrap.fill(s, width=20, subsequent_indent="    "))
Python textwrap can
    format long text
    across multiple
    wrapped lines

## break_long_words（預設 True）
是否強制切開太長單字
（例如 Base64 很長一段沒有空白 → 必須設 True，否則不會換行）

## break_on_hyphens（預設 True）
遇到 - 是否允許在那切行。