from datetime import datetime

def getWeekdayStr(year_s, month_s, day_s):
    try:
        mydate = datetime(int(year_s), int(month_s), int(day_s))
        index = mydate.weekday()
        wStr = ('一','二','三','四','五','六','日')
        return wStr[index]
    except:
        return ''

ddd = getWeekdayStr('2018','7','31')
print(ddd)
