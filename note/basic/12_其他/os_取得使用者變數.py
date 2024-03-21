import os

def test1():
    user_variable = os.environ.get('TEST')
    print(user_variable)

if __name__ == '__main__':
    test1()