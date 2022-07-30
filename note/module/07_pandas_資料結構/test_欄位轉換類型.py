total_rows['ColumnID'] = total_rows['ColumnID'].astype(str) # 數字轉文字


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