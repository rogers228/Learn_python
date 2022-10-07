# 記憶體(內存)String
from io import StringIO

def test1():
    s = StringIO() # 建立 StringIO 物件
    print(s)
    print(type(s))

def test2():
    # 建立簡單文字
    s = StringIO() # 建立 StringIO 物件
    s.write('4dsaf1asd65f1asd56') # 在內存建立文字
    s.seek(0) # 游標回到0的位置
    ans = s.read()
    print(ans)
    s.close() # 關閉  清空內存

def test3():
    # 建立多行文字
    s = StringIO() # 建立 StringIO 物件
    myString = """
        116516FD4A5S41F
        FDSAFASFD
        SADFASDDDDFD
    """
    s.write(myString) # 在內存建立文字
    ans = s.getvalue() # 使用 getvalue 方法
    # ans = s.read()
    print(ans)
    s.close() # 關閉

def test4():
    # 建立簡單文字
    s = StringIO() # 建立 StringIO 物件
    myString = """
        116516FD4A5S41F
        FDSAFASFD
        SADFASDDDDFD
    """
    s.write(myString) # 在內存建立文字
    s.seek(0)
    ans = s.readlines()
    print(ans)
    s.close() # 關閉

if __name__ == '__main__':
    test4()