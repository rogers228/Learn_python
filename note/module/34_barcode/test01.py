import code128


def test1():
    #建立條碼圖片
    code128.image("Hello World").save("Hello World.png")  # with PIL present

if __name__ == '__main__':
    test1()
    print('ok')