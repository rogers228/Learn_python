import sys

if __name__ == '__main__':

    print(sys.argv)
    print(type(sys.argv)) # lsit
    print(len(sys.argv))
    if len(sys.argv) < 3:
        print('no argument')
        sys.exit()
    print('hello')

    for e in sys.argv:
        print(e)

    # cmd執行
    # U:\dsprog\py_excel\test\18_argv\test_argv_01.py a b