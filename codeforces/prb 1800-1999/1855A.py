for _ in range(int(input())):
    _ = int(input())
    correct_positions = sum(1 for i, value in enumerate(list(map(int, input().split())), 1) if value == i)
    print((correct_positions+1) // 2)