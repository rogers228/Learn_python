# https://www.devdungeon.com/content/convert-markdown-html-python
import markdown

def test1():
    # Simple conversion in memory
    md_text = '# Hello\n\n**Text**'
    html = markdown.markdown(md_text)
    print(html)

if __name__ == '__main__':
    test1()