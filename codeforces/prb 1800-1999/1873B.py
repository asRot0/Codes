from math import prod
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a[:] = sorted(a)
    a[0] += 1
    print(prod(a))



"""
# Define a list of numbers
numbers = [5, 2, 9, 1, 8]

# Find the minimum value in the list
min_value = min(numbers)

# Find the index of the minimum value
min_index = numbers.index(min_value)

# Add one to the minimum value
new_value = min_value + 1

# Update the list with the new value
numbers[min_index] = new_value

# Print the updated list
print("Updated list:", numbers)
"""