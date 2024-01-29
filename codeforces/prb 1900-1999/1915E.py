def solve(t, test_cases):
    for i in range(t):
        n = test_cases[i][0]
        glasses = test_cases[i][1]

        prefix_sum = [0] * (n + 1)
        for j in range(n):
            prefix_sum[j + 1] = prefix_sum[j] + ((-1) ** (j + 1)) * glasses[j]

        counts = {}
        for j in range(n + 1):
            if prefix_sum[j] in counts:
                print("YES")
                break
            counts[prefix_sum[j]] = True
        else:
            print("NO")


t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    glasses = list(map(int, input().split()))
    test_cases.append((n, glasses))
solve(t, test_cases)

'''
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = set([0])
    s = 0
    for i in range(n):
        s+=-a[i] if i%2 else a[i]
        d.add(s)
    print('yes' if len(d) <= n else 'no')
'''

'''
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    sm=0
    seen=set()
    for i,n in enumerate(arr):
        if(i&1):
            n=-n
        sm+=n
        if(sm==0 or sm in seen):
            print("Yes")
            break
        seen.add(sm)
    else:
        print("No")
'''