df_w = df.loc[(df['製造類別'] == 'S')|(df['製造類別'] == 's')] # 篩選
# | 直線符號代表 or
# &  代表 and
# () 括號一定要


#使用 IN
df = pd.DataFrame({'A': ['h','s','S','S','s','z','Z','r'], 'B': [1,2,3,5,6,8,15,20]})
print(df)

print('')

df2 = df[df['A'].isin(['s','S'])]
print(df2)