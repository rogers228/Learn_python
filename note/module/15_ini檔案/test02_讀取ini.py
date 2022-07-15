import configparser

def test1():
    cf = configparser.ConfigParser()
    cf.read('test1.ini')
    host = cf['http']['host']
    port = cf['http']['port']

    print(host, port)
        
if __name__ == '__main__':
    test1()