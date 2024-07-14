print('_hello''\n''name','world')
print("first module's name{}".format(__name__))    

# Empty in if/else in Python 
mutex = True
if (mutex == True) : 
	pass
else : 
	print("False") 


class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 0
	
	# A member method that changes 
	# __hiddenVariable 
	def add(self, increment): 
		self.__hiddenVariable += increment 
		print (self.__hiddenVariable) 

# Driver code 
myObject = MyClass()	 
myObject.add(2) 
myObject.add(5) 

# This line causes error 
print (myObject._MyClass__hiddenVariable) 
