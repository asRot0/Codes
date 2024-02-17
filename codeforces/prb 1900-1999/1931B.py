for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    total_water, same_water = 0, 0
    avg_water = sum(a) // n

    for i in a:
        total_water += i
        same_water += avg_water
        if total_water < same_water:
            print('NO')
            break
    else:
        print('YES')



'''
for _ in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))

    avg_water = sum(a) // n
    temp_water = 0

    for i in a:
        if temp_water < 0:
            print('NO')
            break
        if i != avg_water:
            temp_water = temp_water + i - avg_water
    else:
        print('YES')
'''