import configparser

def test1():
    host = 'https://www.google.com'
    port = 80

    cf = configparser.ConfigParser()
    cf['http'] = {}
    cf['http']['host'] = host
    cf['http']['port'] = str(port)

    with open('test1.ini', 'w') as f:
        cf.write(f)

def test2():
    cf = configparser.ConfigParser()
    cf['venv'] = {}
    cf['venv']['version'] = '20220816'

    with open('python_green.ini', 'w') as f:
        cf.write(f)

if __name__ == '__main__':
    test2()