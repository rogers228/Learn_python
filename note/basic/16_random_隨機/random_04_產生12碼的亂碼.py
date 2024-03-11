import random
import string

def ger_random_str():
    # 產生12碼的亂碼
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))

def test_1():
    print(ger_random_str())
    print('ok')



# 產生n碼隨機文字  不依賴string
def get_random_str(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))


if __name__ == '__main__':
    test_1()


