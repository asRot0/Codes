pr = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
for _ in '7' * int(input()):
    input()
    r = "NO"
    x = y = 0
    for i in input():
        s, t = pr[i]
        x += s
        y += t
        if x == 1 and y == 1:r = "YES";break
    print(r)
