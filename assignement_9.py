
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