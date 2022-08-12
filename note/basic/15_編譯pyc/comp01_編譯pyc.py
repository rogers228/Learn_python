import compileall

def test1():
    #編譯該路徑的所有py
    mydir = r'C:\Users\user\Documents\GitHub\Learn_python\note\basic\15_編譯pyc\pyc_test01'
    print(mydir)
    compileall.compile_dir(mydir)

if __name__ == '__main__':
    test1()
    print('ok')