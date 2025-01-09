

df.sort_values(by=['col1']) #單一欄位排序

df.sort_values(by=['col1', 'col2']) #多欄位排序

df.sort_values(by='col1', ascending=False) #反向

#含有不同型,將別無法排序
df['col1'] = df['col1'].apply(str) #將該欄位強制轉換為文字

#空白排在最前
#函數計算後排序

# 其他請參閱
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html