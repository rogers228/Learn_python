import array

def test1():
    arr = array.array('i') # initialising array a
    # 添加索引 index
    arr.append(45) 
    arr.append(154)
    arr.append(35)
    arr.append(45) 
    print(arr)

    #  if index in arr
    if 45 in arr:
        print('yes in')
    else:
        print('no')

if __name__ == '__main__':
    test1()