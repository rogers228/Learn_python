from io import StringIO
import markdown
from markdown.extensions.tables import TableExtension

# table 表格
# abbr  HTML abbr tag 工具說明  屬標移動到該處停留一會，會出現工具說明
# Attribute Lists 允許在md中使用特殊語法 輸出html屬性標籤 例如id, class, a href 於前端應用有相當大的助益
# Definition Lists
# Footnotes 註腳 例如本文中有 注1 注2  在本文底可以找到註解


def test1():
    # 使用讀取md檔， 直接讀取檔
    md_file = r'input.md'
    with open(md_file, encoding='utf8') as f:
        md_str = f.read()
    print(md_str)
    print('-----------------')
    # extensions=[TableExtension(use_align_attribute=True)]  # 轉換table
    extensions=['attr_list'] # 轉換屬性
    html = markdown.markdown(md_str, extensions=extensions) 
    print(html)

def multext(pystr):
    # pystr 多行文字 轉存文字
    # 需引用 from io import StringIO
    s = StringIO() # 建立 StringIO 物件
    s.write(pystr) # 在內存建立文字
    s.seek(0)
    lis = s.readlines()
    lis = [s.strip() for s in lis] # 去除空白
    s.close() # 關閉
    return "\n".join(lis)

def test2():
    # table
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
    
    # html = markdown.markdown(md_str) # 不使用拓展
    extensions=[TableExtension(use_align_attribute=True)]  # 轉換table
    html = markdown.markdown(md_str, extensions=extensions)
    print(html)

def test3():
    # 區塊屬性 (id & class)
    # 為一個區塊建立id or class
    # 故語法應在區塊的最後一行並且獨立
    md_str = multext("""
        # hi

        this is test

        ## table
        | 名稱 | 說明 | 備註 |
        | ------------ | ------------- |  ------------- |
        |id       |使用者idkey         |                |
        |userno   |使用者工號           |                |

        yeoshe
        {: #myid .myclass }

        """)

    print(md_str)
    print('-----------------')
    
    # html = markdown.markdown(md_str) # 不使用拓展
    extensions = []
    extensions.append(TableExtension(use_align_attribute=True))  # 轉換table
    extensions.append('attr_list') # 轉換屬性

    html = markdown.markdown(md_str, extensions=extensions) 
    print(html)

def test4():
    # 內連屬性 以圖片為例
    # attr應緊接 不可空格
    md_str = multext("""
        # hi

        this is a image

        ![mytext](http://123){: #myid .myclass }

        """)

    print(md_str)
    print('-----------------')
    
    # html = markdown.markdown(md_str) # 不使用拓展
    extensions = []
    # extensions.append(TableExtension(use_align_attribute=True))  # 轉換table
    extensions.append('attr_list') # 轉換屬性

    html = markdown.markdown(md_str, extensions=extensions) 
    print(html)


def test5():
    # 程式碼片段
    md_str = multext("""
        # hi

        this is a image

        ```
        this is code
        ```

        """)

    print(md_str)
    print('-----------------')
    
    # html = markdown.markdown(md_str) # 不使用拓展
    extensions = []
    # extensions.append(TableExtension(use_align_attribute=True))  # 轉換table
    extensions.append('fenced_code') # 程式碼片段

    html = markdown.markdown(md_str, extensions=extensions) 
    print(html)
if __name__ == '__main__':
    test5()