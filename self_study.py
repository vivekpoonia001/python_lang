# num_1 = int(input("enter range  "))
# sum = 0
# for i in range(1,num_1+1):
#     sum = sum+i
    
# print(sum)

# num_1 = int(input("enter a number "))
# if num_1<=1:
#     print("the number is nor prime niether even ")
# else:
#     for i in range(2,num_1):
#         if num_1%i==0:
#             print("the number is not prime")
#             break
#     else:
#         print("the number is prime")
for i in range(1,101):
    if i %3==0 and i %5==0:
        print("frizzbuzz")
    elif i %3==0:
        print("fizz")
    elif i %5==0:
        print("buzz")
    else:
        print(i)

