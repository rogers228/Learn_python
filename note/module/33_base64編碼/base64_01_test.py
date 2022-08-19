import base64

def test1():
    s = 'Hello World你好' # 源字串
    print(s)

    b = s.encode('UTF-8') # 轉碼為utf-8
    print(b)

    bytes_encode = base64.b64encode(b) # 轉碼為base64
    print(bytes_encode)

if __name__ == '__main__':
    test1()