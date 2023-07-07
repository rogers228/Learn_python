import json5
# json5支援單行註解，多行註解 單引號, 雙引號, 陣列尾可逗號

def test1():
    # 開啟json5
    with open('json5.json5', 'r', encoding='utf-8') as f:
        dic = json5.load(f)
    print(dic) # 讀取為 dict

    json_s = json5.dumps(dic, indent = 4) # 將dict轉換為 json 方便觀看
    print(json_s)

def test2():
    # create json5
    dic = {
        'name': 'John', # 這是註解
        'age': 30,
        'city': 'New York'
    }

    with open('saveas.json5', 'w') as f:
        json5.dump(dic, f, indent=4)
    print('ok')

if __name__ == '__main__':
    test2()