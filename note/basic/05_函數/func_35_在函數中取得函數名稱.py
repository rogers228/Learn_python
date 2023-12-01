import inspect

def test_myfunction():
    # 獲取函數名稱
    curr_func_name = inspect.currentframe().f_code.co_name
    print(curr_func_name)
    print(type(curr_func_name))

if __name__ == '__main__':
    test_myfunction()