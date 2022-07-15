def ger_rdk(mystr):
    #將換行字串變數轉換為單行，以逗點分隔
    #(不含註解)
    tmp = ''
    aList =mystr.split('\n')
    for i in range(len(aList)):
        sLine = aList[i]
        if len(sLine) > 0:
            sLine = sLine.strip() #去除頭尾空白
            sLine = sLine.rstrip(',') #去除逗號
            if sLine[0:1] == "\'":
                pass #註解不計
            else:
                tmp += sLine + ','
    tmp = tmp.rstrip(',') #去除逗號
    return tmp
                
if __name__ == '__main__':
    with open('test55.txt', 'r') as file:
        data = file.read()
        print(data)

    print()
    print(ger_rdk(data))
