# first question

# num_1 = int(input("enter a number upto you want to sum :"))
# sum = 0;
# for i in range(1, num_1+1):
#     sum += i
# print("sum of first natural numbers is ", sum)

# second question
# num_1 = int(input("enter a number "))
# num_2 = int(input("enter a number upto you want to print"))
# for i in range(1,num_2+1):
#     print(num_1, "*",i, "=",num_1*i)

#third question
# num_1 = int(input("enter a number"))
# if num_1<=1:
#     print("not a prime nor even")
# else:
#     for i in range(2,num_1):
#      if num_1 % i == 0:
#       print("the number is  not prime ")
#       break
#     else:
#           print("the number is prime")
#fourth question
# a = int(input("enter a number"))
# original = a
# reverse = 0
# while a>0:
#     digit = a % 10
#     reverse = reverse * 10 + digit
#     a=a // 10
# if reverse == original:
#     print("the number is palindrome")
# else:
#     print("not Palindrome")


#fifth question
# for i in range(1,101):
#     if i %3==0 and i%5==0:
#         print("Frizz Buzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)

# name = input("enter your name ")
# age = int(input("enter your age "))
# print("1.first class -1500")
# print("2.second class-1000")
# print("3.sleeper class-500")
# choose = int(input("choose your class: "))
# if choose == 1:
#     fare = 1500
# elif choose ==2:
#     fare = 1000
# elif choose ==3:
#     fare= 500
# else:
#     print("invalid choice")

# if age<5 :
#     fare = 0
#     print("your tickit is free")
# elif age>60:
#     fare = fare-(fare*20/100)
# meal =input("1.do you want meal ")
# if meal =="yes":
#     fare+=200
# else: print("no meal  ")
# print("pasanger name: ",name)
# print("pasanger age: ",age)
# print("meal added: ",meal)
# print("total_fare", fare)


#querry 6
print("Menu")
print("1.Whopper king-150")
print("2.Crispy veg-100")
print("3.chiken wings - 120")
choice= int(input("choose your item(1/2/3):"))
if choice ==1:
    fare = 150
elif choice ==2:
    fare = 100
elif choice ==3:
    fare =120
else:
    print("invalid choice")
quantity = int(input("enter the quantity"))
original_amount = quantity* fare
final_price = original_amount
c = input("do you have coupon yes or no: ")
if c =="yes":
    code = input("enter your coupon")
    if code == "king50":
        final_price = final_price - (50*final_price/100)
        discount_amount ="50%"
    elif code=="bk20":
     final_price = final_price-20
     discount_amount = "20 off"
    else:
     print("no discount")
else:
    print("invalid coupon")
print("original_price",original_amount)
print("final price",final_price)

      







