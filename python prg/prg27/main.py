# Formatting output using String method :
# Some of method which help in formatting a output are str.ljust(), str.rjust(), str.centre()

# Python program to 
# format a output using 
# string() method 

str = "I love helloworld"
	
# Printing the center aligned 
# string with fillchr 
print ("Center aligned string with fillchr: ") 
print (str.center(40, '#')) 

# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ") 
print (str.ljust(40, '-')) 

# Printing the right aligned string 
# with "_" padding 
print ("The right aligned string is : ") 
print (str.rjust(40, '_')) 
print("I love helloworld".rjust(40, '-'))
