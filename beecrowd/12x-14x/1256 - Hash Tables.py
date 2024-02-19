def link(li):
    conect = [str(a) for a in li]
    conect.append('\\')
    print(' -> '.join(conect))


for case in range(int(input())):
    if case:
        print()
    m, _ = map(int, input().split())
    dic = {}
    for i in range(m):
        dic[i] = [i]
    add = [int(i) for i in input().split()]
    for i in add:
        dic[i % m].append(i)
    for i in range(m):
        link(dic[i])
