import traceback  # 預設模組不需要安裝

def main():
    try:
        a = 1/0
    except Exception as e:
        traceback.print_exc()  # 將顯示完整錯誤，如同編譯錯誤顯示


def test1(): # 檢查型別 引發錯誤
    payload = 1 # not dict
    try:
        if not isinstance(payload, dict):
            raise TypeError("Variable must be a dictionary")
    except Exception as e:
        traceback.print_exc()  # 將顯示完整錯誤，如同編譯錯誤顯示

def test2():
    try:
        result = 10 / 0
    except Exception as e:
        error_message = str(e) # 捕捉所有異常並將異常物件轉換為字串
        print(f'發生錯誤: {error_message}')

if __name__ == '__main__':
    test2()