import pandas as pd

def test1():
    # 先建立空白 再加入資料
    new_row = {'成品編號':'PVS09', '圖號':'TEST', '版次':'A1', '工程品名':'V38'}
    df = pd.DataFrame(None, columns = list(new_row.keys())) # None dataframe
    df = df.append(new_row, ignore_index=True)
    print(df)
    # append 即將停用

def test2():
    # 一次建立
    new_row = {'成品編號':'PVS09', '圖號':'TEST', '版次':'A1', '工程品名':'V38'}
    df = pd.DataFrame([list(new_row.values())], columns = list(new_row.keys())) # None dataframe
    print(df)

def test3():
    # 先建立空白 再加入資料
    # 使用 concat
    new_row = {'成品編號':'PVS09', '圖號':'TEST', '版次':'A1', '工程品名':'V38'}
    df_none = pd.DataFrame(None, columns = list(new_row.keys())) # None dataframe
    df_row = pd.DataFrame([list(new_row.values())], columns = list(new_row.keys()))
    df = pd.concat([df_none, df_row])
    print(df)


def test4():
    # 先建立空白 再加入資料
    # 新資料僅一部分的欄位
    # 使用 concat
    dic_columns = {'成品編號':'PVS09', '圖號':'TEST', '版次':'A1', '工程品名':'V38'}
    df_none = pd.DataFrame(None, columns = list(dic_columns.keys())) # None dataframe
    # print(df_none)
    new_row = {'成品編號':'PVS15', '圖號':'PVS15-012'}
    lis_row = list(map(lambda key: new_row.get(key,'') , list(dic_columns.keys())))
    # print(lis_row)
    df_row = pd.DataFrame([lis_row], columns = list(dic_columns.keys()))
    # print(df_row)
    df = pd.concat([df_none, df_row])
    print(df)

if __name__ == '__main__':
    test4()