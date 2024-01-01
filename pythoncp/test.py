for case in range(1, int(input())+1):
    n = int(input())
    a, b = map(int, input().split())
    li = list(map(int, input().split()))

    count = 0
    for i in range(n):
        for x in range(i+1, n):
            if a<= li[i] + li[x] <=b:
                count+=1
    print(f'Case {case}: {count}')