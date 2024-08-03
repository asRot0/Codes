def swap_sort_array(n, arr):
    sorted_arr = sorted(arr)
    for i in range(n):
        if sorted_arr[i] % 2 != arr[i] % 2:
            return "NO"
    return "YES"

# Input the number of test cases
t = int(input())

# Process each test case
results = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = swap_sort_array(n, arr)
    results.append(result)

# Output the results
for result in results:
    print(result)
