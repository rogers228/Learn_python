import json
import pandas as pd

def test1():
    # csv to dataframe
    csvfile = r'test.csv'
    df = pd.read_csv(csvfile, sep = ',',encoding='utf-8')
    print(df)

    # dataframe  to  json
    json_str = '{"data":' + df.to_json(orient="records") + '}' 


    #檢視用
    dic_data = json.loads(json_str)  # string-json variable to dict
    print(dic_data)

    json_s = json.dumps(dic_data, indent=4, ensure_ascii=False) # dict to format json
    print(json_s)


    # json_s_min = json.loads(jsmin(json_s)) #to min json
    # print(json_s_min)

def test2():
    csvfile = r'test.csv'
    df = pd.read_csv(csvfile, sep = ',',encoding='utf-8')
    print(df)

    df_a = df.loc[:2]
    print(df_a)
    df_b = df.loc[3:]
    print(df_b)

if __name__ == '__main__':
    test2()