'''functions : A function is a block of code that performs a specific task and can be reused multiple times.'''

def add():
    a=10
    b=10
    print(a+b)
add() # function calling

def add(a,b):
    print(a-b)
# add(9,8)
add(b=14,a=12) # function calling

'''args : *args - multiple arguments are passed using *args'''
def func(*num):
    print(sum(num))# gives sum of the number 
    print(len(num))# gives length of args passed 
    print(max(num))# gives maximum number in args
    print(min(num))# gives minimum number in args
    print(num.count(1))# counts how many time 1 appears in args
    print(num.index(3))# prints the index of 3

    for i in num:
        print(i)

func(1,2,3,4,5,5)


'''kwargs : **kwargs - key,value pair are passed using **kwargs'''

def func(**k_value):
    print(k_value)
    print(k_value.keys())# gives the keys.
    print(k_value.values())# gives the values.
    print(k_value.items())#Each key-value pair is represented as a tuple, but the original dictionary is unchanged.
    print(k_value.get("name"))# gets the value for specific key or value.
    print(k_value.update({"city":"Punjab"}))# adds a key value pair.
    print(k_value.pop("age"))


func(name="Dikshit",age=22)



    

    