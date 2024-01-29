for _ in range(int(input())):
    n = int(input())
    gl = ["a","e"]
    s = list(input())
    for i in range(2,n):
        if s[i] in gl:
            s[i-1]='.'+s[i-1]
    print(*s,sep='')

'''
for s in[*open(0)][2::2]:print(s[0]+''.join('.'*(y in'ae')+x
for x,y in zip(s[1:],s[2:])))
'''