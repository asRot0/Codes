for _ in range(int(input())):
    n = int(input())
    tc = min(n-2, 26)
    n -= tc
    sc = min(n-1, 26)
    n -= sc
    fc = min(n, 26)
    print(chr(ord('a') + fc - 1) + chr(ord('a') + sc - 1) + chr(ord('a') + tc - 1))
