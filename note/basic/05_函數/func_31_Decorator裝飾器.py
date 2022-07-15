'''
    Decorator 
    裝飾器
    簡單來說就是執行func 之前 先做@ 裡面的事
    並且可以重複引用

    例如，
    過馬路前先停看聽
    進入特定網頁前先進行認證 flask
    ''' 

def sitdown(func):
    def wrap():
        print('yes sir i sitdown') #先做的事
        #...
        #...
        #...
        func() # 最後再執行原函數
    return wrap # 回傳(執行)內部func



@sitdown #我是裝飾器
def dog():
    print('wwwwww')

@sitdown
def cat():
    print('muoooo')

def test1():
    dog()

if __name__ == '__main__':
    test1()
    print('ok')