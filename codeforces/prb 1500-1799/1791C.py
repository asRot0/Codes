for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    for i in range(n // 2):
        if s[i] == s[-i - 1]:
            c = n - 2 * i
            break
    print(c) if c else print(1) if n & 1 else print(0)


'''
for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    while i<n-i-1 and s[i]!=s[n-i-1]:i+=1
    print(n-2*i)
'''
'''
for _ in range(int(input())):
    _ = input()
    s = input()
    while len(s)>1 and s[0]!=s[-1]: s = s[1:-1]
    print(len(s))
'''