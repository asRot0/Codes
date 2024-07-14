# Python program to illustrate 
# nested functions 
def outerFunction(text): 
	text = text 

	def innerFunction(): 
		print(text) 

	innerFunction() 


if __name__ == '__main__': 
	outerFunction('Hey!') 

# Python program to illustrate 
# closures 
def outerFunction(text): 
	text = text 

	def innerFunction(): 
		print(text) 

	return innerFunction # Note we are returning function WITHOUT parenthesis 

if __name__ == '__main__': 
	myFunction = outerFunction('Hey!') 
	myFunction() 

# A Python program to demonstrate that a function 
# can be defined inside another function and a 
# function can be passed as parameter. 

# Adds a welcome message to the string 
def messageWithWelcome(str): 

	# Nested function 
	def addWelcome(): 
		return "Welcome to "

	# Return concatenation of addWelcome() 
	# and str. 
	return addWelcome() + str

# To get site name to which welcome is added 
def site(site_name): 
	return site_name 

print(messageWithWelcome(site("GeeksforGeeks"))) 

# Adds a welcome message to the string 
# returned by fun(). Takes fun() as 
# parameter and returns welcome(). 
def decorate_message(fun): 

	# Nested function 
	def addWelcome(site_name): 
		return "Welcome to " + fun(site_name) 

	# Decorator returns a function 
	return addWelcome 

@decorate_message
def site(site_name): 
	return site_name; 

# Driver code 

# This call is equivalent to call to 
# decorate_message() with function 
# site("GeeksforGeeks") as parameter 
print (site("GeeksforGeeks")) 

# A Python example to demonstrate that 
# decorators can be useful attach data 

# A decorator function to attach 
# data to func 
def attach_data(func): 
	func.data = 3
	return func 

@attach_data
def add (x, y): 
	return x + y 

# Driver code 

# This call is equivalent to attach_data() 
# with add() as parameter 
print(add(2, 3)) 

print(add.data) 


# defining a decorator 
def hello_decorator(func): 

	# inner1 is a Wrapper function in 
	# which the argument is called 
	
	# inner function can access the outer local 
	# functions like in this case "func" 
	def inner1(): 
		print("Hello, this is before function execution") 

		# calling the actual function now 
		# inside the wrapper function. 
		func() 

		print("This is after function execution") 
		
	return inner1 


# defining a function, to be called inside wrapper 
def function_to_be_used(): 
	print("This is inside the function !!") 


# passing 'function_to_be_used' inside the 
# decorator to control its behavior 
function_to_be_used = hello_decorator(function_to_be_used) 





# calling the function 
function_to_be_used() 

def hello_decorator(func): 
	def inner1(*args, **kwargs): 
		
		print("before Execution") 
		
		# getting the returned value 
		returned_value = func(*args, **kwargs) 
		print("after Execution") 
		
		# returning the value to the original frame 
		return returned_value 
		
	return inner1 


# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b): 
	print("Inside the function") 
	return a + b 

a, b = 1, 2

# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b)) 



# Python code to illustrate 
# Decorators with parameters in Python 

def decorator(*args, **kwargs): 
	print("Inside decorator") 
	
	def inner(func): 
		
		# code functionality here 
		print("Inside inner function") 
		print("I like", kwargs['like']) 
		
		func() 
		
	# reurning inner function	 
	return inner 

@decorator(like = "geeksforgeeks") 
def my_func(): 
	print("Inside actual function") 


# Python code to illustrate 
# Decorators with parameters in Python 

def decorator_func(x, y): 

	def Inner(func): 

		def wrapper(*args, **kwargs): 
			print("I like Geeksforgeeks") 
			print("Summation of values - {}".format(x+y) ) 

			func(*args, **kwargs) 
			
		return wrapper 
	return Inner 


# Not using decorator 
def my_fun(*args): 
	for ele in args: 
		print(ele) 

# another way of using dacorators 
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks') 


# Simple recursive program to find factorial 
def facto(num): 
	if num == 1: 
		return 1
	else: 
		return num * facto(num-1) 
		

print(facto(5)) 
