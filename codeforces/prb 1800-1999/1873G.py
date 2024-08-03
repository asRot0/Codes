for _ in range(int(input())):
    s = input()
    print(s.count('A') - min(map(len, s.split('B'))))