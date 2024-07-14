''' Consider a question of finding the sum of N numbers inputted from the user.
    Input a number N.
    Input N numbers separated by a single space in a line.
Examples:
Input : 5

Output : 1 2 3 4 5
         15  '''
       




s=0
for i in range(int(input("INPUT:"))):
    print(i+1,end=" ")
    s+=i+1
print()    
print(s)    


#import the below module and see what happens 
import antigravity 
#NOTE - it wont work on online ide 
