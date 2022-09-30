from io import StringIO
import pandas as pd

def test1():
    # CSV String with out headers
    csvString = """
    Spark,  25000, 50 Days,2000
    Pandas, 20000, 35 Days,1000
    Java  , 15000,        , 800
    Python, 15000, 30 Days,  500
    PHP   , 18000, 30 Days,  800
    """
    # Convert String into StringIO
    csvStringIO = StringIO(csvString)
    columns =['Course','Fee','Duration','Discount']
    df = pd.read_csv(csvStringIO, sep=',', header=None,names=columns)

    df[['Course']] = df[['Course']].apply(lambda e: e.str.strip()) # 移除空白
    print(df)
    print(df.dtypes)


if __name__ == '__main__':
    test1()