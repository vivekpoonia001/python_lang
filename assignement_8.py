def seprate_section(tittle):
    print("\n"+"="*20+tittle +"="*20)

# seprate_section("First Question")
# calculate_volume = lambda b,w:(b*w)
# b = int(input("enter breadth of prism"))
# w = int(input("enter your height"))

# print("the volume of prism is ",calculate_volume(b,w))

# seprate_section("second question")
# checker = lambda x:"even" if x%2==0 else "odd"
# x = int(input("enter your number"))
# print("the number is ",checker(x))


# seprate_section("third Question")

# string_1 = lambda s :s[::-1]
# s = input("enter string")
# print("string is reveresed",string_1(s))


# seprate_section("Question 4")
# s1 = ["15", "42", "7"]
# convt = map(int,s1)
# print("converted list is ",list(convt))


# seprate_section("question 5")
# s2 = ["vivek", "dikhit"]
# convter = map(str.upper,s2)
# print("upper case of list is ",list(convter))

# seprate_section("question 6")
# l = [1,2,3,45,667,7,88]
# squared_num = map(lambda x : x**2,l)
#  print("squared num is",list(squared_num))

# seprate_section("Question 7")
# num = [-1,2,-34,435,-345,54,45]
# doc_1 = filter(lambda n : n>1,num )
# print("these numbers are positve",list(doc_1))

# seprate_section("Question 8")
# l1 = ["Vivek", "Dikshit", "sukh","Asish","King"]
# checkk_1 = filter(lambda n: len(n)>5,l1)
# print("the string which has more than 5 characters",list(checkk_1))

# seprate_section("question 9 ")
# l2 = [1,"vivek",2,2.13,"Dikshit"]
# letit = filter(lambda x: isinstance(x,str), l2)
# print("the string words are", list(letit))

# seprate_section("Question 10")
# l = ["mango", "apple","grapes","watermelon"]
# for index , fruits in enumerate(l, start = 1):
#     print(index, fruits)

# seprate_section("question 11")
# l = "python"
# print(list(l))
# ess = enumerate(l,start = 1)
# print("words are ",tuple(ess))

seprate_section("question 12")
l = [True, False, True,False,False]
new_list =[]
for  index , value in enumerate(l,start=0):
    if value:
        new_list.append(index)
print(new_list)