'''
    帶參數的裝飾器 會有三層
    第一層用來傳遞參數

'''
def check_animal(animal):
    def decorator(func):
        def wrap():
            print(animal, 'are you animal?')
            print('yes sir i sitdown') #先做的事
            #...
            #...
            #...
            func() # 最後再執行原函數
        return wrap # 回傳(執行)內部func
    return decorator


@check_animal('allen')
def dog():
    print('wwwwww')

@check_animal('pdno')
def cat():
    print('muoooo')

def test1():
    cat()

if __name__ == '__main__':
    test1()
    print('ok')