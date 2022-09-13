total_rows['ColumnID'] = total_rows['ColumnID'].astype(str) # 數字轉文字
df['DataFrame Column'] = df['DataFrame Column'].astype(float) # 文字轉數字

# 文字轉時間
df['收件日'] =  pd.to_datetime(df['收件日'], format='%Y-%m-%d %H:%M:%S')


# pandas 時間 轉換為 python datetime
alarm_pd_date = r['提醒日期']
print(alarm_pd_date)
print(type(alarm_pd_date))

alarm_py_date = alarm_pd_date.to_pydatetime()
print('# 轉換為 python datetime.date')
print(alarm_py_date)
print(type(alarm_py_date))


#  type object to numeric
df_new['SS001'] = pd.to_numeric(df_new['SS001'], errors='coerce')
df_new['SS002'] = pd.to_numeric(df_new['SS002'], errors='coerce')
df_new[['SS001', 'SS002']] = df_new[['SS001','SS002']].fillna(value=0) # 空白補0