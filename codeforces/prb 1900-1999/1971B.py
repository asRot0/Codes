for _ in range(int(input())):
    s = input()
    if s == s[1:]+s[0]:
        print('no')
    else:
        print('yes')
        print(s[1:]+s[0])