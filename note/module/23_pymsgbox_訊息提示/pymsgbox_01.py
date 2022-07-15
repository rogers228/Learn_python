import pymsgbox as m
#ok
#m.alert('This is an msgbox ok')
#m.alert(text='This is an msgbox ok',title='app', button='bk')
#m.alert('This is an msgbox ok','app', 'ok')
#m.alert('This is an msgbox ok','app', 'ok', timeout = 2000) #時間參數
m.native.alert('This is an msgbox ok','app', 'ok') #使用本地樣式

#yes or no
#m.confirm('This is an msgbox ok and cancel')
#m.confirm(text='This is an msgbox ok',title='app', buttons=['bk', 'Cancel'])
#m.confirm('This is an msgbox ok','app', ['bk', 'Cancel'])
#m.confirm('This is an msgbox ok','app', ['bk', 'Cancel'], timeout = 2000)
#m.native.confirm(text='This is an msgbox ok',title='app', buttons=['bk', 'Cancel']) #使用本地樣式

#inputbox
#m.prompt('This is an inputbox for user')
#m.prompt(text='This is an inputbox for user',title='app', default='bk')
#m.prompt('This is an inputbox for user','app', 'bk')
#m.prompt('This is an inputbox for user','app', 'bk', timeout = 2000)

#inputbox with password
#m.password('This is an inputbox for user')
#.password(text='This is an inputbox for user',title='app', default='D', mask = '*')
#m.password('This is an inputbox for user','app', '')
#m.password('This is an inputbox for user','app', '')



