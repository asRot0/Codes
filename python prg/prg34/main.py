#Python program to illustrate 
# combining else with while 
count = 0
while (count < 3):	 
	count = count + 1
	print("_hello world") 
else: 
	print("In Else Block") 
	
count = 0
while (count < 3):	 
	count = count+1
	print(count) 
	break
else: 
	print("No Break") 

# Python program to illustrate 
# Iterating over a list 
print("List Iteration") 
l = ["geeks", "for", "geeks"] 
for i in l: 
	print(i) 
	
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
	print(i) 
	
# Iterating over a String 
print("\nString Iteration")	 
s = "Geeks"
for i in s : 
	print(i) 
	
# Iterating over dictionary 
print("\nDictionary Iteration") 
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d : 
	print("%s %d" %(i, d[i])) 
# Python program to illustrate 
# combining else with for 

list = ["geeks", "for", "geeks"] 
for index in range(len(list)): 
	print (list[index]) 
else: 
	print ("Inside Else Block")

# Python program to illustrate 
# nested for loops in Python 
# from __future__ import print_function 
for i in range(1, 5): 
	for j in range(i): 
		print(j+1, end=' ') 
	print() 
# Prints all letters except 'e' and 's' 
for letter in 'geeksforgeeks': 
	if letter == 'e' or letter == 's': 
		continue
	print ('Current Letter :', letter) 
	var = 10
for letter in 'geeksforgeeks': 

	# break the loop as soon it sees 'e' 
	# or 's' 
	if letter == 'e' or letter == 's': 
		break

print ('Current Letter :', letter) 
# An empty loop 
for letter in 'geeksforgeeks': 
	pass
print ('Last Letter :', letter) 

# python code to demonstrate working of enumerate() 

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']): 
	print(key+1, value) 

# python code to demonstrate working of zip() 

# initializing list 
questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle'] 

# using zip() to combine two containers 
# and print values 
for question, answer in zip(questions, answers): 
	print('What is your {0}? I am {1}.'.format(question, answer)) 

# python code to demonstrate working of items() 

king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya', 
		'Modi' : 'The Changer'} 

# using items to print the dictionary key-value pair 
for key, value in king.items(): 
	print(key, value) 

# python code to demonstrate working of sorted() 

# initializing list 
lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 

# using sorted() to print the list in sorted order 
print ("The list in sorted order is : ") 
for i in sorted(lis) : 
	print (i,end=" ") 
	
print ("\r") 
	
# using sorted() and set() to print the list in sorted order 
# use of set() removes duplicates
print ("The list in sorted order (without duplicates) is : ") 
for i in sorted(set(lis)) : 
	print (i,end=" ") 
	
print("\r")	

# initializing list 
basket = ['guave', 'orange', 'apple', 'pear', 
		'guava', 'banana', 'grape'] 

# using sorted() and set() to print the list 
# in sorted order 
for fruit in sorted(set(basket)): 
	print(fruit) 

# python code to demonstrate working of reversed() 

# initializing list 
lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 


# using revered() to print the list in reversed order 
print ("The list in reversed order is : ") 
for i in reversed(lis) : 
	print (i,end=" ") 

print("\r")

# python code to demonstrate working of reversed() 

# using reversed() to print in reverse order 
for i in reversed(range(1, 10, 3)): 
	print (i) 

# Python 3.x code to demonstrate star pattern 

# Function to demonstrate printing pattern 
def pypart(n): 
	
	# outer loop to handle number of rows 
	# n in this case 
	for i in range(0, n): 
	
		# inner loop to handle number of columns 
		# values changing acc. to outer loop 
		for j in range(0, i+1): 
		
			# printing stars 
			print("* ",end="") 
	
		# ending line after each row 
		print("\r") 

# Driver Code 
n = 5
pypart(n) 
