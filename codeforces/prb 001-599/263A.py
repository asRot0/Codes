matrix = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_dist = abs(i - 2)
            col_dist = abs(j - 2)
            moves = row_dist + col_dist
            print(moves)
            break
