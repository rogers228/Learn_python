def ger_tn(mystr):
    aList =mystr.strip().split('\n')
    return len(aList)

       
if __name__ == '__main__':
    with open('test55.txt', 'r') as file:
        data = file.read()
        print(data)
    print()
    print(ger_tn(data))
