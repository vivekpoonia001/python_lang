#list comprihension
# s = [1,2,3,4,5]
# m = [ i **2 for i in s ]
# print(m)
# type_num = ["odd" if x%2!=0 else "even" for x in s]
# print(s)
# print(type_num)
# l = [21,56,12,-12,15,-25,-30,45]
# neg_z = [0 if i<0 else i for i in l ]
# print(neg_z)
# num = [4,5,6,7,8]
# num_1 = [i for i in num if i**2>50]
# print(num_1)
# words = ["appple", "elephant","banana","dog","computer","cat"]
# words_1 = [i for i in words if len(i)>5]
# print(words_1)



#tuples
''' it is immutable 
stores the value in orderd format
it allow to store the duplicate value
example==(2,4,567,788)'''
# a = 12,3,4,45
# print(a)
# b = (24)# this is integer
# c = (23,)# this is tuple
# print(a[2:])
# l = ("vivek", 123,34 ,24.5,"!")
# print(l)
# print(len(l))
# t = (1,2,3,4,4,5,6,4)
# print(t.count(4))
# print(t.index(4))
# t1=(1,2,3,4,5,6,7,8)
# t2= (2,567,78,9,6,0)
# t3 = t1+t2
# print(t3)





#sets 
'''
it is a mutable data type 
unindexed 
stores the value in unodered format 
do not allow the duplicate vlaues
defined by {}
# it can store hetrogenous values'''
# a= {}
# b = {15}
# print(type(a))
# print(type(b))
#if i have to use empty set then i have to use set()
# d = set()
# s1 = {24,455,654,24,"vivek"}
# print(s1)
# for s in s1:
#     print(s, end=" ")
    # adding element in the sets

# s1.add("Manjot")
# print(s1)
# dding multiple elemnts in sets then we ahve to use update function
# s1.update([2,45,"Ashish"])
# print(s1)
# s1.pop()
# print(s1)
# s1.remove(45)
# print(s1)
# s1.discard(45)
# print(s1)
# s1.remove(888)# it will give key error 
# print(s1)
# s1.discard(888)# it will run 
# print(s1)
''' unnion 
intersection
difference 
symmetric '''
a = {1,2,3,45,67,7,8}
b = {4,5678,9876,5434567,6543,34,5,6}
print(a|b)#union
print(a&b)#intersection
print(a-b)# diffrence it will print elemts which are present in a 
print(a^b)# elements that are not coommon in both 
print(a.issubset(b))
f= frozenset({1,23,45,6,7})
print(f)
f.add(8)#it will produce error it becomes immmutable 