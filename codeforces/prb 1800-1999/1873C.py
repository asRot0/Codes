for _ in range(int(input())):
    point = 0
    for i in range(10):
        x = input()
        for j in range(10):
            if x[j] == 'X':
                point += min(i, j, 9-i, 9-j)+1
    print(point)