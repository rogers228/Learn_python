# 不好用，放棄

from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, format='A4', left=15, top=12, right=15, auto_page_break=True, bottom_margin=10):
        super().__init__(format=format)  # 初始化父類別
        self.set_margins(left=left, top=top, right=right)  # 設定邊界
        self.set_auto_page_break(auto=auto_page_break, margin=bottom_margin)
        self.add_font('MicrosoftJhengHei', '', 'msjh.ttf', uni=True)  # 微軟正黑體

    # 設定頁首
    def header(self):
        # self.set_font('Arial', 'B', 12)  # 設定字型
        self.set_font('MicrosoftJhengHei', size=12)  # 設定字型與大小  # 微軟正黑體
        self.cell(0, 10, '頁首有限公司', border=0, ln=True, align='C')  # 頁首置中
        self.ln(10)  # 添加空白行（控制頁首與主內容的間距）

    # 設定頁尾
    def footer(self):
        self.set_y(-15)  # 移動到頁面底部距離 15mm 的位置
        self.set_font('Arial', 'I', 10)  # 設定字型
        page_text = f'page: {self.page_no()}/{self.alias_nb_pages()}'
        self.cell(0, 10, page_text, border=0, align='R')  # 顯示頁碼，靠右

def test1():
    pdf = PDF()
    pdf.add_page()  # 新增頁面
    pdf.set_font('Arial', size=12)

    # 添加多行內容
    for i in range(1, 31):
        pdf.cell(0, 10, f"this is row {i}", ln=True)
        y = pdf.get_y()  # 取得當前 Y 座標
        pdf.line(15, y-1, 195, y-1)  # 繪製底線 (X1, Y1, X2, Y2)

    pdf.ln(1)  # 添加一個空行，避免內容過於貼近
    pdf.cell(0, 10, "data is over", ln=True, align='C')  # 添加文字，置中對齊
    pdf.output("test.pdf")



if __name__ == '__main__':
    test1()