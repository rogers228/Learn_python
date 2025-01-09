from urllib.request import urlopen
import requests
import json

def test2():
    # 直接使用請求 request post
    origin = "http://www.yeoshe.tw"
    url = f'{origin}/api_sider'
    front_json = {'apicode': 'kurPakWQ4esL'}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(front_json), headers=headers)
    dic = r.json()
    print(dic)
    print(type(dic))

def test1():
    # 擷取網頁原始碼 (經證實 非經過前端渲染 僅原始html)
    myurl = "http://www.yeoshe.tw/#page=model&code=QlcKgmzvappxALwARX8G"
    html = urlopen(myurl).read().decode('utf-8') # 擷取網頁原始碼 (並非經過前端渲染)
    print(html)

if __name__ == '__main__':
    test2()