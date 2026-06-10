def seprate_section(tittle):
    print("\n"+"="*20+tittle +"="*20)

'''lambda function : A lambda function is a small, 
anonymous function in Python that can take any number of arguments but contains only one expression. 
It is created using the lambda keyword and automatically returns the result of that expression.'''
'''syntax : lambda arguments : expression'''
'''for example : double = lambda x : x*2'''
seprate_section("1. lambda function")
# double = lambda x: x**2
# x = int(input("enter your number:"))
# print("power of ",x,"is",double(x))

# even_odd = lambda x: "even" if x%2==0 else "odd"
# x = int(input("enter your number"))
# print("the number is ",even_odd(x))

'''map functions : map() is a built-in Python function 
that applies a specified function to every element of an iterable and returns an iterator containing the results. '''
'''syntax : map(function, iterable)'''
'''for example : map(lambda x: x * 2, [1, 2, 3])'''
seprate_section("2. map function")

# l = ["1","2","3","4","5","6","7"]
#  convt = map(int, l)
# print("the list is converted to integer",list (convt))
# l1 = [1,2,3,4,5,6,7]
# square_1 = map(lambda x:x**2,l1)
# print("square of that number is ",list(square_1))

''' zip function : zip() is a built-in Python function
 that combines elements from two or more iterables into tuples based on their corresponding positions.'''
'''syntax : zip(iterable1, iterable2, ...)'''
'''for example : zip([1, 2, 3], ['A', 'B', 'C'])'''
# seprate_section("3. zip function")
# l2 = ["Dikshit","Vivek", "Sukh","Manjot","Ashish"]
# l3 = ["Himachal","Rajsathan","Punjab","Harayana","Pahad"]
# merge_1 = dict(zip(l2,l3))
# print("zipped list ",merge_1)


'''enumerate function : enumerate() is a built-in Python function 
that adds a counter (index) to an iterable and returns an iterator of index-value pairs.'''
'''syntax : enumerate(iterable, start=0)'''
'''for example : enumerate(['Apple', 'Banana', 'Mango'], start=1) '''
seprate_section("4. enumerate function")
# l5= ["Dikshit","Vivek", "Sukh","Manjot","Ashish"]
# for index , names in enumerate(l5,start = 1):
#     print(index,names)


'''filter function : The filter() function is a built-in Python function
 that filters elements from an iterable based on a specified condition and 
 returns an iterator containing only the elements for which the condition is True.'''
'''syntax : filter(function, iterable)'''
'''example : filter(lambda x: x % 2 == 0, [1, 2, 3, 4])'''
seprate_section("5. filter function")

ages = [14,25,34,21,12,23,17]
def func_1(age):
    if age<18:
        return False
    else:
        return True
filters_1 = filter(func_1,ages)
print("these person only can give vote",list(filters_1))

