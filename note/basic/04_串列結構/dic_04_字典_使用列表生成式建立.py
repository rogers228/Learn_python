def test1():
    dic = {'rd02': 32, 'rd03': '20220722000000', 'rd04': 1, 'rd06': 1.0, 'rd10': '', 'rd11': '0741,1303,1755', 'rd12': '', 'rd14': 1}
    print(dic)

    dic2 = {k:v for k, v in dic.items()}
    print(dic2)

if __name__ == '__main__':
    test1()