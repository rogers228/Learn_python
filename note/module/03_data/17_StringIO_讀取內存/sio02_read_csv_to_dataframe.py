# 記憶體(內存)String
from io import StringIO
import pandas as pd

def test1():
    csvString = """
        type, name,  weights,  min,  max
        1,    lower,       0, 0.25, 0.35
        2,    middle,      4, 0.35, 0.70
        3,    normal,     42, 0.70, 0.90
        4,    buzz,       44, 0.90, 1.00
        5,    high,        8, 1.00, 1.10
        6,    higher,      1, 1.12, 1.50
        7,    bigger,      0, 1.50, 2.00
    """
    csvStringIO = StringIO(csvString)
    df = pd.read_csv(csvStringIO, sep=',')
    for i, e in enumerate(df.columns.tolist()):
        df.columns.values[i] = e.strip()
    str_columns= ['name']
    df[str_columns] = df[str_columns].apply(lambda e: e.str.strip()) # 移除空白

    print(df)
    print(df.dtypes)
    print(df.columns.tolist())
    print(df['name'].tolist())
    csvStringIO.close() # 關閉 清除內存

if __name__ == '__main__':
    test1()