def func_print():
    print('this is func')

def user_func_with_string():
    # 以字串來操作函數
    dic = {'func_print': func_print}
    func = dic['func_print'] 
    func()
