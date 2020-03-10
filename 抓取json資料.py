import json
import requests
def main():
    examp_5() #執行

def examp_5():
    #讀取json檔案
    file = r'data_json.json'
    with open(file) as f:
        data_json = json.load(f)
    field_json = list(data_json[0].keys()) #欄位列表
    print(field_json)
    print('\n')
    print(len(data_json))
    print('County\t'+'SiteName\t'+'PM2.5\t'+'Status')
    j = data_json #指針
    for i in range(len(j)):
        print('{0}\t{1}\t{2}\t{3}'.format(
            j[i]['County'],
            j[i]['SiteName'],
            j[i]['PM2.5'],
            j[i]['Status']))
        
    print('\nexamp_5 ok')
def examp_4():
    #儲存josn檔案
    r = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json", verify='certs.pem')
    print(r.status_code) #回傳狀態碼
    data_json = r.json()
    with open("data_json.json", "w") as f:
        json.dump(data_json, f, ensure_ascii=False)
    print('\nexamp_4 ok')
    
def examp_3():
    #讀取網路json空氣品質指標(AQI)
    r = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json", verify='certs.pem')
    print(r.status_code) #回傳狀態碼
    data_json = r.json()
    #field_json = list(data_json[0].keys()) #欄位列表
    #print(field_json)#欄位列表
    print('\n')
    print('County\t'+'SiteName\t'+'PM2.5\t'+'Status')

    j = data_json #指針
    for i in range(len(data_json)):
        print('{0}\t{1}\t{2}'.format(
            j[i]['County'],
            j[i]['SiteName'],
            j[i]['PM2.5'],
            j[i]['Status']))
    print('\nexamp_3 ok')
    
def examp_2():
    #儲存josn
    data_json =[{'col1':'value1-1', 'col2':'value1-2'}, {'col1':'value1-2','col2':'value2-2'},{'城市':'台中'}]
    with open('data_json.txt', 'w') as jf:
        json.dump(data_json, jf, ensure_ascii=False)
    print('examp_2 ok')

    
def examp_1():
    #json 格式為List內涵Dict[{},{},{}]
    data_json =[{'col1':'value1-1', 'col2':'value1-2'}, {'col1':'value1-2','col2':'value2-2'}]
    field_json = list(data_json[0].keys()) #欄位列表
    print(field_json)
    print('\n')
    for i in range(len(data_json)):
        print(data_json[i]) #取出List裡的元素Dict
        print(data_json[i]['col1']) #取出List裡的元素Dict

def examp_9():
    r = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json", verify='certs.pem')
    print(r.status_code) #回傳狀態碼
    data_json = r.json()
    print(type(data_json))
    print('\n')
    
    with open('data_json.txt', 'w') as json_file:
        json.dump(data_json, json_file)
    print('ok')

    '''
    for r in data_json:
        print(r["County"], r["SiteName"], r["PM2.5"])
    '''

if __name__ == '__main__':
    main()
