# Modules:
# ‘import’ keyword is used to import a particular module into your python code.

# Python program to illustrate 
# math module 
import math 

def Main(): 
	num = float(input("Enter a number: ")) 
	# fabs is used to get the absolute value of a decimal 
	num = math.fabs(num) 
	print(num) 
if __name__=="__main__": 
	Main() 
