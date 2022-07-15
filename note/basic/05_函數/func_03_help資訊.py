def say(message, times = 1):
    '''標題

    文字第一行
    文字第二行'''
    print(message * times)
say('hello')
say('hello',5)
print(say.__doc__)
help(say)
