import json
import pandas as pd

def test1():
    csvfile = r'test.csv'
    df = pd.read_csv(csvfile, sep = ',',encoding='utf-8')
    print(df)

    # df分解為 a, b
    df_a = df.loc[:2]
    print(df_a)
    df_b = df.loc[3:]
    print(df_b)

def test2():
    df = pd.read_csv('test.csv', sep = ',',encoding='utf-8')
    print(df)
    # df分解為 a, b
    df_a = df.loc[:2]
    df_b = df.loc[3:]
    # df_b = None
    print(df_a)
    print(df_b)
    df_insert = pd.read_csv('test2.csv', sep = ',',encoding='utf-8')
    print(df_insert)
    # 插入在a, b, 中間
    df_new = df_a.append(df_insert, ignore_index = True)
    df_new = df_new.append(df_b, ignore_index = True)
    print(df_new)

if __name__ == '__main__':
    test2()