# [solved]

for case in range(1, int(input())+1):
    n = int(input())
    li = list(map(int, input().split()))
    beautiful_subarrays = 0
    consecutive = 1

    for i in range(1, n):
        if li[i] == li[i-1]:
            consecutive += 1
        else:
            beautiful_subarrays += consecutive * (consecutive + 1) // 2
            consecutive = 1
            # print(beautiful_subarrays)

    beautiful_subarrays += consecutive * (consecutive + 1) // 2
    # print(count)

    total_subarrays = (n *(n + 1)) // 2
    # beautiful_subarrays = count
    non_beautiful_subarrays = total_subarrays - beautiful_subarrays

    print(f'Case {case}: {non_beautiful_subarrays}')
    print('total_subarrays', total_subarrays)
    print('beautiful_subarrays',beautiful_subarrays)
    print('non_beautiful_subarrays', non_beautiful_subarrays)
