with open ("student.txt", "w") as file:
    file.write("Vivek\n")
    file.write("Ashish\n")
    file.write("Dikshit\n")
    print("sucsesfully added to 'student.txt' ")


# print("\nreading contents of 'student.txt' ")   
# with open ("student.txt", "r") as file:
#     contents = file.read()
#     print(contents)

# with open("student.txt", "a") as file:
#      gndwa= file.write("manjot\n")
#      print("appdend vlaue is david")
#      print(gndwa)
# with open ("student.txt", "r") as file:
#      contents = file.read()
#      print(contents)
# print("reading line by line")
# with open ("student.txt", "r") as file:
#      for line in file:
#           print("student:{} ". format(line.strip()))

# print("read all lines into list")
# with open ("student.txt", "r") as file:
#      l_l = file.readlines()
#      print("list of lines",l_l)       
#      print("leng of list", len(l_l))   \

print("print mulitple lines at a time\n")
new_students =("jogi\n", "nishtant\n","Vivek")
with open ("new_students", "w" ) as file:
     file.writelines(new_students)
print("sucssesfully wrote names'new_students")