import json

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True

def test1():
    file = 'test.json'
    with open(file, encoding='utf-8') as data_file:
        json_str = data_file.read()

    if not is_json(json_str):
        # json 格式不合法
        print('json error:')
        print(json_str)
        return

    print(json_str)
    dic_data = json.loads(json_str) # 轉dic
    print(dic_data) 

def test2():
    # print(is_json("{}"))                          #prints True
    # print(is_json("{asdf}"))                      #prints False
    # print(is_json('{ "age":100}'))                #prints True
    # print(is_json("{'age':100 }"))                #prints False
    # print(is_json("{\"age\":100 }"))              #prints True
    # print(is_json('{"age":100 }'))                #prints True
    print(is_json('{"foo":[5,6.8],"foo":"bar"}')) #prints True

if __name__ == '__main__':
    test1()