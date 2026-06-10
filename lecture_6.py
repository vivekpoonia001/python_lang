# dictonary {},m key :value pair, orderd , indexed, mutable
d = {}# it will give dictinoary type 
dict_1 = {"name": "Vivek", "age ": 20, "gender": "male"}
print(dict_1)
print(dict_1["age"])
dict_1.update(name = "VIvek Poonia")
dict_1["age"] = 30
print(dict_1)
dict_1.pop("age")
print(dict_1)
print(dict_1.get("age", "not present in dictonary"))
print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())
for i,j in dict_1.items():
    print(i,"---",j)
dict_2 = {"name":{"firstname":"rahul", "lastname":"Poonia"} , "age" :20,
          "address":{"per":"Pilani","temp":"Mohali"}}
print(dict_2)
print(dict_2["name"]["firstname"])
#dictonary comprehension
dict_3 = {i:i**2 for i in range(10)}
print(dict_3)
print(dict_3[8])
dict_4 ={i**2:i for i in range(4) if(i**2)%2==0}
print(dict_4)
a = {1,2,3}
v = {"a","b","c"}
dict_5 = {i:j for i ,j in zip(a,v)}
print(dict_5)
d = {}
for i in range(5):
    d[int(input("enter index: "))] = input("enter the value: ")
print(d)
print(d[3])
dict_1 = { "Name": "Vivek", "age": 20, "city": "Mohali" }
print(dict_1)
print(dict_1['age'])
dict_1["Course"] = "Data Anlayst"
print(dict_1)
dict_1.update(age = 21)
print(dict_1)
print(dict_1.keys())
print(dict_1.values())
print(dict_1, end ="\n")
for key , values in dict_1.items():
    print(key,":",values)
print(len(dict_1))
d = input("enter a key ")
if d in dict_1:
    print("key found",dict_1[d])
else:
    print("key not found")
marks = { "english":90, "maths":99,"bio":95
}
dict_1.pop("age")
print(dict_1)
d = {}
for i in range(5):
    d[int(input("enter index value"))] = input("enter value ")
print(d)
dict_1 = {i: i**2 for i in range(15)}
print(dict_1)
dict_2 = {i:i**2 for i in range(1,11)if i%2==0}
print(dict_2) 
dict_1 = {}