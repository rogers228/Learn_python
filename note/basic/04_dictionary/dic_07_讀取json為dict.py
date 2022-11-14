import json

def test1():

    # 讀取json為dict
    json_file = r'C:\Users\user\Dropbox\yshr\instance\prodect_model\P5De1eGLnnTfMWI2jrsi.json'
    with open(json_file , mode='r', encoding='utf-8') as json_file:
        dic = json.load(json_file)
    print(type(dic))
    # print(dic) # 不好觀看架構

    # 若有需要 就可將 dic 轉 json 格式 方便觀看架構
    json_s = json.dumps(dic, indent=4, ensure_ascii=False)
    print(json_s)


if __name__ == '__main__':
    test1()
