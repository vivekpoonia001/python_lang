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

# percentage = int(input("enter your percentage "))
# if percentage >75:
#     f_income = int(input("enter your family_income"))
#     if f_income <300000:
#         print("scholar ship granted")
#     else:
#         print("scholarship denied")
# else:
#     print("not eligble")

# username = int(input("enter your username"))
# if username == "yes":
#     password = int(input("enter your password"))
#     if password == "correct":
#         print("login succsefull")
#     else:
#         print("incoreect passowrd")
# else:
#     print("else user not found")
# print("new repositry is made")
# l1 = ["Ashish", "Jogender","Nishant", "Harkarn","Manjot"]
# num_1 = input("enter a friend name: ")
# l1.insert(2,num_1)
# mst_friend = input("enter your most important friend: ")
# pos = int(input("enter postion of that friend: "))
# l1.insert(pos,mst_friend)
# print(l1)
# l1 = [1,10,100,3,6,8]
# l1.insert(3,59)
# print(l1)
# l1.append(5)
# print(l1)
# print(len(l1))
# l1 = ["Ankit","jog","NIs","Vivek","Jaat","San"]
# for i in l1:
#     if len(i)<4:
#         print(i)
#another method 

# num_1 = []
# l1 = ["Ankit","jog","NIs","Vivek","Jaat","San"]
# for i in l1:
#     if len(i)<4:
#         num_1.append(i)
# print(num_1)

# num_1 = range(20)
# result=[]
# for i in num_1:
#     if i %2==0:
#         result.append("even")
#     else:
#         result.append("odd")
# print(result)
# sum of list 
# l1 = [1,2,4,667,7,866,788,56]
# sum =0
# for i in l1: 
#     sum+=i
# print(sum)

# l = [1,24,55,67,786,45,6,7,888,865]
# count = 0 
# for i in l:
#     if i %2==0:
#         count+=1
#     elif i %2!=0:
#         count+=1
        
# print(count)
l1 = [1,34,56,7,887654,3578,8654,45678,8765,43]
largest = l1[0]
for i in l1:
    if i >largest:
        largest = i
print(largest)

    