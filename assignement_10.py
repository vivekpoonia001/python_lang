# class dog:
#  def __init__(self, name, age):
#   self.name = name
#   self.age = age
#  def bark(self):
#   print(f"Woof!my name is {self.name}")

# n1 = dog("Ashish",20)
# (n1.bark())


# Question 2
# class school:
#   school_name = "Python Academy"
#   def __init__(self, student_name):
#    self.student_name = student_name

# s1 = school("Vivek")
# s2 = school("Ashish")
# print(f"school name is {school.school_name}")
# print(f"student name is {s1.student_name}")
# print(f"student name is {s2.student_name}")

#question 3
# class BankAccount:
#   def __init__(self, owner,balance=0):
#     self.owner = owner
#     self.balance = balance
#   def deposit(self,amount):
#      self.balance+= amount
#   def withdrwal(self,amount):
#      self.balance -= amount


# account = BankAccount("Vivek")
# account.deposit(100)
# account.withdrwal(30)
# print("final Balance",account.balance)

#question 4
# class Product:
#   def __init__(self, name, price):
#     self.name = name
#     self.price = price

# class shopping_cart:
#   def __init__(self):
#     self.items = []
#   def add_item(self, product):
#     self.items.append(product)


# p1_product = Product("apple",200)
# p2_product = Product("kiwi",900)

# cart = shopping_cart()
# cart.add_item(p1_product)
# cart.add_item(p2_product)
# for item in cart.items:
#   print(item.name,item.price)

#question 5
class rectangle :
  def __init__(self, height, width):
    self.height = height
    self.width = width
  def calculate_area(self):
    return self.height* self.width
  def calculate_paremeter(self):
    return (2*(self.width+self.height))

w1 = rectangle(5,10)
print(w1.calculate_area())
print(w1.calculate_paremeter())