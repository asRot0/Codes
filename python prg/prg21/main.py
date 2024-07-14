# basic method of input output 
# input N 
n = int(input()) 

# input the array 
arr = [int(x) for x in input().split()] 

# initialize variable 
summation = 0

# calculate sum 
for x in arr: 
	summation += x 
	
# print answer 
print(summation) 

# Python 3.x program showing 
# how to print data on 
# a screen 

# One object is passed 
print("GeeksForGeeks") 

x = 5
# Two objects are passed 
print("x =", x) 

# code for disabling the softspace feature 
print('G', 'F', 'G', sep ='') 

# using end argument 
print("Python", end = '@') 
print('g','f','g',sep='')
print("GeeksforGeeks") 
print('g','f','g',sep='_')
print('g','f','g')