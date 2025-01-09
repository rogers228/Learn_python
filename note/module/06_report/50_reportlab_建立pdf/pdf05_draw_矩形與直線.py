from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import *  # 匯入顏色

# aliceblue
# antiquewhite
# aqua
# aquamarine
# azure
# beige
# bisque
# black
# blanchedalmond
# blue
# blueviolet
# brown
# burlywood
# cadetblue
# chartreuse
# chocolate
# coral
# cornflowerblue
# cornsilk
# crimson
# cyan
# darkblue
# darkcyan
# darkgoldenrod
# darkgray
# darkgreen
# darkkhaki
# darkmagenta
# darkolivegreen
# darkorange
# darkorchid
# darkred
# darksalmon
# darkseagreen
# darkslateblue
# darkslategray
# darkturquoise
# darkviolet
# deeppink
# deepskyblue
# dimgray
# dodgerblue
# firebrick
# floralwhite
# forestgreen
# fuchsia
# gainsboro
# ghostwhite
# gold
# goldenrod
# gray
# green
# greenyellow
# honeydew
# hotpink
# indianred
# indigo
# ivory
# khaki
# lavender
# lavenderblush
# lawngreen
# lemonchiffon
# lightblue
# lightcoral
# lightcyan
# lightgoldenrodyellow
# lightgray
# lightgreen
# lightpink
# lightsalmon
# lightseagreen
# lightskyblue
# lightslategray
# lightsteelblue
# lightyellow
# lime
# limegreen
# linen
# magenta
# mediumaquamarine
# mediumblue
# mediumorchid
# mediumpurple
# mediumseagreen
# mediumslateblue
# mediumspringgreen
# mediumturquoise
# mediumvioletred
# midnightblue
# mintcream
# mistyrose
# moccasin
# navajowhite
# navy
# oldlace
# olive
# olivedrab
# orange
# orangered
# orchid
# palegoldenrod
# palegreen
# paleturquoise
# palevioletred
# papayawhip
# peachpuff
# peru
# pink
# plum
# powderblue
# purple
# red
# rosybrown
# royalblue
# saddlebrown
# salmon
# sandybrown
# seashell
# sienna
# silver
# skyblue
# slateblue
# slategray
# snow
# springgreen
# steelblue
# tan
# teal
# thistle
# tomato
# turquoise
# violet
# wheat
# white
# whitesmoke
# yellow
# yellowgreen

def test1():

    # page setting
    (page_width, page_height) = (210 * mm, 297 * mm) # A4 mm

    # margin
    margin_left   = 15 * mm
    margin_right  = 15 * mm
    margin_top    = 20 * mm
    margin_bottom = 20 * mm

    content_width  = page_width  - margin_left - margin_right
    content_height = page_height - margin_top  - margin_bottom

    c = canvas.Canvas('test.pdf', pagesize=(page_width, page_height))

    # 設定線條顏色與粗細
    c.setDash(6, 3) # 設定為虛線
    c.setStrokeColor(black) # 設定線條顏色
    c.setLineWidth(1)       # 設定線條粗細 (單位是 points)
    c.rect(margin_left, margin_bottom, content_width, content_height) # 矩形
    c.setDash() # 清除虛線
    c.save()

def test2():
    # page setting
    (page_width, page_height) = (210 * mm, 297 * mm) # A4 mm

    # margin
    margin_left   = 15 * mm
    margin_right  = 15 * mm
    margin_top    = 20 * mm
    margin_bottom = 20 * mm

    content_width  = page_width  - margin_left - margin_right
    content_height = page_height - margin_top  - margin_bottom

    c = canvas.Canvas('test.pdf', pagesize=(page_width, page_height))

    # 設定線條顏色與粗細
    c.setLineWidth(0.5)       # 設定線條粗細 (單位是 points)
    c.line(margin_left, page_height - margin_top, page_width - margin_right, page_height - margin_top) # 直線
    c.save()

if __name__ == '__main__':
    test2()
    print('ok')