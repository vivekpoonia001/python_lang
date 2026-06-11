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
# for i in range(1,101):
#     if i %3==0 and i %5==0:
#         print("frizzbuzz")
#     elif i %3==0:
#         print("fizz")
#     elif i %5==0:
#         print("buzz")
#     else:
#         print(i)

s1 = {1,2,3,4,5,6,7,8,9,0}
print(s1)
s1.update([34,56,78])
print(s1)
s1.remove(9)
print(s1)
s1.discard(9)
print(s1)
a={1,23,45,66,78,54}
b={1,223,434,34,3,4,66,50,78}
print(a|b)
print(a&b)
print(a-b)
if 45 in a:
    print("present ")
else:
    print("not present")

a = [1,23,4,5,67,654,345,65,435]
s =  set(a)
print(s)

def book_flight(destination, class_type = "economy"):
    return f"tickit is booked for {destination}in {class_type} is confirm"
destination = input("enter destination")
class_type = input("enter class type")
if class_type =="":
    print(book_flight(destination))
else:
    print(book_flight(destination, class_type))