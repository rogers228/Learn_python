import time
s='bom_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.xlsx'
print(s)
'''
格式化符號
%y 2位數,西元年
%Y 4位數,西元年
%m 2位數,月
%d 2位數,日
%H 24小時制 時
%I 12小時制 時
%M 分鐘
%S 秒
'''

today = time.strftime("%Y%m%d", time.localtime())
print(today)
