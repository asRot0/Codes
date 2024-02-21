for _ in range(int(input())):
    n = int(input())
    grid = [input() for _ in range(n)]
    prev_count = None
    for row in grid:
        curr_count = row.count('1')
        if curr_count==0:
            prev_count = None
            continue
        if curr_count and prev_count is not None:
            if curr_count == prev_count:
                print('SQUARE')
            else:
                print('TRIANGLE')
            break
        prev_count = curr_count