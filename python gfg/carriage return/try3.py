import time

countdown_num = 10
print('time count: ', end=' ')
for i in range(countdown_num, 0, -1):
    # print(i, end='\r')
    print('\x08' * 2, i, end='', flush=True)  # two places to take \x08 (backspace)
    time.sleep(1)
print('\x08' * 2, 'Blast off')
