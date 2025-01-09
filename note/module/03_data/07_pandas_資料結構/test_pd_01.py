import pandas as pd

# 匯入csv
df = pd.read_csv(r'C:\Users\user\Documents\Rogers\Py\flask_test\flaskweb_1\instance\c_rd.csv', sep = ',',encoding='utf-8')

df = df.fillna('') # 填充NaN為空白

# print(df.head(3)) # 列出前n筆的表格

# 文字轉時間
df['rd03'] = pd.to_datetime(df['rd03'], format='%Y%m%d%H%M%S', errors='ignore')
# print(df.head(3)) # 列出前n筆的表格

# 增加星期欄位
df['wd'] = df['rd03'].dt.dayofweek
df['wd'] = df['wd'].replace([0,1,2,3,4,5,6],
    ['(一)','(二)','(三)','(四)','(五)','(六)','(日)']
)

# 時間格式化
df['rd03'] = df['rd03'].dt.strftime('%m/%d')

# 合併時間與星期
df['rd03'] = df['rd03'] + df['wd']

# 刪除星期欄位
del df['wd']

# 替換id為名稱
df['rd04'] = df['rd04'].replace([0,1,2,3,4,5,6],
    ['未設定','出勤日','公休日','週休日','國定假日','無薪公休','不計']
)
# print(df.head(3)) # 列出前n筆的表格

df_w = df.loc[df['ps02'] == 'AA0031'] # 篩選
print(df_w.head(5)) # 列出前n筆的表格
# print(df_w)

df_list = df_w.values.tolist()
print(df_list)