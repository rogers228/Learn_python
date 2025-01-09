df.drop([0], inplace=True)


df.drop(['a'], axis = 0, inplace = True)


axis: 1 代表列 (垂直)
axis: 0 代表行 (水平)


inplace 引數設定為 True 時，列將從原始 DataFrame 中刪除；否則，將返回原始 DataFrame 的副本



df_all.drop(['rd02'], axis = 1, inplace = True) #刪除欄