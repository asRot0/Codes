for _ in range(int(input())):
    s = input()
    if s[0]==s[-1]:
        print(s[0]+'='+s[-1])
    elif s[0] < s[-1]:
        print(s[0]+'<'+s[-1])
    else: print(s[0]+'>'+s[-1])