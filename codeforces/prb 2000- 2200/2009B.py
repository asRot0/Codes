for _ in range(int(input())):
    arr = []
    for _ in range(int(input())):
        for i,c in enumerate(input()):
            if c == '#':
                arr.append(i+1)
                break

    print(*arr[::-1])
