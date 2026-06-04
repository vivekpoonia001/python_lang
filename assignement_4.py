#question 1
friends =["Vivek", "Dikshit","Maanjot", "Sukhpreet", "Ashish"]
name = input("enter a name")
friends.insert(5, name)
print(friends)
imp_friend = input("enter your important friend")
pos =int(input("enter postion of your imp_friend "))
friends.insert(pos,imp_friend)
print(friends)

#question2
l1 = [1,2,3,4,5,6,7,8,9,10]
print(l1)
n = int(input("enter range "))
l = []
for i in range(1,n+1):
    l.append(i)
print(l)
#question 3
l = [1,10,100,3,6,8]
l.insert(3,59)
l.append(5)
print(l)
print(len(l))

#question 4
new =[]
l = ["vivek ", "suk", "Manjot", "ash", "dikhshit", "dri"]
for i in l:
   if len(i)<4:
    new.append(i)
print(new)
question 5
num_2 = []
num = range(20)
for i in num:
  if i %2==0:
    num_2.append("even")
  if i %2!=0:
    num_2.append("odd")
      
print(num_2)

#another approach taking user input

num = []
num_3 = []
num_1 = int(input("enter range"))
for i in range(num_1):
 
  num_2 = int(input("enter number"))
  num.append(num_2)
print(num)
for i in num:
  if i %2==0:
    num_3.append("even")
  if i %2!=0:
    num_3.append("odd")
print(num_3)
#question 5
num =[]
for i in range(1,1000):
  if i%7==0:
    num.append(i)
print(num)

#question6
l = "hello my name is Vivek Poonia"
print("number of spaces: ",l.count(" "))
#question 8
l3 = []
l=[1,2,4,5,7,8]
l2 = [2,4,5,7,8,0]
for i in l:
    if i in l2:
        print(i)
        l3.append(i)
print(l3)