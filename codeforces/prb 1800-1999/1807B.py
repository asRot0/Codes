for _ in range(int(input())):
    input()
    a = map(int, input().split())
    sume, sumo = 0, 0
    for num in a:
        if num & 1: sumo+=num
        else: sume+=num
    print('YES' if sume>sumo else 'NO')