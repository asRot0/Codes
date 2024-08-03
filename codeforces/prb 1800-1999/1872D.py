import math

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    c = n // ((x*y)//math.gcd(x,y))  # common elements
    max_elements = n // x - c
    min_elements = n // y - c
    print(((n * max_elements) - (max_elements*(max_elements-1)//2)) - (min_elements*(min_elements+1)//2))

'''

    # Calculate the number of elements divisible by LCM(x, y)
    common_elements = n // lcm(x, y)

    # Calculate the maximum and minimum elements count
    max_elements = n // x
    min_elements = n // y

    # unique elements
    max_elements -= common_elements
    min_elements -= common_elements

    # Calculate the maximum and minimum sums
    max_sum = (n * max_elements) - (max_elements*(max_elements-1)//2)
    min_sum = (min_elements*(min_elements+1)//2)

# -------------

x = [2, 4, 6]
y = [3, 6]

common_elements = set(x) & set(y)
unique_x_length = len(x) - len(common_elements)
unique_y_length = len(y) - len(common_elements)

print(f'x={unique_x_length} and y={unique_y_length}')


# -----------

n = 7
x = 2
y = 3
result_generatorx = set((x + i * x for i in range(n // x)))
result_generatory = set((y + i * y for i in range(n//y)))
common_elements = len(result_generatorx & result_generatory)

# -----------

max_elements = len(result_generatorx) - common_elements
min_elements = len(result_generatory) - common_elements

# Calculate maximum and minimum sums using constant time complexity formulas
max_sum = (2 * n - max_elements + 1) * max_elements // 2

# Calculate min_sum by summing the smallest min_elements values from n
min_sum = min_elements * (min_elements + 1) // 2


# ----------

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    resx = set((x+i*x for i in range(n//x)))
    resy = set(y+i*y for i in range(n//y))
    common_elements = len(resx & resy)

    max_elements = len(resx) - common_elements
    min_elements = len(resy) - common_elements

    max_sum = (2 * n - max_elements + 1) * max_elements // 2
    min_sum = min_elements * (min_elements + 1) // 2
    print(max_sum-min_sum)

'''
