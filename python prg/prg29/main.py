# Printing Geeks in HEX 
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1) 
# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 

# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 

# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 
# Python3 program to demonstrate the 
# use of replace() method 

string = "geeks for geeks geeks geeks geeks"

# Prints the string by replacing geeks by Geeks 
print(string.replace("geeks", "Geeks")) 

# Prints the string by replacing only 3 occurrence of Geeks 
print(string.replace("geeks", "GeeksforGeeks", 3)) 
