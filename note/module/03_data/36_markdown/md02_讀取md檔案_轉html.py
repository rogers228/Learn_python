import markdown
from markdown.extensions.tables import TableExtension

def test1():
    # 讀取檔案
    md_file = r'C:\Users\user\Documents\Rogers\for_horse\readme.md'
    with open(md_file, encoding='utf8') as f:
        md_text = f.read()

    print(md_text)
    html = markdown.markdown(md_text)
    print(html)


def test2():
    # 使用拓展
    # 方能正確讀取表格
    # https://python-markdown.github.io/extensions/

    md_file = r'C:\Users\user\Documents\Rogers\for_horse\readme.md'
    with open(md_file, encoding='utf8') as f:
        md_text = f.read()

    # print(md_text)
    html = markdown.markdown(md_text,
        extensions=[TableExtension(use_align_attribute=True)]
        )

    print(html)

if __name__ == '__main__':
    test2()