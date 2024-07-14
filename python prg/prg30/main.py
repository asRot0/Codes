# Python program to demonstrate 
# Addition of elements in a List 

# Creating a List 
List = [] 
print("Initial blank List: ") 
print(List) 

# append() and extend() methods can only add elements at the end
# Addition of Elements 
# in the List 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 

# Adding elements to the List 
# using Iterator 
for i in range(1, 4): 
	List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 

# Adding Tuples to the List 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 

# Addition of List to a List 
List2 = ['hello', 'world'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 
# Python program to demonstrate 
# Addition of elements in a List 

# Creating a List 
List = [1,2,3,4] 
print("Initial List: ") 
print(List) 

# Addition of Element at 
# specific Position 
# (using Insert Method) 
# insert() method requires two arguments(position, value)
List.insert(3, 12) 
List.insert(0, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List) 
# Python program to demonstrate 
# Addition of elements in a List 
	
# Creating a List 
List = [1,2,3,4] 
print("Initial List: ") 
print(List) 

# Addition of multiple elements 
# to the List at the end 
# (using Extend Method) 
List.extend([8, 'Geeks', 'Always']) 
print("\nList after performing Extend Operation: ") 
print(List) 
# Python program to demonstrate 
# accessing of element from list 

# Creating a List with 
# the use of multiple values 
List = ["Geeks", "For", "Geeks"] 

# accessing a element from the 
# list using index number 
print("Accessing a element from the list") 
print(List[0]) 
print(List[2]) 

# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List = [['Geeks', 'For'] , ['Geeks']] 

# accessing a element from the 
# Multi-Dimensional List using 
# index number 
print("Acessing a element from a Multi-Dimensional list") 
print(List[0][1]) 
print(List[1][0]) 
# Python program to demonstrate 
# Removal of elements in a List 

# Creating a List 
List = [1, 2, 3, 4, 5, 6, 
		7, 8, 9, 10, 11, 12, 'hello'] 
print("Intial List: ") 
print(List) 

# Removing elements from List 
# using Remove() method 
List.remove(5) 
List.remove(6) 
List.remove('hello')
print("\nList after Removal of two elements: ") 
print(List) 

# Removing elements from List 
# using iterator method 
for i in range(1, 5): 
	List.remove(i) 
print("\nList after Removing a range of elements: ") 
print(List) 

List = [1,2,3,4,5] 

# Removing element from the 
# Set using the pop() method 
# by default it removes only the last element of the set
List.pop() 
print("\nList after popping an element: ") 
print(List) 

# Removing element at a 
# specific location from the 
# Set using the pop() method 
List.pop(2) 
print("\nList after popping a specific element: ") 
print(List) 
# Python program to demonstrate 
# Removal of elements in a List 

# Creating a List 
List = ['G','E','E','K','S','F', 
		'O','R','G','E','E','K','S'] 
print("Intial List: ") 
print(List) 

# Print elements of a range 
# using Slice operation 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_List) 

# Print elements from a 
# pre-defined point to end 
Sliced_List = List[5:] 
print("\nElements sliced from 5th "
	"element till the end: ") 
print(Sliced_List) 

# Printing elements from 
# beginning till end 
Sliced_List = List[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_List) 
# Creating a List 
List = ['G','E','E','K','S','F', 
		'O','R','G','E','E','K','S'] 
print("Initial List: ") 
print(List) 

# Print elements from beginning 
# to a pre-defined point using Slice 
Sliced_List = List[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) 

# Print elements of a range 
# using negative index List slicing 
Sliced_List = List[-6:-1] 
print("\nElements sliced from index -6 to -1") 
print(Sliced_List) 

# Printing elements in reverse 
# using Slice operation 
Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List) 
# Python code to demonstrate the working of 
# del and pop() 

# initializing list 
lis = [2, 1, 3, 5, 4, 3, 8] 

# using del to delete elements from pos. 2 to 5 
# deletes 3,5,4 
del lis[2 : 5] 

# displaying list after deleting 

print ("List elements after deleting are : ",end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
	
print("\r") 

# using pop() to delete element at pos 2 
# deletes 3 
lis.pop(2) 

# displaying list after popping 
print ("List elements after popping are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
print("\n")	
# Python code to demonstrate the working of 
# insert() and remove() 

# initializing list 
lis = [2, 1, 3, 5, 3, 8] 

# using insert() to insert 4 at 3rd pos 
lis.insert(3, 4) 

# displaying list after inserting 
print("List elements after inserting 4 are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
	
print("\r") 

# using remove() to remove first occurrence of 3 
# removes 3 at pos 2 
lis.remove(3) 

# displaying list after removing 
print ("List elements after removing are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
print("\n")
# Python code to demonstrate the working of 
# sort() and reverse() 

# initializing list 
lis = [2, 1, 3, 5, 3, 8] 

# using sort() to sort the list 
lis.sort() 

# displaying list after sorting 
print ("List elements after sorting are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
	
print("\r") 

# using reverse() to reverse the list 
lis.reverse() 

# displaying list after reversing 
print ("List elements after reversing are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
print("\n")
# Python code to demonstrate the working of 
# extend() and clear() 

# initializing list 1 
lis1 = [2, 1, 3, 5] 

# initializing list 1 
lis2 = [6, 4, 3] 

# using extend() to add elements of lis2 in lis1 
lis1.extend(lis2) 

# displaying list after sorting 
print ("List elements after extending are : ", end="") 
for i in range(0, len(lis1)): 
	print(lis1[i], end=" ") 
	
print ("\r") 

# using clear() to delete all lis1 contents 
lis1.clear() 

# displaying list after clearing 
print ("List elements after clearing are : ", end="") 
for i in range(0, len(lis1)): 
	print(lis1[i], end=" ") 
print("\n")

#Creating an empty Tuple 
Tuple1 = () 
print("Initial empty Tuple: ") 
print (Tuple1) 

#Creatting a Tuple 
#with the use of string 
Tuple1 = ('Geeks', 'For') 
print("\nTuple with the use of String: ") 
print(Tuple1) 

# Creating a Tuple with 
# the use of list 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 

#Creating a Tuple 
#with the use of built-in function 
Tuple1 = tuple('helloworld')
print("\nTuple with the use of function:",end="") 
print(Tuple1)
print(tuple('hello')) 
  
#Creating a Tuple 
#with repetition 
Tuple1 = ('hello',) * 3
print("\nTuple with repetition: ") 
print(Tuple1) 
  
#Creating a Tuple  
#with the use of loop 
Tuple1 = ('hello') 
print("\nTuple with a loop") 
for i in range(0, len(Tuple1)): 
    Tuple1 = (Tuple1,) 
    print(Tuple1) 
#Accessing Tuple 
#with Indexing 
Tuple1 = tuple("Geeks") 
print("\nFirst element of Tuple: ") 
print(Tuple1[1]) 


#Tuple unpacking 
Tuple1 = ("Geeks", "For", "Geeks") 

#This line unpack 
#values of Tuple1 
a, b, c = Tuple1 
print("\nValues after unpacking: ") 
print(a) 
print(b) 
print(c) 
# Python program to demonstrate 
# Creation of Set in Python 

# Creating a Set 
set1 = set() 
print("Intial blank Set: ") 
print(set1) 

# Creating a Set with 
# the use of a String 
set1 = set("GeeksForGeeks") 
print("\nSet with the use of String: ") 
print(set1) 

# Creating a Set with 
# the use of Constructor 
# (Using object to Store String) 
String = 'GeeksForGeeks'
set1 = set(String) 
print("\nSet with the use of an Object: " ) 
print(set1) 
print(set('hello'))

# Creating a Set with 
# the use of a List 
set1 = set(['Geeks', 'For', 'Geeks', 'hello', 'world']) 
print("\nSet with the use of List: ") 
print(set1) 
print(set('helloworld'))
# Python program to demonstrate 
# Addition of elements in a Set 

# Creating a Set 
set1 = set() 
print("Intial blank Set: ") 
print(set1) 

# Adding element and tuple to the Set 
set1.add(8) 
set1.add(9) 
set1.add((6,7)) 
print("\nSet after Addition of Three elements: ") 
print(set1) 

# Adding elements to the Set 
# using Iterator 
for i in range(1, 6): 
	set1.add(i) 
print("\nSet after Addition of elements from 1-5: ") 
print(set1) 
# Python program to demonstrate 
# Addition of elements in a Set 

# Addition of elements to the Set 
# using Update function 
set1 = set([ 4, 5, (6, 7)]) 
set1.update([10, 11]) 
print("\nSet after Addition of elements using Update: ") 
print(set1) 
# Python program to demonstrate 
# Accessing of elements in a set 

# Creating a set 
set1 = set(["Geeks", "For", "Geeks"]) 
print("\nInitial set") 
print(set1) 

# Accessing element using 
# for loop 
print("\nElements of set: ") 
for i in set1: 
	print(i, end=" ") 
print('\r')
# Checking the element 
# using in keyword 
print("Geeks" in set1) 
# Python program to demonstrate 
# Deletion of elements in a Set 

# Creating a Set 
set1 = set([1, 2, 3, 4, 5, 6, 
			7, 8, 9, 10, 11, 12]) 
print("Intial Set: ") 
print(set1) 

# Removing elements from Set 
# using Remove() method 
set1.remove(5) 
set1.remove(6) 
print("\nSet after Removal of two elements: ") 
print(set1) 

# Removing elements from Set 
# using Discard() method 
set1.discard(8) 
set1.discard(9) 
print("\nSet after Discarding two elements: ") 
print(set1) 

# Removing elements from Set 
# using iterator method 
for i in range(1, 5): 
	set1.remove(i) 
print("\nSet after Removing a range of elements: ") 
print(set1) 
# Python program to demonstrate 
# Deletion of elements in a Set 

# Creating a Set 
set1 = set([1, 2, 3, 4, 5, 6, 
			7, 8, 9, 10, 11, 12]) 
print("Intial Set: ") 
print(set1) 

# Removing element from the 
# Set using the pop() method 
set1.pop() 
print("\nSet after popping an element: ") 
print(set1) 
#Creating a set 
set1 = set([1,2,3,4,5]) 
print("\n Initial set: ") 
print(set1) 


# Removing all the elements from 
# Set using clear() method 
set1.clear() 
print("\nSet after clearing all the elements: ") 
print(set1) 
# Python program to demonstrate 
# working of a FrozenSet 

# Creating a Set 
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r') 

Fset1 = frozenset(String) 
print("The FrozenSet is: ") 
print(Fset1) 

# To print Empty Frozen Set 
# No parameter is passed 
print("\nEmpty FrozenSet:",end=" ") 
print(frozenset()) 
# Creating a Dictionary 
# with Integer Keys 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 

# Creating a Dictionary 
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
# Creating a Nested Dictionary 
# as shown in the below image 
Dict = {1: 'Geeks', 2: 'For', 
		3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 

print(Dict) 
# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Adding set of values 
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 

# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 
# Python program to demonstrate 
# accessing a element from a Dictionary 

# Creating a Dictionary 
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 

# accessing a element using key 
print("Accessing a element using key:") 
print(Dict['name']) 

# accessing a element using key 
print("Accessing a element using key:") 
print(Dict[1]) 
# accessing a element using get() 
# method 
print("Accessing a element using get:") 
print(Dict.get(3)) 
# Creating a Dictionary 
Dict = {'Dict1': {1: 'Geeks'}, 
		'Dict2': {'Name': 'For'}} 

# Accessing element using key 
print(Dict['Dict1']) 
print(Dict['Dict1'][1]) 
print(Dict['Dict2']['Name']) 
# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
		'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
		'B' : {1 : 'Geeks', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 

# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 

# Deleting a Key from 
# Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 
# Creating a Dictionary 
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 

# Deleting a key 
# using pop() method 
pop_ele = Dict.pop(1) 
print('\nDictionary after deletion: ' + str(Dict)) 
print('Value associated to poped key is: ' + str(pop_ele)) 
# Creating Dictionary 
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 

# Deleting an arbitrary key 
# using popitem() function 
pop_ele = Dict.popitem() 
print("\nDictionary after deletion: " + str(Dict)) 
print("The arbitrary pair returned is: " + str(pop_ele)) 
# Creating a Dictionary 
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 

# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict) 

# Python code to demonstrate the working of 
# array(), append(), insert() 

# importing "array" for array operations 
import array 

# initializing array with array values 
# initializes array with signed integers 
arr = array.array('i', [1, 2, 3]) 

# printing original array 
print ("The new created array is : ",end=" ") 
for i in range (0, 3): 
	print (arr[i], end=" ") 

print("\r") 

# using append() to insert new value at end 
arr.append(4); 

# printing appended array 
print("The appended array is : ", end="") 
for i in range (0, 4): 
	print (arr[i], end=" ") 
	
# using insert() to insert value at specific position 
# inserts 5 at 2nd position 
arr.insert(2, 5) 

print("\r") 

# printing array after insertion 
print ("The array after insertion is : ", end="") 
for i in range (0, 5): 
	print (arr[i], end=" ") 

print("\r")

# Python code to demonstrate the working of 
# pop() and remove() 

# initializing array with array values 
# initializes array with signed integers 
arr= array.array('i',[1, 2, 3, 1, 5]) 

# printing original array 
print ("The new created array is : ",end="") 
for i in range (0,5): 
	print (arr[i],end=" ") 

print ("\r") 

# using pop() to remove element at 2nd position 
print ("The popped element is : ",end="") 
print (arr.pop(2)); 

# printing array after popping 
print ("The array after popping is : ",end="") 
for i in range (0,4): 
	print (arr[i],end=" ") 

print("\r") 

# using remove() to remove 1st occurrence of 1 
arr.remove(1) 

# printing array after removing 
print ("The array after removing is : ",end="") 
for i in range (0,3): 
	print (arr[i],end=" ") 

print("\r")

# Python code to demonstrate the working of 
# index() and reverse() 

# initializing array with array values 
# initializes array with signed integers 
arr= array.array('i',[1, 2, 3, 1, 2, 5]) 

# printing original array 
print ("The new created array is : ",end="") 
for i in range (0,6): 
	print (arr[i],end=" ") 

print ("\r") 

# using index() to print index of 1st occurrenece of 2 
print ("The index of 1st occurrence of 2 is : ",end="") 
print (arr.index(2)) 

#using reverse() to reverse the array 
arr.reverse() 

# printing array after reversing 
print ("The array after reversing is : ",end="") 
for i in range (0,6): 
	print (arr[i],end=" ") 

print("\r")

# Python code to demonstrate the working of 
# typecode, itemsize, buffer_info() 

# initializing array with array values 
# initializes array with signed integers 
arr= array.array('i',[1, 2, 3, 1, 2, 5]) 

# using typecode to print datatype of array 
print ("The datatype of array is : ",end="") 
print (arr.typecode) 

# using itemsize to print itemsize of array 
print ("The itemsize of array is : ",end="") 
print (arr.itemsize) 

# using buffer_info() to print buffer info. of array 
# address in which array is stored and number of elements
print ("The buffer info. of array is : ",end="") 
print (arr.buffer_info()) 

# Python code to demonstrate the working of 
# count() and extend() 

# initializing array 1 with array values 
# initializes array with signed integers 
arr1 = array.array('i',[1, 2, 3, 1, 2, 5]) 

# initializing array 2 with array values 
# initializes array with signed integers 
arr2 = array.array('i',[1, 2, 3]) 

# using count() to count occurrences of 1 in array 
print ("The occurrences of 1 in array is : " + str(arr1.count(1))) 

# using extend() to add array 2 elements to array 1 
arr1.extend(arr2) 

print ("The modified array is : ",end="") 
for i in range (0,9): 
	print (arr1[i],end=" ") 

print("\r")

# Python code to demonstrate the working of 
# fromlist() and tolist() 

# initializing array with array values 
# initializes array with signed integers 
arr = array.array('i',[1, 2, 3, 1, 2, 5]) 

# initializing list 
li = [1, 2, 3] 

# using fromlist() to append list at end of array 
arr.fromlist(li) 

# printing the modified array 
print ("The modified array is : ",end="") 
for i in range (0,9): 
	print (arr[i],end=" ") 

# using tolist() to convert array into list 
li2 = arr.tolist() 

print ("\r") 

# printing the new list 
print ("The new list created is : ",end="") 
for i in range (0,len(li2)): 
	print (li2[i],end=" ") 

