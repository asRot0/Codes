for _ in range(int(input())):
    i = list(map(int, input().split()))
    print('YNEOS'[sum(i)%3!=0 or sum(i)//3 < max(i[:3])::2])