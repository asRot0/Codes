import time

for i in range(5, -1, -1):
    # Clear the console
    print('\033c', end='')

    # Print the countdown number at the same position
    print(i, end='', flush=True)

    # Wait for one second
    time.sleep(1)

# Print a new line at the end of the countdown
print()
'''The code uses the range() function to loop through the numbers from 5 to 0 (inclusive) in reverse order (-1 as the 
step). In each iteration, the console is cleared using the ANSI escape code \033c, which clears the screen. Then the 
current countdown number is printed at the same position using the end='' argument, which prevents the print() 
function from printing a new line at the end of the string. The flush=True argument ensures that the output is 
immediately printed to the console. Finally, the program waits for one second using the time.sleep() function before 
moving on to the next iteration. 

Note that this code may not work on all console environments, depending on the support for ANSI escape codes.
'''