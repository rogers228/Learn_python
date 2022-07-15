#是否吻合字串 不區分大小寫

#使用or列出全部
mystr = 'd'
if mystr == 'a' or mystr == 'A':
	print('yes')
else:
	print('no')

print('-----')

#進階  轉換後再比較

mystr = 'S'
if mystr.lower() in ['y', 's']:
	print('yes')
else:
	print('no')