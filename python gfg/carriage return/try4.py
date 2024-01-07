import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print('\x08' * 5 + timeformat, end='', flush=True)
        # print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print("\nThat's the end! You lose...\n\n\n\n\n")
    exit()

countdown(10)