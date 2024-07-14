# Formatting output using String modulo operator(%) :
# Prints today's date with help 
# of datetime library 
import datetime 

today = datetime.datetime.today() 
print(f"{today:%m-%d-%Y}") 
print(f"{today:%B %d, %Y}")


newline = ord('\n') 

print(f"newline: {newline}")

# Demonstrate ValueError while 
# doing forced type-conversions 

# When explicitly converted floating point 
# values to decimal with base-10 by 'd' 
# type conversion we encounter Value-Error. 
print("The temperature today is {0:f} degrees outside !"
										.format(35.567)) 

# Instead write this to avoid value-errors 
print("The temperature today is {0:.0f} degrees outside !" 
										.format(35.567))
