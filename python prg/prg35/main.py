# Declaring the list geek 
geek = ['Geeks', 'Programming', 'Algorithm', 'Article'] 

# Directly printing the list 
print ("Simple List:", geek) 

# Printing the list by join method 
print ('List by using join method: %s' % ', ' .join(geek)) 

# Direct use of join method 
print ('Direct apply the join method:',(", " .join(geek))) 

list1 = [1, 3, 5, 7] 
list2 = [2, 4, 6, 8] 

# Here zip() function takes two equal length list and merges them 
# together in pairs 
for a, b in zip(list1,list2): 
	print (a, b)

# Python 3.x code to demonstrate star pattern 

# Function to demonstrate printing pattern 
def pypart(n): 
	myList = [] 
	for i in range(1,n+1): 
		myList.append("* "*i) 
	print("\n".join(myList)) 

# Driver Code 
n = 5
pypart(n) 

for i in range(1, 4): 
	print(i) 
	break
else: # Not executed as there is a break 
	print("No Break") 

# Python 3.x program to check if an array consists 
# of even number 
def contains_even_number(l): 
	for ele in l: 
		if ele % 2 == 0: 
			print ("list contains an even number") 
			break

	# This else executes only if break is NEVER 
	# reached and loop terminated after all iterations. 
	else:	 
		print ("list does not contain an even number") 

# Driver code 
print ("For List 1:") 
contains_even_number([1, 9, 8]) 
print (" \nFor List 2:") 
contains_even_number([1, 3, 5]) 

# Function to convert number into string 
# Switcher is dictionary data type here 
def numbers_to_strings(argument): 
	switcher = { 
		0: "zero", 
		1: "one", 
		2: "two", 
	} 

	# get() method of dictionary data type returns 
	# value of passed argument if it is present 
	# in dictionary otherwise second argument will 
	# be assigned as default value of passed argument 
	return switcher.get(argument, "nothing") 

# Driver program 
if __name__ == "__main__": 
	argument=0
	print (numbers_to_strings(argument)) 

# A C-style way of accessing list elements 
cars = ["Aston", "Audi", "McLaren"] 
i = 0
while (i < len(cars)): 
	print (cars[i]) 
	i += 1

# Accessing items using for-in loop 

cars = ["Aston", "Audi", "McLaren"] 
for x in cars: 
	print (x) 

# Accessing items using indexes and for-in 

cars = ["Aston", "Audi", "McLaren"] 
for i in range(len(cars)): 
	print (cars[i]) 

# Accessing items using enumerate() 

cars = ["Aston" , "Audi", "McLaren "] 
for i, x in enumerate(cars): 
	print (x) 

# Accessing items and indexes enumerate() 

cars = ["Aston" , "Audi", "McLaren "] 
for x in enumerate(cars): 
	print (x[0], x[1]) 

# demonstrating the use of start in enumerate 

cars = ["Aston" , "Audi", "McLaren "] 
for x in enumerate(cars, start=1): 
	print (x[0], x[1]) 

# Two separate lists 
cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS kit", "Car repair-tool kit"] 

# Single dictionary holds prices of cars and 
# its accessories. 
# First three items store prices of cars and 
# next two items store prices of accessories. 
prices = {1:"570000$", 2:"68000$", 3:"450000$", 
		4:"8900$", 5:"4500$"} 

# Printing prices of cars 
for index, c in enumerate(cars, start=1): 
	print ("Car: %s Price: %s"%(c, prices[index])) 

# Printing prices of accessories 
for index, a in enumerate(accessories,start=1): 
	print ("Accessory: %s Price: %s"%(a,prices[index+len(cars)])) 

		# Python program to demonstrate the working of zip 

# Two separate lists 
cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS", "Car Repair Kit", 
			"Dolby sound kit"] 

# Combining lists and printing 
for c, a in zip(cars, accessories): 
	print ("Car: %s, Accessory required: %s"%(c, a))
		 
# Python program to demonstrate unzip (reverse 
# of zip)using * with zip function 

# Unzip lists 
l1,l2 = zip(*[('Aston', 'GPS'), 
			('Audi', 'Car Repair'), 
			('McLaren', 'Dolby sound kit') 
		]) 

# Printing unzipped lists	 
print(l1) 
print(l2) 

# Python code to demonstrate the working of 
# accumulate() and chain() 

# importing "itertools" for iterator operations 
import itertools 

# importing "operator" for operator operations 
import operator 

# initializing list 1 
li1 = [1, 4, 5, 7] 

# initializing list 2 
li2 = [1, 6, 5, 9] 

# initializing list 3 
li3 = [8, 10, 5, 4] 

# using accumulate() 
# prints the successive summation of elements 
print ("The sum after each iteration is : ",end="") 
print (list(itertools.accumulate(li1))) 

# using accumulate() 
# prints the successive multiplication of elements 
print ("The product after each iteration is : ",end="") 
print (list(itertools.accumulate(li1,operator.mul))) 

# using chain() to print all elements of lists 
print ("All values in mentioned chain are : ",end="") 
print (list(itertools.chain(li1,li2,li3))) 

# Python code to demonstrate the working of 
# chain.from_iterable() and compress() 

# importing "itertools" for iterator operations 
import itertools 

# initializing list 1 
li1 = [1, 4, 5, 7] 

# initializing list 2 
li2 = [1, 6, 5, 9] 

# initializing list 3 
li3 = [8, 10, 5, 4] 

# intializing list of list 
li4 = [li1, li2, li3] 

# using chain.from_iterable() to print all elements of lists 
print ("All values in mentioned chain are : ",end="") 
print (list(itertools.chain.from_iterable(li4))) 

# using compress() selectively print data values 
print ("The compressed values in string are : ",end="") 
print (list(itertools.compress('GEEKSFORGEEKS',[1,0,0,0,0,1,0,0,1,0,0,0,0]))) 

# Python code to demonstrate the working of 
# dropwhile() and filterfalse() 

# importing "itertools" for iterator operations 
import itertools 

# initializing list 
li = [2, 4, 5, 7, 8] 

# using dropwhile() to start displaying after condition is false 
print ("The values after condition returns false : ",end="") 
print (list(itertools.dropwhile(lambda x : x%2==0,li))) 

# using filterfalse() to print false values 
print ("The values that return false to function are : ",end="") 
print (list(itertools.filterfalse(lambda x : x%2==0,li))) 

# Python code demonstrating 
# basic use of iter() 
lst = [11, 22, 33, 44, 55] 

iter_lst = iter(lst) 
while True: 
	try: 
		print(iter_lst.__next__()) 
	except:
		break
	

# Python code demonstrating 
# basic use of iter() 

listB = ['Cat', 'Bat', 'Sat', 'Mat'] 


iter_listB = listB.__iter__()

try: 
	print(iter_listB.__next__()) 
	print(iter_listB.__next__()) 
	print(iter_listB.__next__()) 
	print(iter_listB.__next__()) 
	print(iter_listB.__next__()) #StopIteration error 
except: 
	print(" \nThrowing 'StopIterationError'", 
					"I cannot count more.") 

# Python code showing use of iter() using OOPs 

class Counter: 
	def __init__(self, start, end): 
		self.num = start 
		self.end = end 

	def __iter__(self): 
		return self

	def __next__(self): 
		if self.num > self.end: 
			raise StopIteration 
		else: 
			self.num += 1
			return self.num - 1
			
			
# Driver code 
if __name__ == '__main__' : 
	
	a, b = 2, 5
	
	c1 = Counter(a, b) 
	c2 = Counter(a, b) 
	
	# Way 1-to print the range without iter() 
	print ("Print the range without iter()") 
	
	for i in c1: 
		print ("Eating more Pizzas, couting ", i, end ="\n") 
	
	print ("\nPrint the range using iter()\n") 
	
	# Way 2- using iter() 
	obj = iter(c2) 
	try: 
		while True: # Print till error raised 
			print ("Eating more Pizzas, couting ", next(obj)) 
	except: 
		# when StopIteration raised, Print custom message 
		print ("\nDead on overfood, GAME OVER") 

# Function to check object 
# is iterable or not 
def iterable(obj): 
	try: 
		iter(obj) 
		return True
		
	except TypeError: 
		return False

# Driver Code	 
for element in [34, [4, 5], (4, 5), 
			{"a":4}, "dfsdf", 4.5]: 
				
	print(element, " is iterable : ", iterable(element)) 

# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 1			
	yield 2			
	yield 3		
	yield 'hello'

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value) 

string = 'geek'
li = list(string[i] for i in range(len(string)-1, -1, -1)) 
print(li) 
