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



     ps02            rd03  rd04            rd11 rd12  rd13
0  AA0003  20201118000000     1            0730  未結算     2
1  AA0003  20201117000000     1  0733,1254,1733          1
2  AA0003  20201116000000     1  0747,1245,1733          1

       ps02      rd03 rd04            rd11     rd12  rd13
392  AA0031  11/18(三)  出勤日            0738      未結算     2
393  AA0031  11/17(二)  出勤日  0735,1257,1830    溢勤1小時     2
394  AA0031  11/16(一)  出勤日       0732,1744              1
395  AA0031  11/15(日)  公休日                              1
396  AA0031  11/14(六)  週休日       0827,1300  溢勤4.5小時     2
[Finished in 0.5s]