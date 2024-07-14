# prints Hello world 3 Times 
count = 0
while (count < 3):	 
	count = count+1
	print("Hello world") 


for i in range(1, 5): 
	for j in range(i): 
		print(j, end=' ') 
	print() 


# Prints all letters except 'e' and 's' 
for letter in 'geeksforgeeks': 
	if letter == 'e' or letter == 's': 
		continue
	print('Current Letter :',letter)	
	

 
# break the loop as soon it sees 'e' 
# or 's' 
for letter in 'geeksforgeeks': 
	if letter == 'e' or letter == 's': 
		break
print('Current Letter :',letter)  


# An empty loop 
for letter in 'geeksforgeeks': 
	pass
print('Last Letter :',letter) 