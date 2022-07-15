class SchoolMember: #建立SchoolMember類別
    def __init__(self, name, age): #建立3個參數
        self.name = name
        self.age = age
        print('Initialized SchoolMember: %s' % self.name )

    def tell(self):
        print('Name: %s, Age: %s' %(self.name, self.age))

class Teacher(SchoolMember): #Teacher繼承SchoolMenber
    def __init__(self, name, age, salary): #Teacher含有4個參數
        SchoolMember.__init__(self, name, age) #其中3個參數為SchoolMember類別當中的self, name, age屬性
        self.salary = salary #其中1個參數是Teacher獨有
        print('Initialized Teacher: %s' % self.name )

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: %d' % self.salary )

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        Student.marks = marks
        print('Initialized Student: %s' % self.name )

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: %d' % self.marks )
'''        
ro = SchoolMember('Rogers', 5)
ro.tell()

t = Teacher('Mrs Shrividya', 5, 300)
t.tell()

s= Student('Tony', 2, 35)
s.tell()
'''

t = Teacher('Mrs Shrividya', 5, 300)
s= Student('Tony', 2, 35)
numbers = [t,s]
for mumber in numbers:
    mumber.tell()
