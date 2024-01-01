
# solved

def count_pairs_within_bounds(p, lb, ub):
    p.sort()
    count = 0
    n = len(p)

    for i in range(n):
        left_bound = lb - p[i]
        print('leftbound', left_bound)
        right_bound = ub - p[i]
        print('rightbound', right_bound)

        left_index = bisect_left(p, left_bound, lo=i + 1)
        print('left_index',left_index)
        right_index = bisect_right(p, right_bound, lo=i + 1)
        print('right_index',right_index)

        count += right_index - left_index
        print(count)
        print('--------')

    return count

from bisect import bisect_left, bisect_right

t = int(input())
for case in range(1, t + 1):
    n = int(input())
    a, b = map(int, input().split())
    li = list(map(int, input().split()))

    result = count_pairs_within_bounds(li, a, b)
    print(f'Case {case}: {result}')
