print('--列表練習--')
mylist = [1,2,3,4,5,6] #建立列表
print(mylist) #印出列表
print()
print('--引用列表中的項目--')
print(mylist[2]) #印出第3個項目，預設從0開始
print(mylist[0]) #印出第1個項目，預設從0開始
print(mylist[2:5]) #印出從第3開始到第6為止 須注意!!!(不包含第6)
print(mylist[2:]) #印出從第3開始到最後
print(mylist[:5]) #印出從最前到第6 須注意!!!(不包含第6)
print(mylist[:]) #印出從最前到最後
print()
print('--項目賦值---')
mylist[2] = 100 #設定第3個的值
#mylist[3] = 'rogers' #設定第4個的值為字串，竟然可以不同類型，超強!
print(mylist) #印出列表
mylist[0:2] = [51, 52, 53] #可直接修改列表區段，將第1-2個項目修改為新值，竟然可以修改區段，超強!!!
print(mylist) #印出列表
print()
print('--使用for迴圈，找出列表最大值---')
m=0
for e in mylist:
    if m < e:
        m=e
print(m)
print()
print('--使用for迴圈及索引，找出列表最大值---')
m=0
for i in range(len(mylist)):
    if m < mylist[i]:
        m=mylist[i]
print(m)
print()
print('--使用for建立10個元素的一維陣列--')
#mylist=[]
#for i in range(10):
#    mylist[i] = 1
#出現錯誤，因為不能賦值給不存在的列表
#應使用append方法添加
mylist=[]
for i in range(10):
    mylist.append(i)
print(mylist) #印出列表
print()
print('--使用精簡for建立10個元素的一維陣列--')
print('mylist = [ i for i in range(10)]')
mylist = [ i for i in range(10)]
#mylist[5] = 'rogers' # 可以賦值，不同類型也可
#mylist[9]=99 #可以賦值
#mylist[10]=99 #超出陣列不可以賦值
print(mylist) #印出列表



