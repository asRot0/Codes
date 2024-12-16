for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    unique = set(a)
    count = 0
    for i in unique:
        count += a.count(i)//2
    print(count)