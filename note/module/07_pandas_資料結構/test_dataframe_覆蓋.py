import json
import pandas as pd

def test1():

    df = pd.read_csv('test.csv', sep = ',',encoding='utf-8')
    print(df)

    df_b = pd.read_csv('test2.csv', sep = ',',encoding='utf-8')
    print(df_b)

    df = df_b # 覆蓋
    print(df)

if __name__ == '__main__':
    test1()