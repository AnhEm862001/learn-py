#python oop

"""
A class empty 
"""
class Employee:

    pass #Skip that class no attributes or methods, when run this code without error

"""
"""
class New_Employee:
    #A class attribute initial
    on_position = "intern" 

    #Init set the initial state of the object use __init__
    def __init__ (self, name, age, career):
        self.name = name
        self.age = age
        self.career = career
    
    #Display the information of employee use __str__
    def __str__(self):
        return f"{self.name} hien nay {self.age} tuoi dang lam {self.career} o vi tri"

Linh = New_Employee("Linh", 22, "luat su")

##Inheritance
class Old_Employee(New_Employee):
    def __init__(self, name, age, career):
        super().__init__(name, age, career)
        self.on_position = "fresher"
Huy = Old_Employee("Huy", 23, "lap trinh vien")

#Check class child and class father
print(isinstance(New_Employee,Old_Employee))