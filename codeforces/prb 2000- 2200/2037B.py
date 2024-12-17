for _ in range(int(input())):
    k = int(input())
    seen = set()
    r = k-2

    for i in map(int, input().split()):
        if i<=r and not r%i:
            if r//i in seen:
                print(i, r//i)
                break
            seen.add(i)