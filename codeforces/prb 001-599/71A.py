for _ in range(int(input())):
    s = input()
    sl = len(s)
    print(s if sl<=10 else s[0]+str(sl-2)+s[-1])
