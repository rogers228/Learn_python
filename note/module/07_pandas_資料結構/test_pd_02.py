import pandas as pd

# 匯入csv
df = pd.read_csv(r'C:\Users\user\Documents\Rogers\Py\flask_test\flaskweb_1\instance\c_sg.csv', sep = ',',encoding='utf-8')

df = df.fillna('') # 填充NaN為空白

# print(df.head(3)) # 列出前n筆的表格

# 文字轉時間
df['sg06'] = pd.to_datetime(df['sg06'], format='%Y%m%d%H%M%S', errors='ignore')
df['sg07'] = pd.to_datetime(df['sg07'], format='%Y%m%d%H%M%S', errors='ignore')
# print(df.head(3)) # 列出前n筆的表格

# # 增加星期欄位
# df['wd'] = df['rd03'].dt.dayofweek
# df['wd'] = df['wd'].replace([0,1,2,3,4,5,6],
#     ['(一)','(二)','(三)','(四)','(五)','(六)','(日)']
# )

# 時間格式化
df['sg06'] = df['sg06'].dt.strftime('%Y/%m/%d %H:%M')
df['sg07'] = df['sg07'].dt.strftime('%Y/%m/%d %H:%M')
# print(df.head(3)) # 列出前n筆的表格


# 替換id為名稱
df['sg05'] = df['sg05'].replace([0,1,2,3,4,5,6,7,8,9,10,11,12],
    ['未設定','特休假','公假','婚假','喪假','產假','病假','事假','陪產假','產檢假','育嬰假','留職停薪','防疫照顧假']
)
df['sg10'] = df['sg10'].replace([0,1,2],['未簽','核准','退回'])

# print(df.head(3)) # 列出前n筆的表格

df_w = df.loc[(df['ps02'] == 'AA0031') & (df['sg05'] == '特休假')] # 篩選
print(df_w.head(5)) # 列出前n筆的表格
# print(df_w)

# df_list = df_w.values.tolist()
# print(df_list)