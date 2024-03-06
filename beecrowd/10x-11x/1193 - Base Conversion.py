case = int(input())
li = []
for i in range(case):
    st = input()
    li.append(st)
for i in range(case):
    print('Case ' + str(i + 1) + ':')
    if ' bin' in li[i]:
        a = li[i].replace(' bin', '')
        a = int(a, 2)
        print(a, 'dec')
        print(hex(a)[2:], 'hex')
        print()
        continue
    if ' dec' in li[i]:
        a = li[i].replace(' dec', '')
        a = int(a)
        print(hex(a)[2:], 'hex')
        print(bin(a)[2:], 'bin')
        print()
        continue
    if ' hex' in li[i]:
        a = li[i].replace(' hex', '')
        a = int(a, 16)
        print(a, 'dec')
        print(bin(a)[2:], 'bin')
        print()
        continue