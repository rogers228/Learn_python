def test10():
    import ast
    test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
    res = ast.literal_eval(test_string)
    print(res)

if __name__ == '__main__':
    test10()
    print('ok'