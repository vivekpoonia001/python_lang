'''OOPS : OOPs (Object-Oriented Programming System) is a programming approach that uses classes and objects to organize code. Its main principles are Encapsulation, Inheritance, Polymorphism, and Abstraction, which improve code reusability, maintainability, and scalability.'''

'''
1. Class : A class is a blueprint or template used to create objects. It defines the attributes (data) and methods (functions) that objects will have.
# syntax : class Student:
                pass
                

2. Object : An object is an instance of a class. It represents a real entity created from the class blueprint.
# syntax : s1 = Student()


3. Attribute : An attribute is a variable that belongs to a class or object and stores data.
# syntax : self.name = "Dikshit"


4. Method : A method is a function defined inside a class that describes the behavior of objects.
# syntax : def display(self):
                print(self.name)

                
5. Constructor (__init__) : A constructor is a special method that is automatically called when an object is created. It is used to initialize object data.
# syntax : def __init__(self, name):
                self.name = name


6. self : self is a reference to the current object. It is used to access the object's attributes and methods.
# syntax : self.name


7. Instance Variable : An instance variable belongs to a specific object. Each object can have different values.
# syntax : self.name = name


8. Class Variable : A class variable belongs to the class itself and is shared by all objects.
# syntax : class Student:
                school = "ABC School"

'''

# class student:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#     def k(self):
#         return f"name of student is {self.name}, age of student is {self.age}"

# s1 = student("Vivek", 20)
# s2 = student("Ashish", 21)
# print(s1.k())
# print(s2.k())

class employee:
    company_name = "tech solutoins"
    employee_count = 0
    def __init__(self,name , salary):
        self.name = name
        self.salary = salary
        employee.employee_count+=1

e1 = employee("Vivek", 2000000)
e2 = employee("ashish",1500000)
print(f"Company:{employee.company_name}")
print(f"e1 worsk at :{e1.company_name}")
print(f"total employee:{employee.employee_count}")


