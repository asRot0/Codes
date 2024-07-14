# Python code to demonstrate the working of 
# exp() and log() 

# importing "math" for mathematical operations 
import math 

# returning the exp of 4 
print ("The e**4 value is : ", end="") 
print (math.exp(4)) 

# returning the log of 2,3 
print ("The value of log 2 with base 3 is : ", end="") 
print (math.log(2,3)) 
# Python code to demonstrate the working of 
# log2() and log10() 

# returning the log2 of 16 
print ("The value of log2 of 16 is : ", end="") 
print (math.log2(16)) 

# returning the log10 of 10000 
print ("The value of log10 of 10000 is : ", end="") 
print (math.log10(10000)) 
# Python code to demonstrate the working of 
# pow() and sqrt() 

# returning the value of 3**2 
print ("The value of 3 to the power 2 is : ", end="") 
print (math.pow(3,2)) 

# returning the square root of 25 
print ("The value of square root of 25 : ", end="") 
print (math.sqrt(25)) 
# Python code to demonstrate the working of 
# sin() and cos() 

a = math.pi/6

# returning the value of sine of pi/6 
print ("The value of sine of pi/6 is : ", end="") 
print (math.sin(a)) 

# returning the value of cosine of pi/6 
print ("The value of cosine of pi/6 is : ", end="") 
print (math.cos(a)) 
# Python code to demonstrate the working of 
# tan() and hypot() 

a = math.pi/6
b = 3
c = 4

# returning the value of tangent of pi/6 
print ("The value of tangent of pi/6 is : ", end="") 
print (math.tan(a)) 

# hypot(a, b) : This returns the hypotenuse of the values passed in arguments
# Numerically, it returns the value of sqrt(a*a + b*b)
# returning the value of hypotenuse of 3 and 4 
print ("The value of hypotenuse of 3 and 4 is : ", end="") 
print (math.hypot(b,c)) 
# Python code to demonstrate the working of 
# degrees() and radians() 

a = math.pi/6
b = 30

# returning the converted value from radians to degrees 
print ("The converted value from radians to degrees is : ", end="") 
print (math.degrees(a)) 

# returning the converted value from degrees to radians 
print ("The converted value from degrees to radians is : ", end="") 
print (math.radians(b)) 
# Python code to demonstrate the working of 
# ceil() and floor() 
# ceil() :This function returns the smallest integral value greater than the number. If number is already integer, same number is returned
# floor() :This function returns the greatest integral value smaller than the number. If number is already integer, same number is returned

a = 2.3

# returning the ceil of 2.3 
print ("The ceil of 2.3 is : ", end="") 
print (math.ceil(a)) 

# returning the floor of 2.3 
print ("The floor of 2.3 is : ", end="") 
print (math.floor(a)) 
# Python code to demonstrate the working of 
# fabs() and factorial() 
 
a = -10
b= 5

# returning the absolute value. 
print ("The absolute value of -10 is : ", end="") 
print (math.fabs(a)) 

# returning the factorial of 5 
print ("The factorial of 5 is : ", end="") 
print (math.factorial(b)) 
# Python code to demonstrate the working of 
# copysign() and gcd() 
# copysign(a, b) :- This function returns the number with the value of ‘a’ but with the sign of ‘b’. The returned value is float type
# gcd() :- This function is used to compute the greatest common divisor of 2 numbers mentioned in its arguments

a = -10
b = 5.5
c = 15
d = 5

# returning the copysigned value. 
print ("The copysigned value of -10 and 5.5 is : ", end="") 
print (math.copysign(b,a)) 

# returning the gcd of 15 and 5 
print ("The gcd of 5 and 15 is : ", end="") 
print (math.gcd(5,15)) 
# Python code to demonstrate the working of 
# gamma() 

a = 4

# returning the gamma() of 4 
print ("The gamma() of 4 is : ", end="") 
print (math.gamma(a)) 
# Python code to demonstrate the working of 
# const. pi and e 

# returning the value of const. pi 
print ("The value of const. pi is : ", end="") 
print (math.pi) 

# returning the value of const. e 
print ("The value of const. e is : ", end="") 
print (math.e) 
# Python code to demonstrate the working of 
# inf, nan, isinf(), isnan() 

# checking if number is nan 
if (math.isnan(math.nan)): 
	print ("The number is nan") 
else : print ("The number is not nan") 

# checking if number is positive infinity 
if (math.isinf(math.inf)): 
	print ("The number is positive infinity") 
else : print ("The number is not positive infinity") 
# Declaring a list 
L = [1, "a" , "string" , 1+2] 
print (L) 
L.append(6) 
print (L) 
L.pop() 
print (L) 
print (L[1]) 
# Declaring a tuple
tup = (1, "a", "string", 1+2) 
print (tup) 
print (tup[1]) 
# Declaring a iteration
i = 1
while (i < 10): 
	i += 1
	print (i,end=' ')
print()    
s = "Hello World"
for i in s : 
	print (i,end='') 
print()    
L = [1, 4, 5, 7, 8, 9] 
for i in L: 
	print (i,end='')
print()
for i in range(0, 10): 
	print (i,end='') 
print()