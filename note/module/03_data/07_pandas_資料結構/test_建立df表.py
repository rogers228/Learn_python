import pandas as pd

def test1():
    lis = [
            ['Rogers',32,'A'],
            ['Allen',5,'A'],
            ['Jessis',28,'B'],
            ['Jay',18,'O'],
            ]
    col_s = ['Name','Age','Bud']
    df = pd.DataFrame(lis, columns = col_s) # 建立 DataFrame
    print(df)

def test2():
    col_s = ['Name','Age','Bud']
    df = pd.DataFrame(None, columns = col_s) # 建立空白 DataFrame
    print(df)
    if len(df.index) == 0:
        print('df is None')

def test3():
    data = {
        'Name': ['Tom', 'Joseph', 'Krish', 'John'],
        'Age': [20, 21, 19, 18]}
    df = pd.DataFrame(data)
    print(df)
if __name__ == '__main__':
    test3()