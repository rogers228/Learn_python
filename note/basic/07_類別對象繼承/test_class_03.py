class Person: #類別
    population = 0

    def __init__(self, name):
        self.name= name
        print('(Initalizing %s)' % self.name)
        Person.population += 1

    def __del__(self):
        print('%s says bye.' % self.name)
        Person.population -= 1

        if Person.population == 0:
            print('I am the last one.')
        else:
            print('There are still %d people left.' % Person.population )

    def sayhi(self):
            print('Hi, my name is %s.' % self.name)

    def howMany(self):
        if Person.population == 1:
            print('I an the only person here.')
        else:
            print('We have %d person here.' % Person.population)

    
sw=Person('Swaroop')
sw.sayhi()
sw.howMany()

ka=Person('Kalam')
ka.sayhi()
ka.howMany()

sw.sayhi()
sw.howMany()


