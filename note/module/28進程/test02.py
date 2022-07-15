import os

def test1():
    # 進程       父進程
    # pid=13612, ppid=17356
    print('pid={0}, ppid={1}'.format(os.getpid(), os.getppid()))

if __name__ == '__main__':
    test1()