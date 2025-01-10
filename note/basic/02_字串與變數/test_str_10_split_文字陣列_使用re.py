import re
def test1():
    # 使用 re.split  更靈活
    str_arr = "a,b,c , d, e,f ,g , h , i ,j, k"
    lis = re.split(r'\s*,\s*', str_arr)
    print(lis)

if __name__ == '__main__':
    test1()