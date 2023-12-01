

def test1():
    # 以value找key  僅找到第一個

    cds_act_method = {356: 'test_func'}

    # 透過字典推導式找到對應的鍵
    # next() 函數用於獲取迭代器中的下一個元素

    desired_value = 'test_func'
    matching_key = next(key for key, value in cds_act_method.items() if value == desired_value)
    print(matching_key)

if __name__ == '__main__':
    test1()