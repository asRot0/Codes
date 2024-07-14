'''  Python user can take multiple values or inputs in one line by two methods.
>>> Using split() method
>>> Using List comprehension  '''

# Using split() method :
# It breaks the given input by the specified separator. If separator is not provided then any white space is a separator

# Syntax : input().split(separator, maxsplit)

# Python program showing how to 
# multiple input using split 

# taking two inputs at a time 
x, y = input("Enter a two value: ").split() 
print("Number of boys: ", x) 
print("Number of girls: ", y) 
print() 

# taking three inputs at a time 
x, y, z = input("Enter a three value: ").split() 
print("Total number of students: ", x) 
print("Number of boys is : ", y) 
print("Number of girls is : ", z) 
print() 

# taking two inputs at a time 
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print() 

# taking multiple inputs at a time 
# and type casting using list() function 
x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x) 
y =list(input("enter:").split())
print("second list:",y)

# Using List comprehension :
# List comprehension is an elegant way to define and create list in Python

# Python program showing 
# how to take multiple input 
# using List comprehension 

# taking two input at a time 
x, y = [int(x) for x in input("Enter two value: ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print() 

# taking three input at a time 
x, y, z = [int(x) for x in input("Enter three value: ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print("Third Number is: ", z) 
print() 

# taking two inputs at a time 
x, y = [int(x) for x in input("Enter two value: ").split()] 
print("First number is {} and second number is {}".format(x, y)) 
print() 

# taking multiple inputs at a time 
x = [int(x) for x in input("Enter multiple value: ").split()] 
print("Number of list is: ", x) 