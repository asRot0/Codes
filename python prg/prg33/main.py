# Examples of Identity operators 
a1 = 3
b1 = 3
a2 = 'GeeksforGeeks'
b2 = 'GeeksforGeeks'
a3 = [1,2,3] 
b3 = [1,2,3] 

# is          True if the operands are identical 
# is not      True if the operands are not identical 

print(a1 is not b1) 


print(a2 is b2) 

# Output is False, since lists are mutable. 
print(a3 is b3) 

# Examples of Membership operator 
x = 'Geeks for Geeks'
y = {3:'a',4:'b'} 

# is          True if the operands are identical 
# is not      True if the operands are not identical 

print('G' in x) 

print('geeks' not in x) 

print('Geeks' not in x) 

print(3 in y) 

print('b' in y) 

# Ternary Operator in Python

# Program to demonstrate conditional operator 
a, b = 10, 20

# Syntax : [on_true] if [expression] else [on_false] 

# Copy value of a in min if a < b else copy b 
min = a if a < b else b 

print(min) 

# Python program to demonstrate ternary operator 
a, b = 10, 20

# Use tuple for selecting an item 
print( (b, a) [a < b] ) 

# Use Dictionary for selecting an item 
print({True: a, False: b} [a < b]) 

# lamda is more efficient than above two methods 
# because in lambda we are assure that 
# only one expression will be evaluated unlike in 
# tuple and Dictionary 
print((lambda: b, lambda: a)[a < b]()) 

# Python program to demonstrate nested ternary operator 
a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b"
		if a > b else "b is greater than a") 

# Python program to demonstrate nested ternary operator 
a, b = 10, 20

if a != b: 
	if a > b: 
		print("a is greater than b") 
	else: 
		print("b is greater than a") 
else: 
	print("Both a and b are equal") 

'''When condition becomes true, expression [on_false]
   is not executed and value of "True and [on_true]"
   is returned.  Else value of "False or [on_false]"
   is returned.
   Note that "True and x" is equal to x. 
   And "False or x" is equal to x. '''
   
# [expression] and [on_true] or [on_false] 

	
# Program to demonstrate conditional operator 
a, b = 10, 20

# If a is less than b, then a is assigned 
# else b is assigned (Note : it doesn't 
# work if a is 0. 
min = a < b and a or b 
min1 = a > b and a or b
print(min) 
print(min1)

# Python program to show use of 
# + operator for different purposes. 

print(1 + 2) 

# concatenate two strings 
print("_hello"+" world") 

# Product two numbers 
print(3 * 4) 

# Repeat the String 
print("hello "*4) 


# Python Program illustrate how 
# to overload an binary + operator 

class A: 
	def __init__(self, a): 
		self.a = a 

	# adding two objects 
	def __add__(self, o): 
		return self.a + o.a 
ob1 = A(1) 
ob2 = A(2) 
ob3 = A("_hello") 
ob4 = A(" world") 

print(ob1 + ob2) 
print(ob3 + ob4) 

# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading. 

class complex: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	# adding two objects 
	def __add__(self, other): 
		return self.a + other.b, self.b + other.a 

	def __str__(self): 
		return self.a, self.b 

Ob1 = complex(1, 2) 
Ob2 = complex(6, 8) 
Ob3 = Ob1 + Ob2 
print(Ob3) 

# Python program to overload 
# a comparison operators 

class A: 
	def __init__(self, a): 
		self.a = a 
	def __gt__(self, other): 
		if(self.a>other.a): 
			return True
		else: 
			return False
ob1 = A(2) 
ob2 = A(3) 
if(ob1>ob2): 
	print("ob1 is greater than ob2") 
else: 
	print("ob2 is greater than ob1") 

# Python program to overload equality 
# and less than operators 

class A: 
	def __init__(self, a): 
		self.a = a 
	def __lt__(self, other): 
		if(self.a<other.a): 
			return "ob1 is less than ob2"
		else: 
			return "ob2 is less than ob1"
	def __eq__(self, other): 
		if(self.a == other.a): 
			return "Both are equal"
		else: 
			return "Not equal"
				
ob1 = A(2) 
ob2 = A(3) 
print(ob1 < ob2) 

ob3 = A(4) 
ob4 = A(4) 
print(ob1 == ob2) 

# Syntax : any(list of iterables)
# Since all are false, false is returned 
print (any([False, False, False, False])) 

# Here the method will short-circuit at the 
# second item (True) and will return True. 
print (any([False, True, False, False])) 

# Here the method will short-circuit at the 
# first (True) and will return True. 
print (any([True, False, False, False])) 

# Syntax : all(list of iterables)
# Here all the iterables are True so all 
# will return True and the same will be printed 
print (all([True, True, True, True])) 

# Here the method will short-circuit at the 
# first item (False) and will return False. 
print (all([False, True, True, False])) 

# This statement will return False, as no 
# True is found in the iterables 
print (all([False, False, False]))
# This statement will return True
# the iterable is empty 
print(all([]))

# Python code to demonstrate working of 
# setitem(), delitem() and getitem() 

# importing operator module 
import operator 

# Initializing list 
li = [1, 5, 6, 7, 8] 

# printing original list 
print ("The original list is : ",end="") 
for i in range(0,len(li)): 
	print (li[i],end=" ") 

print ("\r") 

# using setitem() to assign 3 at 4th position 
operator.setitem(li,3,3) 

# printing modified list after setitem() 
print ("The modified list after setitem() is : ",end="") 
for i in range(0,len(li)): 
	print (li[i],end=" ") 

print ("\r") 

# using delitem() to delete value at 2nd index 
operator.delitem(li,1) 

# printing modified list after delitem() 
print ("The modified list after delitem() is : ",end="") 
for i in range(0,len(li)): 
	print (li[i],end=" ") 

print ("\r") 

# using getitem() to access 4th element 
print ("The 4th element of list is : ",end="") 
print (operator.getitem(li,3)) 
# Python code to demonstrate working of 
# setitem(), delitem() and getitem() 

# importing operator module 
import operator 

# Initializing list 
li = [1, 5, 6, 7, 8] 

# printing original list 
print ("The original list is : ",end="") 
for i in range(0,len(li)): 
	print (li[i],end=" ") 

print ("\r") 

# using setitem() to assign 2,3,4 at 2nd,3rd and 4th index 
operator.setitem(li,slice(1,4),[2,3,4]) 

# printing modified list after setitem() 
print ("The modified list after setitem() is : ",end="") 
for i in range(0,len(li)): 
	print (li[i],end=" ") 

print ("\r") 

# using delitem() to delete value at 3rd and 4th index 
operator.delitem(li,slice(2,4)) 

# printing modified list after delitem() 
print ("The modified list after delitem() is : ",end="") 
for i in range(0,len(li)): 
	print (li[i],end=" ") 

print ("\r") 

# using getitem() to access 1st and 2nd element 
print ("The 1st and 2nd element of list is : ",end="") 
print (operator.getitem(li,slice(0,2))) 

# Python code to demonstrate working of 
# concat() and contains() 

# importing operator module 
import operator 

# Initializing string 1 
s1 = "geeksfor"

# Initializing string 2 
s2 = "geeks"

# using concat() to concatenate two strings 
print ("The concatenated string is : ",end="") 
print (operator.concat(s1,s2)) 

# using contains() to check if s1 contains s2 
if (operator.contains(s1,s2)): 
	print ("geeksfor contains geeks") 
else : print ("geeksfor does not contain geeks") 
# Python code to demonstrate working of 
# and_(), or_(), xor(), invert() 

# importing operator module 
import operator 

# Initializing a and b 

a = 1

b = 0

# using and_() to display bitwise and operation 
print ("The bitwise and of a and b is : ",end="") 
print (operator.and_(a,b)) 

# using or_() to display bitwise or operation 
print ("The bitwise or of a and b is : ",end="") 
print (operator.or_(a,b)) 

# using xor() to display bitwise exclusive or operation 
print ("The bitwise xor of a and b is : ",end="") 
print (operator.xor(a,b)) 

# using invert() to invert value of a 
operator.invert(a) 

# printing modified value 
print ("The inverted value of a is : ",end="") 
print (a) 
# Python code to demonstrate the working of 
# iadd() and iconcat() 

# importing operator to handle operator operations 
import operator 

# using iadd() to add and assign value 
x = operator.iadd(2, 3); 

# printing the modified value 
print ("The value after adding and assigning : ", end="") 
print (x) 

# initializing values 
y = "geeks"

z = "forgeeks"

# using iconcat() to concat the sequences 
y = operator.iconcat(y, z) 

# using iconcat() to concat sequences 
print ("The string after concatenation is : ", end="") 
print (y) 
# Python code to demonstrate the working of 
# isub() and imul() 

# using isub() to subtract and assign value 
x = operator.isub(2, 3); 

# printing the modified value 
print ("The value after subtracting and assigning : ", end="") 
print (x) 

# using imul() to multiply and assign value 
x = operator.imul(2, 3); 

# printing the modified value 
print ("The value after multiplying and assigning : ", end="") 
print (x) 
# Python code to demonstrate the working of 
# itruediv() and imod() 

# using itruediv() to divide and assign value 
x = operator.itruediv(10, 5); 

# printing the modified value 
print ("The value after dividing and assigning : ", end="") 
print (x) 

# using imod() to modulus and assign value 
x = operator.imod(10, 6); 

# printing the modified value 
print ("The value after modulus and assigning : ", end="") 
print (x) 


# Python3 program to illustrate 
# working of AND gate 

def AND (a, b): 

	if a == 1 and b == 1: 
		return True
	else: 
		return False

# Driver code 
if __name__=='__main__': 
	print(AND(1, 1)) 

	print("+---------------+----------------+") 
	print(" | AND Truth Table | Result |") 
	print(" A = False, B = False | A AND B =",AND(False,False)," | ") 
	print(" A = False, B = True | A AND B =",AND(False,True)," | ") 
	print(" A = True, B = False | A AND B =",AND(True,False)," | ") 
	print(" A = True, B = True | A AND B =",AND(True,True)," | ") 

# Python3 program to illustrate 
# working of NAND gate 

def NAND (a, b): 
	if a == 1 and b == 1: 
		return False
	else: 
		return True

# Driver code 
if __name__=='__main__': 
	print(NAND(1, 0)) 

	print("+---------------+----------------+") 
	print(" | NAND Truth Table | Result |") 
	print(" A = False, B = False | A AND B =",NAND(False,False)," | ") 
	print(" A = False, B = True | A AND B =",NAND(False,True)," | ") 
	print(" A = True, B = False | A AND B =",NAND(True,False)," | ") 
	print(" A = True, B = True | A AND B =",NAND(True,True)," | ") 

# Python3 program to illustrate 
# working of OR gate 

def OR(a, b): 
	if a == 1: 
		return True
	elif b == 1: 
		return True
	else: 
		return False

# Driver code 
if __name__=='__main__': 
	print(OR(0, 0)) 

	print("+---------------+----------------+") 
	print(" | OR Truth Table | Result |") 
	print(" A = False, B = False | A AND B =",OR(False,False)," | ") 
	print(" A = False, B = True | A AND B =",OR(False,True)," | ") 
	print(" A = True, B = False | A AND B =",OR(True,False)," | ") 
	print(" A = True, B = True | A AND B =",OR(True,True)," | ") 

# Python3 program to illustrate 
# working of Xor gate 

def XOR (a, b): 
	if a != b: 
		return 1
	else: 
		return 0

# Driver code 
if __name__=='__main__': 
	print(XOR(5, 5)) 

	print("+---------------+----------------+") 
	print(" | XOR Truth Table | Result |") 
	print(" A = False, B = False | A AND B =",XOR(False,False)," | ") 
	print(" A = False, B = True | A AND B =",XOR(False,True)," | ") 
	print(" A = True, B = False | A AND B =",XOR(True,False)," | ") 
	print(" A = True, B = True | A AND B =",XOR(True,True)," | ") 

# Python3 program to illustrate 
# working of Not gate 

def NOT(a): 
	if(a == 0): 
		return 1
	elif(a == 1): 
		return 0
# Driver code 
if __name__=='__main__': 
	print(NOT(0)) 

	print("+---------------+----------------+") 
	print(" | NOT Truth Table | Result |") 
	print(" A = False | A NOT =",NOT(False)," | ") 
	print(" A = True, | A NOT =",NOT(True)," | ") 

# Python3 program to illustrate 
# working of NOR gate 

def NOR(a, b): 
	if(a == 0) and (b == 0): 
		return 1
	elif(a == 0) and (b == 1): 
		return 0
	elif(a == 1) and (b == 0): 
		return 0
	elif(a == 1) and (b == 1): 
		return 0

# Driver code 
if __name__=='__main__': 
	print(NOR(0, 0)) 

	print("+---------------+----------------+") 
	print(" | NOR Truth Table | Result |") 
	print(" A = False, B = False | A AND B =",NOR(False,False)," | ") 
	print(" A = False, B = True | A AND B =",NOR(False,True)," | ") 
	print(" A = True, B = False | A AND B =",NOR(True,False)," | ") 
	print(" A = True, B = True | A AND B =",NOR(True,True)," | ") 

# Python3 program to illustrate 
# working of Not gate 

def XNOR(a,b): 
	if(a == b): 
		return 1
	else: 
		return 0
# Driver code 
if __name__=='__main__': 
	print(XNOR(1,1)) 

	print("+---------------+----------------+") 
	print(" | XNOR Truth Table | Result |") 
	print(" A = False, B = False | A AND B =",XNOR(False,False)," | ") 
	print(" A = False, B = True | A AND B =",XNOR(False,True)," | ") 
	print(" A = True, B = False | A AND B =",XNOR(True,False)," | ") 
	print(" A = True, B = True | A AND B =",XNOR(True,True)," | ") 


# Python program to illustrate 
# Finding common member in list 
# using 'in' operator 
list1=[1,2,3,4,5] 
list2=[6,7,8,9] 
for item in list1: 
	if item in list2: 
		print("overlapping")	 
else: 
	print("not overlapping") 

# Python program to illustrate 
# Finding common member in list 
# without using 'in' operator 

# Define a function() that takes two lists 
def overlapping(list1,list2): 

	c=0
	d=0
	for i in list1: 
		c+=1
	for i in list2: 
		d+=1
	for i in range(0,c): 
		for j in range(0,d): 
			if(list1[i]==list2[j]): 
				return 1
	return 0
list1=[1,2,3,4,5] 
list2=[6,7,8,9] 
if(overlapping(list1,list2)): 
	print("overlapping") 
else: 
	print("not overlapping") 

# Python program to illustrate the use 
# of 'is' identity operator 
x = 5
if (type(x) is int): 
	print("true") 
else: 
	print("false") 
# Python program to illustrate the 
# use of 'is not' identity operator 
x = 5.2
if (type(x) is not int): 
	print("true") 
else: 
	print("false") 
