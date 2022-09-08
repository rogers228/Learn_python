單欄位不分大小寫
df = df[df['製造類別'].isin(['s','S'])] # 篩選
df = df[~df['製造類別'].isin(['h','H'])] # 篩選非停用  ~ 代表not !

單欄位
df_w = df.loc[df['ps02'] == 'AA0031'] # 篩選

單欄位 like
df_w = df[df['ps02'].str.contains('AA0031')
df_w = df[df['件號'].str.contains(s_gno) == True]

單欄位 like '2%'
df_w = df[df['pdno'].str.contains(r'^2.*')] # 材料件 品號2開頭

多條件
df_w = df.loc[(df['製造類別'] == 'S')|(df['製造類別'] == 's')] # 篩選
# | 直線符號代表 or
# &  代表 and
# () 括號一定要

# ~ 代表not !
df[~df.country.isin(countries_to_keep)]

#以index篩選
lis_match_index = [1,2,5,8]
df_w = df_w.take(lis_match_index)


#篩選單筆
df.iloc[[0]]************
df_w.iloc[0]['表格名稱英文']
df_w.iloc[[0]]['wh02']

#非空白  未驗證
df_w = df[df['工程屬性'].notna()] # 工程屬性不為空白者


# index 取欄位值
drawno = df.loc[df.index == gid]['圖號'].item()

or
sf['圖號'].values[0]

or
df.loc[gid, '圖號']

