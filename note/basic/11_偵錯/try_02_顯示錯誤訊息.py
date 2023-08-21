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

if __name__ == '__main__':
    test1()