from datetime import datetime
from datetime import timedelta

year_s, month_s, day_s = '2018','7','31'
mydate = datetime(int(year_s), int(month_s), int(day_s))
print(mydate)
endDate = mydate + timedelta(days = 1) # 加1天
print(endDate)



from dateutil.relativedelta import relativedelta
date_end_datetime = date_start_datetime + relativedelta(years=10) # 加10年