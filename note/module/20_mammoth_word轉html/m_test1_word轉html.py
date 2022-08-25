import mammoth # docx 轉 html

def test1():
    style_map = """
    p[style-name='heading 1'] => h1:fresh
    p[style-name^='Heading'] => h2:fresh
    p[style-name='Subtle Reference'] => em:fresh
    """

    docx_fiel = r'C:\Users\user\Desktop\test.docx'
    with open(docx_fiel, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        # result = mammoth.convert_to_html(docx_file, style_map=style_map)
        # result = mammoth.convert_to_html(docx_file, style_map=style_map, include_default_style_map=False)

        html = result.value # The generated HTML
        messages = result.messages # Any messages, such as warnings during conversion

    print(html)

def test2():
    docx_file = r'C:\Users\user\Desktop\test.docx'
    html_file = r'C:\Users\user\Desktop\test.html'
    docx2html(docx_file, html_file)

def docx2html(docx_file, html_file):
    with open(docx_file, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value # The generated HTML
        messages = result.messages # Any messages, such as warnings during conversion
    h = open(html_file,"w", encoding='utf-8')
    h.write(html)
    h.close()
    print('finish')


if __name__ == '__main__':
    test2()
    print('ok')