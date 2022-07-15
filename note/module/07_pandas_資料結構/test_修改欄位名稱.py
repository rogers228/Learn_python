def test5():
    col_1 = ['pd','pdf','mb02','mb03']    
    lis_1 = [
            ['Rogers','PARENT',1,'A'],
            ['Allen','Rogers',2,'A'],
            ['Jessis','Rogers',3,'B'],
            ['Jay','Rogers',4,'O'],
            ['Allen','Jay',5,'A'],
            ]
    df = pd.DataFrame(lis_1, columns = col_1) # 建立 DataFrame
    print(df)
    
    new_columns = {'pd': 'new_pd', 'mb02': 'MB002'}
    df = df.rename(columns=new_columns)
    print(df)