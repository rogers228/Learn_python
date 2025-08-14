import uuid


def test1():
    print('test1')
    # 生成版本4的UUID
    unique_id = uuid.uuid4()
    print(unique_id)
    print(type(unique_id))

if __name__ == '__main__':
    test1()