import time

countdown_num = 10

for i in range(countdown_num, 0, -1):
    print(i, end='\r')
    time.sleep(1)
print('Blast off')
