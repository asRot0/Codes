for _ in range(int(input())):
    _ = input()
    s = input()
    print(s.count('pie')+s.count('map')-s.count('mapie'))


'''
for _ in range(int(input())):
    n = int(input())
    s = input()
    i, count = 0, 0

    while i < n:
        if i+2 < n and s[i:i+3] == 'pie':
            count += 1
            i += 3

        elif i+2 < n and s[i:i+3] == 'map':
            count += 1
            i += 3

        else: i += 1
    print(count)
'''