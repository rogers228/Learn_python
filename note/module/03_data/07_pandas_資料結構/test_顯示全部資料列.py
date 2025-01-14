pd.set_option('display.max_rows', df.shape[0]+1) # 顯示最多列
pd.set_option('display.max_columns', None) #顯示最多欄位


print(df_w.head(5)) # 列出前n筆的表格