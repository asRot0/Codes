for s in[*open(0)][2::2]:print('NYOE S'[1<len(a:=s.split())<=sum(map(int,a))-a.count('1')::2])

# ----------

for _ in range(int(input())):
    n, c, s = int(input()), 0, 0
    a = map(int, input().split())
    for i in a:
        c+=i==1
        s+=i-1
    print('NYOE S'[n!=1 and c<=s::2])

# ----------

# Read the number of test cases
for _ in range(int(input())):
    # Read the length of the array, initialize counters
    n = int(input())
    count_ones = 0
    sum_minus_ones = 0

    # Read the array elements
    array_elements = map(int, input().split())

    # Count the number of ones and calculate the sum of (element - 1)
    for element in array_elements:
        count_ones += (element == 1)
        sum_minus_ones += (element - 1)

    # Determine if it's possible to form a good array
    is_good_array = 'YES' if n != 1 and count_ones <= sum_minus_ones else 'NO'

    # Print the result
    print(is_good_array)
