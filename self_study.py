# num = int(input("enter a number"))
# if(num%2==0):
#     print("the number is even")
# else: 
#     print("the number is odd")

# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# num3 = int(input("enter third number:"))
# if num1>num2 and num1>num3:
#     print("the greatest number is ", num1)
# elif(num2>num1 and num2>num3):
#     print("greatest numbre is ", num2)
# else:
#     print("the greates number is ", num3)

# num = int(input("enter a year "))
# if(num%4==0 and num%100!=0) or (num%400==0):
#     print("the year is leap year")
# else:
#     print("year is nbot a leap year")
# print("vivek \n"*5)
# num = int(input("enter a number"))
# sum = 0;
# for i in range(1,num+1):
#     sum+=i
# print("the sum of numbers is ", sum)
# print("the amount of balance",)
# amount = int(input("enter the wothdrwal amount"))
# if amount >500:
#     withdrwal = int(input("enter withdrwal money"))
#     if withdrwal <=amount:
#         print("withdrwal succsefull")
#     else:
#         print("insufficient balance ")
# else:
    # print("minimum balanace not found")

percentage = int(input("enter your percentage "))
if percentage >75:
    f_income = int(input("enter your family_income"))
    if f_income <300000:
        print("scholar ship granted")
    else:
        print("scholarship denied")
else:
    print("not eligble")

username = int(input("enter your username"))
if username == "yes":
    password = int(input("enter your password"))
    if password == "correct":
        print("login succsefull")
    else:
        print("incoreect passowrd")
else:
    print("else user not found")