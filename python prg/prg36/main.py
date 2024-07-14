# A simple Python function to check 
# whether x is even or odd 
def evenOdd( x ): 
	if (x % 2 == 0): 
		print ("even")
	else: 
		print ("odd")

# Driver code
evenOdd(6)
evenOdd(7)

def swap(x, y): 
	temp = x; 
	x = y; 
	y = temp; 

# Driver code 
x = 2
y = 3
swap(x, y) 
print(x) 
print(y) 

# Python program to demonstrate 
# default arguments 
def myFun(x, y=50): 
	print("x: ", x) 
	print("y: ", y) 

# Driver code (We call myFun() with only 
# argument) 
myFun(10) 

# Python program to demonstrate Keyword Arguments 
def student(firstname, lastname): 
	print(firstname, lastname) 
	
	
# Keyword arguments				 
student(firstname ='_hello', lastname ='world')	 
student(lastname ='world', firstname ='_hello') 

# Python program to illustrate 
# *args for variable number of arguments 
def myFun(*argv): 
	for arg in argv: 
		print (arg) 
	
myFun('Hello', 'Welcome', 'to', 'Home') 

# Python program to illustrate 
# *args with first extra argument 
def myFun(arg1, *argv): 
	print ("First argument :", arg1) 
	for arg in argv: 
		print("Next argument through *argv :", arg) 

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 

# Python program to illustrate 
# *kargs for variable number of keyword arguments 

def myFun(**kwargs): 
	for key, value in kwargs.items(): 
		print ("%s == %s" %(key, value)) 

# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')	 

def myFun(*args,**kwargs): 
	print("args: ", args) 
	print("kwargs: ", kwargs) 


# Now we can use both *args ,**kwargs to pass arguments to this function : 
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks") 

# Python code to illustrate cube of a number 
# using labmda function 
	
cube = lambda x: x*x*x 
print(cube(6)) 

# Python program to demonstrate 
# use of class method and static method. 
from datetime import date 

class Person: 
	def __init__(self, name, age): 
		self.name = name 
		self.age = age 
	
	# a class method to create a Person object by birth year. 
	@classmethod
	def fromBirthYear(cls, name, year): 
		return cls(name, date.today().year - year) 
	
	# a static method to check if a Person is adult or not. 
	@staticmethod
	def isAdult(age): 
		return age > 18

person1 = Person('mayank', 21) 
person2 = Person.fromBirthYear('mayank', 1996) 

print (person1.age) 
print (person2.age) 

# print the result 
print (Person.isAdult(22)) 

# A Simple Python program to demonstrate working 
# of yield 

# A generator function that yields 1 for the first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 'a'
	yield 'b'
	yield 'c'

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value) 

# A Python program to generate squares from 1 
# to 100 using yield and therefore generator 

# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
	i = 1; 

	# An Infinite loop to generate squares 
	while True: 
		yield i*i				 
		i += 1 # Next execution resumes 
				# from this point	 

# Driver code to test above generator 
# function 
for num in nextSquare(): 
	if num > 100: 
		break	
	print(num) 

# A Python program to return multiple 
# values from a method using class 
class Test: 
	def __init__(self): 
		self.str = "_hello world"
		self.x = 20

# This function returns an object of Test 
def fun(): 
	return Test() 
	
# Driver code to test above method 
t = fun() 
print(t.str) 
print(t.x) 

# A Python program to return multiple 
# values from a method using tuple 

# This function returns a tuple 
def fun(): 
	str = "_hello world"
	x = 20
	return str, x; # Return tuple, we could also 
					# write (str, x) 

# Driver code to test above method 
str, x = fun() # Assign returned tuple 
print(str) 
print(x) 
# A Python program to return multiple 
# values from a method using list 

# This function returns a list 
def fun(): 
	str = "_hello world"
	x = 20
	return [str, x];

# Driver code to test above method 
list = fun() 
print(list) 
# A Python program to return multiple 
# values from a method using dictionary 

# This function returns a dictionary 
def fun(): 
	d = dict(); 
	d['str'] = "_hello world"
	d['x'] = 20
	return d 

# Driver code to test above method 
d = fun() 
print(d) 

# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
	return text.upper() 

def whisper(text): 
	return text.lower() 

def greet(func): 
	# storing the function in a variable 
	greeting = func("Hi, I am created by a function passed as an argument.") 
	print (greeting) 

greet(shout) 
greet(whisper) 

# Python program to illustrate functions 
# Functions can return another function 

def create_adder(x): 
	def adder(y): 
		return x+y 

	return adder 

add_15 = create_adder(15) 

print (add_15(10)) 

# Python code to demonstrate ceil(), trunc() 
# and floor() 

# importing "math" for precision function 
import math 

# initializing value 
a = 6.78

# using trunc() to print integer after truncating 
print ("The integral value of number is : ",end="") 
print (math.trunc(a)) 

# using ceil() to print number after ceiling 
print ("The smallest integer greater than number is : ",end="") 
print (math.ceil(a)) 

# using floor() to print number after flooring 
print ("The greatest integer smaller than number is : ",end="") 
print (math.floor(a)) 
# Python code to demonstrate precision 
# and round() 

# initializing value 
a = 3.4536

# using "%" to print value till 2 decimal places 
print ("The value of number till 2 decimal place(using %) is : ",end="") 
print ('%.2f'%a) 

# using format() to print value till 2 decimal places 
print ("The value of number till 2 decimal place(using format()) is : ",end="") 
print ("{0:.2f}".format(a)) 

# using round() to print value till 2 decimal places 
print ("The value of number till 2 decimal place(using round()) is : ",end="") 
print (round(a,2)) 
