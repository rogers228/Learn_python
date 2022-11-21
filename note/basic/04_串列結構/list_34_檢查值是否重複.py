def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    #   所有元素的數量             轉換為集合(自動剔除重複值)元素的數量
    if len(listOfElems) == len(set(listOfElems)):
        # 數量相同 代表沒有重複
        return False
    else:
        # 反之 代表有重複
        return True