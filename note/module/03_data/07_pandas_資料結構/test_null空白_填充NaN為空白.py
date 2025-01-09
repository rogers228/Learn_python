df = df.fillna('') # 填充NaN為空白

#填充特定欄位
df[['a', 'b']] = df[['a','b']].fillna(value=0)


