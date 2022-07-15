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
    
if __name__ == '__main__':
    test1()