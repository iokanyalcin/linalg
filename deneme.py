class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        self.age = 24
    def show_name(self):
        return '{} {}'.format(self.firstname,self.lastname)

    def __str__(self):
        return '{} {}'.format(self.firstname,self.lastname) 
    
class Student(Person):
    pass
x = Person("okan","yalcin")
print(x.show_name())
print(x)
print(x.age)
y = Student("okan1","yalcin1")
print(y.firstname)
print(y.lastname)
print(y.show_name())
print(y)
