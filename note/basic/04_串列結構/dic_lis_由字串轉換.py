def test17():
    import ast
    s = "{'ItemClass':'pd', 'A01':'V'}"
    dic = ast.literal_eval(s)
    print(dic)
    print(type(dic))

    s = "['a','b','c']"
    lis = ast.literal_eval(s)
    print(lis)
    print(type(lis))