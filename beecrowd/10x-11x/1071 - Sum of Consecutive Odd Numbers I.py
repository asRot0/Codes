a = int(input())
b = int(input())
if a>b:
    a,b=b,a
l = []
for i in range(a, b):
    l.append(i)
if len(l):
    l.pop(0)
    print(sum([a for a in l if a % 2 != 0]))
else:
    print('0')