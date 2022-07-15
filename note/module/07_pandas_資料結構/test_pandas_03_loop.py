    df = pd.DataFrame(x_lis, columns=x_tit_n) #list to pandas
    for i, r in df.iterrows(): # index, row
        print('index{0}, 圖號:{1}'.format(i, r['圖號']))




for i in range(len(df.index)):
    print(df.iloc[i, 0])
    print(df.iloc[i]['品號'])