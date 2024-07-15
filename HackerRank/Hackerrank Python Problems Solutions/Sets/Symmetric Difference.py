_, a = input(), set(input().split())
_, b = input(), set(input().split())

m = a.difference(b)
n = b.difference(a)
ans = m.union(n)

print('\n'.join(sorted(ans, key=int)))


'''
_, a = int(input()), set(map(int, input().split()))
_, b = int(input()), set(map(int, input().split()))

if not a.difference(b) == b.difference(a):
    li = a.difference(b)
    li.update(b.difference(a))

li = list(li)
li.sort()
print(*li, sep='\n')

'''
