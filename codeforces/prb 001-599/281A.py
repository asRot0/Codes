s = input()
print(chr(ord(s[0])-32)+s[1:] if ord(s[0])>91 else s)
