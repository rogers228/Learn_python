from pprint import pprint

def test1():
    data = {"key1": "value1", "key2": "value2", "key3": {'a': 67}}
    print(data)
    pprint(data)

def test2():
    from tabulate import tabulate
    data = [["Alice", 25], ["Bob", 30], ["Charlie", 28]]
    headers = ["Name", "Age"]
    print(tabulate(data, headers=headers))

if __name__ == '__main__':
    test2()