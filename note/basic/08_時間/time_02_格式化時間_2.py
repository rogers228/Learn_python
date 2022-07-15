import datetime
userinput = "2013/3/6"
try:
    cdate = datetime.datetime.strptime(userinput, '%Y/%m/%d')
    print(cdate)
except:
    print('err')
