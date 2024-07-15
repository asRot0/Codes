if __name__ == '__main__':
    n = int(input())
    std = {}
    for _ in range(n):
        name, *mark = input().split()
        scr = list(map(float, mark))
        std[name] = scr
    quee_name = input()
    vlu = sum(std[quee_name]) / 3
    print('%.2f' % vlu)
