'''
for _ in range(int(input())):
    for _ in range(3):
        s = input()
        if '?' in s:
            mis = filter(lambda c: c not in s,'ABC')
            print(next(mis))
            break
'''

for _ in range(int(input())):
    s1, s2, s3 = input(), input(), input()
    if '?' in s1:
        mis = set('ABC') - set(s1)
        print(mis.pop())
    elif '?' in s2:
        mis = set('ABC') - set(s2)
        print(mis.pop())
    else:
        mis = set('ABC') - set(s3)
        print(mis.pop())