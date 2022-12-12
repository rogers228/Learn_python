import re
from re import finditer

def find_content(source):
    # 找到特定標籤之內的內容
    # {{ content }}
    # ....
    # {{ end content }}
    result = ''
    pattern_statr = re.compile(r"#\s*{{\s*content\s*}}")
    pattern_end = re.compile(r"#\s*{{\s*end\s*content\s*}}")
    if not bool(re.search(pattern_statr, source)):
        print('缺少 # {{ content }} 標籤，無法匹配')
        return result
    if not bool(re.search(pattern_end, source)):
        print('缺少 # {{ end content }} 標籤，無法匹配')
        return result
    tag_start = re.search(pattern_statr, source)
    tag_end = re.search(pattern_end, source)
    result = source[tag_start.end(): tag_end.start()]
    return result

def test1():
    with open('test1.txt', "r", encoding='utf-8') as f:
        source = f.read() + '\n'
    print(find_content(source))

if __name__ == '__main__':
    test1()
