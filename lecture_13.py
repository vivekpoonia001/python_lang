'''today we are learning some more topics of oops 
that includes 
inheritance 
encapsulation
polymorphism 
now lets talk about inheritance -Inheritance allows one class (child class) to use the properties and methods of another class (parent class).

What is Polymorphism?
Poly = Many
Morph = Forms
Polymorphism means:
The same method name can behave differently for different objects.

Encapsulation means:
Wrapping data (variables) and methods (functions) into a single unit (class) and controlling access to the data.
'''
# inheritance 
# class dog():
#     def __init__(self,name):
#         self.name = name
# class animal(dog):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

# pet = animal("boxer","german")
# print(pet.name, pet.breed)

# polymorphism
# class animal():
#     def speak(self):
#         return "any sound"
# class lion(animal):
#     def speak(self):
#         return "roar"
    
# class dog(animal):
#     def speak(self):
#         return "bark"
# mimic = animal()
# mic = lion()
# mim = dog()
# print(f"any animal can make :{mimic.speak()}")
# print(f"lion make :{mic.speak()}")
# print(f"dog make :{mim.speak()}")


#encapsulation
class bankaccount():
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    def withdrwal(self, amount):
        if 0<amount<=self.__balance:
            self.__balance -= amount
    def get_balance(self):
      return self.__balance


acc = bankaccount(1000)
acc.deposit(500)
acc.withdrwal(300)
print(acc.get_balance())


