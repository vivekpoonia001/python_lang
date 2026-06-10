#question 1
dict_1 = input("enter a string")
a = dict_1.split(" ")
print(a)
count = {}
for i in a :
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
print(count)


#question 2
# n = int(input("enter the range"))
# d = {}
# for i in range(1,n+1):
#     d[int(input("enter index value "))] = input("enter value ")
# print(d)
# total_marks = sum(d.values())
# avg_marks = total_marks//n
# print(avg_marks)


