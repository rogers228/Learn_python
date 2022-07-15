ans = df_w.iloc[0] #首筆
print(ans['圖號']) #以欄位取值



df.reset_index(inplace=True) #重置索引

df = df.sort_index() #重新排序一下