class bom:
    def __init__(self, pd):
        self.pd = pd
        self.pd2 =''
        self.pp()
        
    def bomList(self):
        self.pd2='123'
        return ['aa','bb', self.pd]

    def bomCost(self):
        return [1, 2, self.pd, self.pd2]

    def pp(self):
        print('ppp')
