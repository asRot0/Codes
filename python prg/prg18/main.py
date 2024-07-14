# taking two inputs at a time 

a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print() 
print(f"first num is {a} and second num is {b}")

name1 = 34
name2 = 46
name3 = 58
temp = "This is a {1} and he is a good boy named {0} gjif {2}".format(name1, name2, name3)
temp1 = f"this is a {name2} and he is a good boy {name1}"
print(temp)
print(temp1)