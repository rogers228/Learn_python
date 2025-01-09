from io import StringIO

def test1():
    with open('test.py', 'r', encoding='utf-8') as f:
        content = f.read() # 讀取文件內容
    print(content)
    file_object = StringIO(content) # 將文件內容包裝成一個 StringIO 對象
    namespace = {} # 創建一個空的命名空間
    exec(file_object.read(), namespace) # 執行StringIO 存至 namespace
    dic_new = namespace.get('dic')
    print(dic_new)
    ans = namespace.get('int_a')
    print(ans)

if __name__ == '__main__':
    test1()