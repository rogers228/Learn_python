from reportlab.pdfgen import canvas
from reportlab.lib.units import mm  # 匯入毫米單位

# x, y 座標系統的原點是紙張的左下角
# 邊界是使用座標系統的精確控制來達成的

def test1():
    print('test1')

    # page setting
    (page_width, page_height) = (210 * mm, 297 * mm) # A4 mm
    # print(page_width, page_height)

    # margin
    margin_left   = 15 * mm
    margin_right  = 15 * mm
    margin_top    = 20 * mm
    margin_bottom = 20 * mm

    content_width  = page_width  - margin_left - margin_right
    content_height = page_height - margin_top  - margin_bottom

    c = canvas.Canvas('test.pdf', pagesize=(page_width, page_height))
    c.rect(margin_left, margin_bottom, content_width, content_height)

    # # 繪製中文
    c.setFont("Helvetica", 12)

    x = margin_left
    y = page_height - margin_top

    c.drawString(x, y-12, "this is a test")

    c.save()

if __name__ == '__main__':
    test1()
    print('ok')