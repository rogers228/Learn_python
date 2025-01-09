import base64

# 邊碼為base64
# 用途1 簡易加密
# 用途2 儲存資料，傳輸，特別是針對 特殊符號 轉義符


def encode_base64(input_string):
    utf8_bytes = input_string.encode('utf-8')
    base64_bytes = base64.b64encode(utf8_bytes)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string

def decode_base64(base64_string):
    base64_bytes = base64_string.encode('utf-8')
    utf8_bytes = base64.b64decode(base64_bytes)
    original_string = utf8_bytes.decode('utf-8')
    return original_string

def test1():
    mystr = 'fda123 dfds□'
    print('mystr:', mystr)
    base64_string = encode_base64(mystr)
    print('mystr to base64:', base64_string)

    print('base64 decode:', decode_base64(base64_string))

if __name__ == '__main__':
    test1()