import re
from re import finditer

def test1():

    with open('test1.txt', "r", encoding='utf-8') as f:
        source = f.read() + '\n'
    print(source)
    print('-----')
    

    pattern = re.compile(r"#\s*include\s*{{\s*(.*)}}")

    lis_py = re.findall(pattern, source)
    lis_py = [e.strip() for e in lis_py] # 去除空格
    # print(lis_py)

    lis_include = [e.group() for e in list(finditer(pattern, source))]
    # print(lis_include)

    new_str = source[:]
    for file, str_replace in zip(lis_py, lis_include):
        # print(file, str_replace )
        new_str = new_str.replace(str_replace, 'ddddd')

    print('new_str')
    print(new_str)
#     source
# Target
if __name__ == '__main__':
    test1()
