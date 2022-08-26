import array

def test1():
    lis = [0,1,2,3,4,3]
    print(lis)
    arr = array.array('l', lis) # 建立
    print(arr)

    print(len(arr)) # 長度
    print(arr[2])   # 取值
    print(arr[2:5]) # 取段
    print(arr.typecode) # 陣列類型
    print(arr.itemsize) # 類型長度 (bytes)

    arr.append(9) # 添加元素
    print(arr)

    arr2 = array.array('l', [7,8,9]) # 添加陣列
    arr.extend(arr2)
    print(arr)

    print(arr.count(3)) # 筆數 !!!
    print(arr.index(7)) # 回傳index 僅回傳首個

    arr.insert(0, 48) # 插入  依照索引位置插入  可以為負
    print(arr)

    arr.pop() #刪除最後一個
    print(arr)

    arr.remove(3) #依值刪除 僅刪除首個
    print(arr)

    arr.reverse() # 反轉
    print(arr) 

    lis_n = arr.tolist()
    print(lis_n) 
    '''
    Type code   C Type  Python Type 最小所需的位元組    註解
    'b' signed char int 1   
    'B' unsigned char   int 1   
    'u' Py_UNICODE  Unicode character   2   -1
    'h' signed short    int 2   
    'H' unsigned short  int 2   
    'i' signed int  int 2   
    'I' unsigned int    int 2   
    'l' signed long int 4   -2147483648至2147483647
    'L' unsigned long   int 4   
    'q' signed long long    int 8   
    'Q' unsigned long long  int 8   
    'f' float   float   4   
    'd' double  float   8   
    '''

# def test2():
#     arr = array.array('l')
#     arr.frombytes(u'abcde') # 建立
#     print(arr)


if __name__ == '__main__':
    test1()