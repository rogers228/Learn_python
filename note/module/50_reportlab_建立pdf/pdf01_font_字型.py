from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# 未註冊中文字型 將無法顯示

def test1():
    print('test1')
    # 註冊字型
    pdfmetrics.registerFont(TTFont("MicrosoftJhengHei", "msjh.ttf"))  # 微軟正黑體
    pdfmetrics.registerFont(TTFont("Verdana", "Verdana.ttf"))        # Verdana

    c = canvas.Canvas("test.pdf")

    # 設定字型大小
    chinese_font = "MicrosoftJhengHei"
    english_font = "Verdana"
    font_size = 12

    # 繪製中文
    c.setFont(chinese_font, font_size)
    c.drawString(100, 750, "這是中文文字，使用微軟正黑體。")

    # 繪製英文與數字
    c.setFont(english_font, font_size)
    c.drawString(100, 720, "This is English and numbers: 12345 using Verdana.")
    c.save()

if __name__ == '__main__':
    test1()
    print('ok')