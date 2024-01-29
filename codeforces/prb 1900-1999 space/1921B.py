for _ in range(int(input())):
    n = int(input())
    a, b = input(), input()
    c = d = 0
    for i in range(n):
        if a[i]=='0' and b[i]=='1':
            c+=1
        elif a[i]=='1' and b[i]=='0':
            d+=1
    print(max(c,d))


'''
for _ in range(int(input())):
    n = int(input())
    s = input()
    f = input()
    x, y = 0, 0
    for i in range(n):
        if s[i] == f[i]: continue
        if s[i] == '1': x += 1
        else: y += 1
    print(max(x, y))
'''

'''
for _ in range(int(input())):
    n, a, b = int(input()), input(), input(); c, d = abs(a.count('1') - b.count('1')), 0
    for i in range(n):
        if a[i] != b[i]: d += 1
    print((c + d) // 2)
'''

'''   
for _ in range(int(input())):
  n=int(input())
  s1,s2=input(),input()
  d1,d2=0,0
  ans=0
  for i in range(n):
    if s1[i]!=s2[i]:
      d1+=1
      if s2[i]=='1':d2+=1
  print(max(d2,d1-d2))
'''