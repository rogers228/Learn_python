#This is a list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist) , 'items.')
print('There items are:')
for item in shoplist:
    print(item,)
print('\nI also have rice.') #'\n 換行
shoplist.append('rice') #添加項目rice
print('My list is now',shoplist)
print('\nI will sort my list.')
shoplist.sort() #列表內容重新排序
print('Sorted list is',shoplist)
print('\nThe 1 item is',shoplist[0])
print('The 2 item is',shoplist[1])
oleitem = shoplist[0]
del shoplist[0] #刪除第一個列表內容
print('\nI bought the',oleitem)
print('now list is',shoplist)
