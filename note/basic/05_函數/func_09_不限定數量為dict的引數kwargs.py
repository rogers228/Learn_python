def test_kw(**kwargs):
    # **kwargs key value word 不限定數量引數ˋ
    # 使用者不需事先定義字典，輸入的引數即轉為字典型態，明確好用
    print(kwargs)
    for key in kwargs:
        print(f'{key}:{kwargs[key]}')

def test42():
    test_kw(a=1, b=2,c='456')

if __name__ == '__main__':
    test42()