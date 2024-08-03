for _ in range(int(input())):
	n,k = map(int, input().split())
	arr = sorted(map(int, input().split()))
	res = 0
	for i in range(n):
		k += arr[i]
		x = k//(i+1)
		if x<arr[i]: break
		res = x
	print(res)

"""
t = int(input())
for _ in range(t):
	n, x = map(int, input().split())
	a = list(map(int, input().split()))
	low, high = 0, int(1e10)
	while low < high:
		mid = (low + high + 1) // 2
		val = sum(max(0, mid - i) for i in a)
		if val > x: high = mid - 1
		else: low = mid
	print(low)
"""