class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = person("ram", "kumar")
x.printname()

class student(person):
    pass
x=student("shyam","pandey")
x.printname()



########################################################################################
class Person:
    def money(self):
        print("parent money")

    def house(self):
        print("parent house")

# p=Person()
# p=.money()
# p=.house()

class Child(Person):
    pass
c= Child()
c.money()
c.house()











