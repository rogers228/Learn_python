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



def test2():
    #          類別   名稱      權重    最低比率     最高比率     說明 
    columns =['type','name','weights','min_scale','max_scale', 'help']
    str_columns=['name','help']
    csvString = """
    1,  lower,   0, 0.25, 0.35, 速限的25%以上速限的35%以下很低的速度通常是愈到不正常的情況
    2,  middle,  4, 0.35, 0.70, 速限的35%以上限速70%以下介於常速與低速之間
    3,  normal, 42, 0.70, 0.90, 速限的70%以上限速90%以下
    4,  buzz,   44, 0.90, 1.00, 限速的90%以上限速100以下
    5,  high,    8, 1.00, 1.10, 超過限速低於限速110%以下
    6,  higher,  1, 1.12, 1.50, 超過限速112%以上150%以下
    7,  bigger,  0, 1.50, 2.00, 超過限速150%以上200%以下
    """
    csvStringIO = StringIO(csvString)
    df = pd.read_csv(csvStringIO, sep=',', header=None,names=columns)
    df[str_columns] = df[str_columns].apply(lambda e: e.str.strip()) # 移除空白
    # self.speed_data = df
    # debug
    df = df[['type','name','weights','min_scale','max_scale']]
    print(df)
    print(df.dtypes)

if __name__ == '__main__':
    test2()