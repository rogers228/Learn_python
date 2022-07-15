class Person: #類別
    def __init__(self, a): #對象，直接自動執行的程序，固定為__init__
                           #對象中的參數第一個必為self，代表類別本身
        self.name = a #對象中的變數，在Python不需要宣告變數
        self.k = 25
    def sayhi(self): #對象
        print('Hello, how are you?', self.name , '\nHow old ary you?', self.k)
p=Person('Rogers')
p.sayhi()

