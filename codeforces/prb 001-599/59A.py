s = input()
print(s.lower() if 2*sum(i.islower() for i in s) >= len(s) else s.upper())