'''僅引用test_function_say模組裡的say程序
往後的程式碼不可再冠上模組名'''
from test_function_say import say
say('hello',3)
#test_function_say.say('hello',3) #錯誤，不可在冠上模組名稱
#say2('hello') #錯誤，未引用say2程序，無法使用
print(__doc__)

