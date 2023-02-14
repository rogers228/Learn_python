您可以使用 python-docx 和 python-markdown2 套件來將 docx 檔案轉換為 markdown。

首先，您需要安裝這兩個套件：

Copy code
pip install python-docx
pip install python-markdown2
然後，您可以使用以下代碼來將 docx 檔案轉換為 markdown：

python
Copy code

```py
import docx
import markdown2

def convert_docx_to_markdown(docx_file):
    # 讀取 docx 檔案
    doc = docx.Document(docx_file)

    # 建立一個空的 markdown 文字串
    markdown_text = ""

    # 遍歷每一個段落
    for paragraph in doc.paragraphs:
        # 將段落文字轉換為 markdown 格式
        markdown_text += markdown2.markdown(paragraph.text) + "\n"

    return markdown_text

# 使用您的 docx 檔案名稱取代 "document.docx"
markdown_text = convert_docx_to_markdown("document.docx")

# 將 markdown 文字寫入檔案
with open("document.md", "w") as f:
    f.write(markdown_text)
```