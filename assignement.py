''''question 1'''
student_name = input("enter the name of student ")
class_1 = int (input("enter the class of the student"))
section = input("enter the section of the student ")
marks_1 = int(input("enter the marks of first subject 1:"))
marks_2 = int(input("enter the marks of first subject 2:"))
marks_3 = int(input("enter the marks of first subject 3:"))
marks_4 = int(input("enter the marks of first subject 4:"))
marks_5 = int(input("enter the marks of first subject 5:"))

total_marks = 500
total_marks_obtained = marks_1 + marks_2 + marks_3 + marks_4 + marks_5
percentage = (total_marks_obtained/total_marks)*100
print(f"Name of the student is {student_name}\nclass is {class_1}, section is {section}\npercentage is {percentage}")
'''second question'''
# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# num3 = int(input("enter third number:"))
# print("the sum of three number is ", num1+num2+num3)
'''third question'''
# num = int(input("entter a number:"))
# print("the square of number is ",num*num)

'''fourth question'''
# temp = input("enter the temprature in celcius:")
# celcius = float(temp)
# fahrenheit = (celcius*9/5)+32
# print("tempin celcuis is:",celcius, "temp in fahrenheit is:", fahrenheit)
# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# quetiont = num1//num2
# remainder = num1%num2
# print("the number is quotient:", quetiont, "the number is remainder:", remainder)

'''fifth question   '''
p = int(input("enter the principal amount:"))
r = int(input("enter the rate of interest:"))
t = int(input("enter the time in years:"))
simple_interest = (p*r*t)/100
print("the simple interest is:", simple_interest)