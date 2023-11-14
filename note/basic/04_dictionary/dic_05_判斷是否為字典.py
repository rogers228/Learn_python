import json
def test1():
    a = {5:5}
    if isinstance(a, dict):
        print('a is dic')
    else:
        print('a is not dic')

def test2():
    str_kwargs = '{"message": "yeohse"}'
    dic_kwargs = json.loads(str_kwargs)
    if not isinstance(dic_kwargs, dict):
        print('type error! dic_kwargs is not dictionary')
    print('ok')

if __name__ == '__main__':
    test2()