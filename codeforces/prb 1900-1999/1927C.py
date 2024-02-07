for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = set(i for i in map(int, input().split()) if i <= k)
    b = set(i for i in map(int, input().split()) if i <= k)

    print(['NO', 'YES'][len(a|b) == k and
          len(a) >= k//2 and len(b) >= k//2])