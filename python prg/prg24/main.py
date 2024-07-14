# Convert base-10 decimal integers 
# to floating point numeric constants 
print ("This site is {0:f}% securely {1}!!". 
					format(100, "encrypted")) 

# To limit the precision 
print ("My average of this {0} was {1:.2f}%"
			.format("semester", 78.234876)) 

# For no decimal places 
print ("My average of this {0} was {1:.0f}%"
			.format("semester", 78.234876)) 

# Convert an integer to its binary or 
# with other different converted bases. 
print("The {0} of 100 is {1:b}"
		.format("binary", 100)) 
		
print("The {0} of 100 is {1:o}"
		.format("octal", 100)) 

print("The {0} of 200 is {1:x}"
        .format("hexadecimal", 200))


# To demonstrate spacing when 
# strings are passed as parameters 
print("{0:4}, is the computer science portal for {1:8}!"
						.format("GeeksforGeeks", "geeks")) 

# To demonstrate spacing when numeric 
# constants are passed as parameters. 
print("It is {0:5} degrees outside !"
						.format(40)) 

# To demonstrate both string and numeric 
# constants passed as parameters 
print("{0:4} was founded in {1:16}!"
	.format("GeeksforGeeks", 2009)) 


# To demonstrate aligning of spaces 
print("{0:^30} was founded in {1:<4}!"
		.format("GeeksforGeeks", 2009)) 

print("{:*^20s}".format("Geeks")) 
print("{0:/<20s}-----------{0:\>20s}".format("gfg"))


