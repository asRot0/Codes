k, n, w = map(int, input().strip().split())
cost = (k*w*(w+1))//2
print(abs(n-cost) if cost>n else 0)