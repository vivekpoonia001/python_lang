# s1 = {1,2,3,4,5,6,7,8,9,0}
# print(s1)
# s1.update([34,56,78])
# print(s1)
# s1.remove(9)
# print(s1)
# s1.discard(9)
# print(s1)
# a={1,23,45,66,78,54}
# b={1,223,434,34,3,4,66,50,78}
# print(a|b)
# print(a&b)
# print(a-b)
# if 45 in a:
#     print("present ")
# else:
#     print("not present")

# a = [1,23,4,5,67,654,345,65,435]
# s =  set(a)
# print(s)


#tuole querries
# a =("Vivek ", "Nishant", "Jogender","Uttam","pandat")
# for i in a:
#  print(a)

# a1 = (1,2,3,4,5,6,78,7654,3,3,5,65432)
# # print(a1.count(3))
# a2 =(1,223,456,765,433567,7654,337,6,5,43,2,4,57)
# print(a1+a2)



#comphresion querries 
l1= ["vivek", "Jogi", "nishant", "kutta"]
# l2 = [i**2 for i in l1]
# print(l2)
# l4=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# l3=[i for i in l4 if i%2==0 ]
# print(l3)
# l5 = int(input("enter start point "))
# l6 = int(input("enter end point"))
# l7 = list(range(l5,l6+1))
# l8=[i for i in l7 if i%2==0]
# print(l8)
# l2 = [i.upper() for i in l1]
# print(l2)
l2 = [len(i) for i  in l1]
print(l2)
# print(l1[0])
l1 = int(input("enter a starting point "))
l2 = int(input("enter ending point"))
l3= list(range(l1,l2+1))
l4=[i for i in l3 if i%2==0 and i%5==0]
print(l4)

