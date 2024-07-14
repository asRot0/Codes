# This function uses global variable s 
def f(): 
	print(s) 

# Global scope 
s = "I love _hello world"
f() 


# This function has a variable with 
# name same as s. 
def f(): 
	s = "Me too."
	print(s) 

# Global scope 
s = "I love _hello world"
f() 
print(s) 

# This function modifies global variable 's' 
def f(): 
	global s 
	print (s) 
	s = "Look for _hello world Python Section"
	print (s) 

# Global Scope 
s = "Python is great!"
f() 
print (s) 

a = 1

# Uses global because there is no local 'a' 
def f(): 
	print ('Inside f() : ', a)

# Variable 'a' is redefined as a local 
def g():	 
	a = 2
	print ('Inside g() : ',a) 

# Uses global keyword to modify global 'a' 
def h():	 
	global a 
	a = 3
	print ('Inside h() : ',a) 

# Global scope 
print ('global : ',a) 
f() 
print ('global : ',a) 
g() 
print ('global : ',a) 
h() 
print ('global : ',a) 

# A sample function that takes 4 arguments 
# and prints the, 
def fun(a, b, c, d): 
	print(a, b, c, d) 

# Driver Code 
my_list = [1, 2, 3, 4] 

# Unpacking list into four arguments 
# We can use * to unpack the list 
fun(*my_list) 

# A Python program to demonstrate use 
# of packing 

# This function uses packing to sum 
# unknown number of arguments 
def mySum(*args): 
	sum = 0
	for i in range(0, len(args)): 
		sum = sum + args[i] 
	return sum

# Driver code 
print(mySum(1, 2, 3, 4, 5)) 
print(mySum(10, 20)) 

# A Python program to demonstrate both packing and 
# unpacking. 

# A sample python function that takes three arguments 
# and prints them 
def fun1(a, b, c): 
	print(a, b, c) 

# Another sample function. 
# This is an example of PACKING. All arguments passed 
# to fun2 are packed into tuple *args. 
def fun2(*args): 

	# Convert args tuple to a list so we can modify it 
	args = list(args) 

	# Modifying args 
	args[0] = '_hello world'
	args[1] = 'awesome'

	# UNPACKING args and calling fun1() 
	fun1(*args) 

# Driver code 
fun2('Hello', 'beautiful', 'world!') 


# A sample program to demonstrate unpacking of 
# dictionary items using ** 
def fun(a, b, c): 
	print(a, b, c) 

# A call with unpacking of dictionary 
d = {'a':2, 'b':4, 'c':10} 
fun(**d) 

# A Python program to demonstrate packing of 
# dictionary items using ** 
def fun(**kwargs): 

	# kwargs is a dict 
	print(type(kwargs)) 

	# Printing dictionary items 
	for key in kwargs: 
		print("%s = %s" % (key, kwargs[key])) 

# Driver code 
fun(name="geeks", ID="101", language="Python") 

# Python code to demonstrate Type conversion 
# using int(), float() 

# initializing string 
s = "10010"

# printing string converting to int base 2 
# int(a,base)
c = int(s,2) 
print ("After converting to integer base 2 : ", end="") 
print (c) 

# printing string converting to float 
e = float(s) 
print ("After converting to float : ", end="") 
print (e) 
# Python code to demonstrate Type conversion 
# using ord(), hex(), oct() 

# initializing integer 
s = '4'

# printing character converting to integer 
c = ord(s) 
print ("After converting character to integer : ",end="") 
print (c) 

# printing integer converting to hexadecimal string 
c = hex(56) 
print ("After converting 56 to hexadecimal string : ",end="") 
print (c) 

# printing integer converting to octal string 
c = oct(56) 
print ("After converting 56 to octal string : ",end="") 
print (c) 
# Python code to demonstrate Type conversion 
# using tuple(), set(), list() 

# initializing string 
s = 'hello'

# printing string converting to tuple 
c = tuple(s) 
print ("After converting string to tuple : ",end="") 
print (c) 

# printing string converting to set 
c = set(s) 
print ("After converting string to set : ",end="") 
print (c) 

# printing string converting to list 
c = list(s) 
print ("After converting string to list : ",end="") 
print (c) 
# Python code to demonstrate Type conversion 
# using dict(), complex(), str() 

# initializing integers 
a = 1
b = 2

# initializing tuple 
tup = (('a', 1) ,('f', 2), ('g', 3)) 

# printing integer converting to complex number 
c = complex(1,2) 
print ("After converting integer to complex number : ",end="") 
print (c) 

# printing integer converting to string 
c = str(a) 
print ("After converting integer to string : ",end="") 
print (c) 

# printing tuple converting to expression dictionary 
c = dict(tup) 
print ("After converting tuple to dictionary : ",end="") 
print (c) 
# Convert ASCII value to characters 
# using chr()
a = chr(76) 
b = chr(77) 

print(a) 
print(b) 


# Python code to demonstate String encoding 

# initialising a String 
a = 'GeeksforGeeks'

# initialising a byte object 
c = b'GeeksforGeeks'

# using encode() to encode the String 
# encoded version of a is stored in d 
# using ASCII mapping 
d = a.encode('ASCII') 

# checking if a is converted to bytes or not 
if (d==c): 
	print ("Encoding successful") 
else : print ("Encoding Unsuccessful") 
# Python code to demonstate Byte Decoding 

# initialising a String 
a = 'GeeksforGeeks'

# initialising a byte object 
c = b'GeeksforGeeks'

# using decode() to decode the Byte object 
# decoded version of c is stored in d 
# using ASCII mapping 
d = c.decode('ASCII') 

# checking if c is converted to String or not 
if (d==a): 
	print ("Decoding successful") 
else : print ("Decoding Unsuccessful") 

# Python program to swap two variables in single line 
x = 5
y = 10
x, y = y, x 
print ("After Swapping values of x and y are",end=" ") 
print("x=",x,"y=",y)

# File1.py 

print ("File1 __name__ = %s" %__name__) 

if __name__ == "__main__": 
	print ("File1 is being run directly")
else: 
	print ("File1 is being imported")

# File2.py 

import File1 

print ("File2 __name__ = %s" %__name__) 

if __name__ == "__main__": 
	print ("File2 is being run directly")
else: 
	print ("File2 is being imported")
