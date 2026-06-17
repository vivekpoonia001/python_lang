# l_f = ["apple\n", "watermelon\n", "pineapple\n"]
# with open("fruits.txt", "w") as file:
#     file.writelines(l_f)
# print("the fruits are ", l_f)

#question 2
# try:
#     with open("vegetables.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("file not found")


#question 3

# with open ("fruits.txt", "a+") as file:
#    file.writelines(["Grapes\n","Dragon fruit\n"])
#    file.seek(0)
#    content = file.read()
#    print(content)

# #question 4
# with open ("fruits.txt", "r")as file:
#    for i in file:
#       print(i.strip())


#question 5
# try :
#    num_1 = 10
#    num_2 = int(input("enter number "))
#    result = num_1/num_2
# except ValueError:
#    print("user entered a non number")
# except ZeroDivisionError:
#    print("10 cant be divide by zero")
# else:
#    print(result)
# finally:
#    print("divsion attempt finished")


#question 6
# my_colors = ["red", "blue", "green"]
# student_info = {"name": "John", "grade": "A"}
# try:
#    print(my_colors[5])
# except Exception as e :
#     print("index error",e)

# try:
#    print(student_info["age"])
# except Exception as e :
#    print("enter a valid key",e)
   