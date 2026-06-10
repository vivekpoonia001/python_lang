#question 1
#  import random 
# import string
# def genrate_password():
#     char = string.ascii_letters+string.digits
#     password = " ".join(random.choice(char) for i in range(8) )
#     return password
# print("generated password ", genrate_password())

#question 2
# def calculate_bmi(weight_kg,height_m):
#     bmi = weight_kg/height_m**2
#     print(bmi)
# calculate_bmi(80,1.90)

#question 3
# def book_flight(destination, class_type = "economy"):
#     return f"tickit is booked for {destination}in {class_type} is confirm"
# destination = input("enter destination")
# class_type = input("enter class type")
# if class_type =="":
#     print(book_flight(destination))
# else:
#     print(book_flight(destination, class_type))

# def create_profile(username, age, country = "unknown"):
#     return {"username":username, "age":age , "country":country}
# ab = create_profile(country = "India", age =30, username = "VIvek")
# print(ab)

# def concatenate_words(*words):
#     man = "a".join(words)
#     print(man)
# concatenate_words("vivk","ergb","ergt","rtg")


def build_configuration(**setings):
  for key,value in setings.items():
     print(f"{key}: {value}",end=", ")
build_configuration(theme='dark', debug=True, max_users=100)
     
     
       