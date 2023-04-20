import markdown
from markdown.extensions.tables import TableExtension

def test1():
    markdown.markdownFromFile(
        input = r'C:\Users\user\Documents\Rogers\for_horse\readme.md',
        output= 'output.html',
        encoding='utf8',
    )
    print('finished')

def test2():
    # 使用拓展
    # 方能正確轉出表格
    # https://python-markdown.github.io/extensions/


    markdown.markdownFromFile(
        input = r'C:\Users\user\Documents\Rogers\for_horse\readme.md',
        output= 'output.html',
        encoding='utf8',
        extensions=[TableExtension(use_align_attribute=True)]
    )
    print('finished')

# 其他拓展
# table 表格
# abbr  HTML abbr tag 工具說明  屬標移動到該處停留一會，會出現工具說明
if __name__ == '__main__':
    test2()