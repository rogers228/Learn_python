import time
a = 65
b = 'what'
c = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
print(str(a))

'''
高級文字變數
可取代原有的%s %d 用法
用法:'{}'.format()'''

#基本傳遞變數到字串
print('-----基本傳遞變數到字串-----')
print('{}'.format('hi!')) #傳遞值到字串     
print('{}'.format(a)) #傳遞變數到字串
print('現在時間:{}~999'.format(c)) #傳遞變數到字串
print('{}......{}'.format(a,b)) #傳遞2個變數，依順序
print('{1}......{0}'.format(a,b)) #傳遞2個變數，指定順序
print('{1}......{0}..{1}'.format(a,b)) #傳遞2個變數，到3個位置，指定順序

#指定參數名稱
print('{Lng1}......{Str1}'.format(Lng1 = a, Str1 = b))

#使用列表
print('-----list-----')
print('{0[0]}...{0[1]}...{0[2]}'.format(['aaa', 'bbb', 'ccc']))
lis = ['where', 99, 3.141592654]
print('{0[0]}...{0[1]}...{0[2]}'.format(lis))

#數字格式化
#{}裡面可以輸入格式化符號
pi = 0.2566816
print('{:.2%}'.format(pi))


#寫些情況無法使用大誇號{} 也可以使用取代
a = 'abcdefg'
print(a)
a = a.replace('cd', 'xx')
print(a)
