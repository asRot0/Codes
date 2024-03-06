n = int(input())
while n :
    s = str(input())
    s1 = int(s[0])
    s2 = int(s[2])
    if s1 == s2: print(s1 * s2)
    elif s[1].isupper(): print(s2 - s1)
    else: print(s2 + s1)
    n-=1