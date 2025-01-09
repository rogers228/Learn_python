today = datetime.datetime.now()
alarmday = r['提醒日期'].to_pydatetime() # pandas時間 轉 python datetime
result = (today-alarmday).days # 相差天數