n = int(input())
for _ in range(n):
    s = int(input())
    nam = input().split()
    cls = [k.replace('M', '') for k in input().split()]
    prs = []
    for nm, cl in zip(nam, cls):
        if cl.count('P')/len(cl) < 0.75:
            prs.append(nm)
    print(*prs)