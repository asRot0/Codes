n = int(input())
li = []
for i in range(0, n):
    li.append(int(input()))
for i in range(0, n):
    if li[i] == 0:
        print('NULL')
    elif li[i] < 0:
        if li[i] % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
    elif li[i] > 0:
        if li[i] % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')