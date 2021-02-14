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
    #When you define __init__ for child class python overrides original __init__ 
    def __init__(self,student_name,student_lname,age,school):
        super().__init__(student_name,student_lname)
        self.age = age
        self.school = school
    def __str__(self):
        return "Name: {} Lastname: {} \nAge: {} School: {}".format(self.firstname,self.lastname,self.age,self.school)
        
        
        



y = Student("Okan","Yalcin",24,"Hitite University")
print(y)