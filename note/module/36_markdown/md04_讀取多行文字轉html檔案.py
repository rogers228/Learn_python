from io import StringIO
import markdown
from markdown.extensions.tables import TableExtension

def multext(pystr):
    # pystr 多行文字 轉存文字
    # 需引用 from io import StringIO
    s = StringIO() # 建立 StringIO 物件
    s.write(pystr) # 在內存建立文字
    s.seek(0)
    lis = s.readlines()
    lis = [s.strip() for s in lis if s.strip()] # 去除空白及換行符
    s.close() # 關閉
    return "\n".join(lis)

def test1():
    # 直接使用python 三引號換行符號  會轉為markdown  code   是無法成功
    # 讀取多行文字更方便測試
    md_str = multext("""
        # hi

        this is test

        ## table
        | 名稱 | 說明 | 備註 |
        | ------------ | ------------- |  ------------- |
        |id       |使用者idkey         |                |
        |userno   |使用者工號           |                |
        """)

    print(md_str)
    print('-----------------')
    extensions=[TableExtension(use_align_attribute=True)]  # 轉換table
    html = markdown.markdown(md_str, extensions=extensions) 
    print(html)

if __name__ == '__main__':
    test1()