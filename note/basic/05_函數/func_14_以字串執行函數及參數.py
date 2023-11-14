import json

def test1():
    act_code = 355 # func key can be string or int
    dic_func = {355: myfunc} # func
    func = dic_func.get(act_code, None) # 尋找應執行的方法
    str_kwargs = '{"age": 15, "message": "test"}'
    dic_kwargs = json.loads(str_kwargs)
    func(dic_kwargs)

def myfunc(dic_kwargs):
    # check key
    lis_args = ['age', 'message'] # dic_kwargs 應包含的 key
    for key in lis_args:
        if key not in list(dic_kwargs.keys()):
            raise TypeError(f'{key} key is not find!') # 找不到

    # run code
    message = dic_kwargs['message']
    print(message)


if __name__ == '__main__':
    test1()