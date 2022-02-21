# getting user input

# name = input('name: ')
# age = input("age: ")
# print("you are ", age, " years old, and your name is ", name)


# conditionals

# x = input('Name: ')

# if x == 'Max':
#     print('bruh moment')
# else:
#     print('hello ' + x)


#For loop

# x = [3,5,2,3,6,34,3]
# for i in x:
#     print(i)
# print()
#      # enumerate in this case will keep track of the indexes of the values in a list
# for i, element in enumerate(x):
#     print(i, element)

# #Slice operator
# x = [0,1,2,3,4,5,6,7,8]
# sliced = x[::-1]
# print(sliced)

# x2 = [x + 5 for x in range(5)]
# print(x2)


#Unpack operator

# def func(x,y):
#     print(x,y)

# pairs = [(1,2),(3,4)]

# for pair in pairs:
#     #not the 'pythonic' way to do this
#     func(pair[0],pair[1])
#     #this is the syntactically correct way to do things, even though both will give you the same result
#     func(*pair)


# *args, **kwargs

def func(*args, **kwargs):
    print(args, kwargs)

func(1,2,3,4,54, one=0, two=1)
