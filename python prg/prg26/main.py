# Formatting output using String modulo operator(%) :
# To this purpose, the modulo operator % is overloaded by the string class to perform string formatting


# The general syntax for a format placeholder is:  %[flags][width][.precision]type 


# Python program showing how to use 
# string modulo operator(%) to print 
# fancier output 

# print integer and float value 
print("Geeks : % 2d, Portal : % 7.2f" %(1, 05.333)) 

# print integer value 
print("Total students : % 3d, Boys : % 2d" %(240, 120)) 

# print octal value 
print("% 7.3o"% (25)) 

# print exponential value 
print("% 10.3E"% (356.08977)) 

# Python program to 
# show format () is 
# used in dictionary 

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678} 

# using format() in dictionary 
print('Geeks: {0[geeks]:d}; For: {0[for]:d};' 
	'Geeks: {0[geek]:d}'.format(tab)) 

data = dict(fun ="GeeksForGeeks", adj ="Portal") 

# using format() in dictionary 
print("I love {fun} computer {adj}".format(**data)) 
