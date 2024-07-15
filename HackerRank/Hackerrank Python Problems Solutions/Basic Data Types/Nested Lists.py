if __name__ == '__main__':
    a = [[input(), float(input())] for _ in range(int(input()))]
    s = sorted(set([i[1] for i in a]))
    for name in sorted(x[0] for x in a if x[1] == s[1]):
        print(name)
