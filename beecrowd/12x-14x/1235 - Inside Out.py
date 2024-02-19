n = int(input())
li = []
for i in range(n):
    c = input()
    m = int(len(c)/2)
    s1, s2 = c[:m], c[m:len(c)]
    s1, s2 = s1[::-1], s2[::-1]
    print(s1 + s2)