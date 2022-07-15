import setproctitle

def test1():
    setproctitle.setproctitle('test1')
    print('test1')

if __name__ == '__main__':
    test1()