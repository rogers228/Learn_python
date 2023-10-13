import sys
print('測試')

#方法1
if True:
    sys.exit() #正式結束程式  需要導入sys


#方法2
if True:
    raise SystemExit  #正式結束程式 而不需要導入sys

print('若離開就看不到了')


# 由子線程 結束全部
os._exit(0) #結束自己 連同主線程結束