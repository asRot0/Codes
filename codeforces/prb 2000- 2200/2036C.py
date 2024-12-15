for _ in range(int(input())):
    s=list(input())
    q=int(input())
    cnt=0
    for i in range(len(s)):
        if ''.join(s[i:i+4])=='1100':
            cnt+=1
    for _ in range(q):
        i,v=input().split()
        i=int(i)-1
        curr=''.join(s[max(0,i-3):i+4]).count('1100')
        s[i]=v
        conn=''.join(s[max(0,i-3):i+4]).count('1100')
        cnt+=conn-curr
        print('Yes' if cnt>0 else 'No')
