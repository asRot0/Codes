for _ in range(int(input())):
    _, _, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    count = 0

    for i in b:
        for j in c:
            if i+j <= k: count += 1

    print(count)