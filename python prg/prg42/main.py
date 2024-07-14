# list of cities 
cities = ["Berlin", "Vienna", "Zurich"] 

# initialize the object 
ite = iter(cities)

while True:
    try:
        print(ite.__next__())

    except:
        break


# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    itr=iter(argv)
    while True:
        try:
            print(itr.__next__())
        except:
            break
myFun('hello', 'welcome', 'to', 'error')
