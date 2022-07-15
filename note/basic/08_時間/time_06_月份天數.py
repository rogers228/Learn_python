from datetime import datetime
from datetime import timedelta

def getYMdays(year_s, month_s):
    try:
        mydate = datetime(int(year_s), int(month_s), 1)
        old_Month = mydate.month
        new_Month = mydate.month
        i = 0
        while new_Month == old_Month:
            mydate = mydate + timedelta(days = 1)
            new_Month = mydate.month
            i = i + 1
            if i > 31:
                return 31
        return i
    except:
        return 31
    
dd = getYMdays('2021','02')
print(str(dd))
        

