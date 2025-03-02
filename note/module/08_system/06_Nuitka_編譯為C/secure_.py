config = {
    'name': 'allen',
    'key': 'test'
}

def secret_function(x, y):
    return x * y + 10
    
def test1():
    print(config)

if __name__ == '__main__':
    test1()
