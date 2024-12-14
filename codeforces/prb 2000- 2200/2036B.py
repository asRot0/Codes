for _ in range(int(input())):
    n, k = map(int, input().split())
    li = [0]*k

    for _ in range(k):
        b, c = map(int, input().split())
        li[b-1] += c
    li.sort(reverse=True)
    print(sum(li[:min(n,k)]))