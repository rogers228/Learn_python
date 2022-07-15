import configparser

def test1():
    cf = configparser.ConfigParser()
    cf.read('test1.ini')
    cf.set('http', 'port', str(90))
    with open('test1.ini', 'w') as f:
        cf.write(f)
    
    print('ok')
if __name__ == '__main__':
    test1()