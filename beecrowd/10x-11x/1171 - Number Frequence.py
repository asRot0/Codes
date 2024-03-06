n = int(input())
a = [int(input()) for i in range(n)]
b = list(set(a))
b.sort()
for i in b:
    print('{} aparece {} vez(es)'.format(i, a.count(i)))