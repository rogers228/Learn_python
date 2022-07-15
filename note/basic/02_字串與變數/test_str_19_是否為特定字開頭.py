def isinfirst(word, findstr):
    #是否為特定字開頭
    result = word.find(findstr)
    return True if result == 0 else False
    
def test12():
    word = 'geeks for yeoshe'
    print(isinfirst(word, 'shi'))