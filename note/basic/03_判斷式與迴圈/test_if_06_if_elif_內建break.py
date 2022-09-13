def test10():
    a=500
    if a>1:
        print('a>1')

        # 吻合時 內建break 
    elif a>2:
        print('a>2')
    elif a>3:
        print('a>3')
    else:
        print('else')
    # 以上吻合不再執行
    # 等同內建break

if __name__ == '__main__':
    test10()