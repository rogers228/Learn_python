import random
import string

def ger_random_str():
    # 產生12碼的亂碼
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))

def test_1():
    print(ger_random_str())
    print('ok')

if __name__ == '__main__':
    test_1()