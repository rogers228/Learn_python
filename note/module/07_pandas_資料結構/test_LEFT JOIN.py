def test4():
    # df left join
    lis1 = [
            ['Rogers',32,'A'],
            ['Allen',5,'A'],
            ['Jessis',28,'B'],
            ['Jay',18,'O'],
            ]
    col1 = ['Name','Age','Bud']
    df1 = pd.DataFrame(lis1, columns = col1) # 建立 DataFrame
    # print(df1)

    lis2 = [
            ['Allen','C123'],
            ['Jessis','N220'],
            ['Andy','B127'],
            ]
    col2 = ['Name','No']
    df2 = pd.DataFrame(lis2, columns = col2) # 建立 DataFrame
    # print(df2)

    df = df1.merge(df2, on='Name', how='left') # left join
    df = df.fillna('') # 填充NaN為空白
    print(df)