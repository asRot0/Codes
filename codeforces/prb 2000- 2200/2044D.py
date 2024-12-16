for _ in range(int(input())):
    seen = {*range(1, int(input())+1)}
    res = []

    for i in map(int, input().split()):
        if i in seen:
            res.append(i)
            seen.discard(i)
        else: res.append(seen.pop())
    print(*res)