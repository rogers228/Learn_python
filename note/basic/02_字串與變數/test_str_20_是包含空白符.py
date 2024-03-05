def has_whitespace(s):
    return any(c.isspace() for c in s)

def test1():
    mystr = 'fsadsfsadf '
    print(has_whitespace(mystr))

if __name__ == '__main__':
    test1()