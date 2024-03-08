from typing import List
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        table = Counter(tuple(i) for i in grid)
        count = 0
        n = len(grid)

        # grid[:] = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

        # for i in grid:
        #     count += table.get(str(i), 0)

        for i in range(n):
            count += table.get(tuple(grid[j][i] for j in range(n)), 0)

        return count


'''
    n = len(grid)
    row_count = Counter(tuple(row) for row in grid)
    col_count = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))

    count = 0
    for row in row_count:
        count += row_count[row] * col_count[row]

    return count
'''