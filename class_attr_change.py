class Person:
    name = 'anonymous'

    def changeName1(self,name):
        self.name = name

    def changeName2(self,name):
        Person.name = name

    @classmethod
    def changeName3(cls,name):
        cls.name = name



p1= Person()
p1.changeName1('Surbhi')
print(p1.name)
print(Person.name)
print('')

p1.changeName2('Surbhi')
print(p1.name)
print(Person.name)
print('')

p1.changeName3('Surbhi')
print(p1.name)
print(Person.name)