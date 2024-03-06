n = int(input())
for i in range(n):
    e = str(input())
    ti = ''
    for j in e:
        if j.isalpha():
            ti += chr(ord(j) + 3)
        else:
            ti += j
    ti = ti[::-1]
    m = int(len(ti) / 2)
    tf = ti[:m]
    for j in range(m, len(ti)):
        tf += chr(ord(ti[j]) - 1)
    print(tf)