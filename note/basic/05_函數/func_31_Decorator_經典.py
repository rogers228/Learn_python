
def run_first(func): # 裝飾器  先執行
    def jacket(*args):    # 夾克 外殼 接受參數
        print('hi, i am jacket.')
        result = func(*args) # 執行原函數 並取得結果
        return result # 回傳結果

    return jacket # 執行夾克


@run_first # 原函數穿上夾克
def find(my_int=100):
    # print('my_int:', my_int)
    lis = []
    for i in range(1, my_int+1):
        # print(i)
        if not (i % 2 == 0 or i % 3 == 0):
            lis.append(i)
    return lis

def test1():
    lis = find(45)
    print(lis)

if __name__ == '__main__':
    test1()