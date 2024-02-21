def digit_sum(n):
    if n < 10:
        return n * (n + 1) // 2

    digits = len(str(n))
    power_of_10 = 10 ** (digits - 1)
    first_digit = n // power_of_10
    result = digit_sum(first_digit - 1) * power_of_10
    result += first_digit * (n % power_of_10 + 1)
    result += first_digit * digit_sum(power_of_10 - 1)
    result += digit_sum(n % power_of_10)

    return result


for _ in range(int(input())):
    n = int(input())
    print(digit_sum(n))

# another approach
'''
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


for _ in range(int(input())):
    n = int(input())
    total = 0
    for i in range(1, n+1):
        total += digit_sum(i)

    print(total)
'''

# time complexity of O(log n)
'''
def digit_sum(n):
    if n < 10:
        return n * (n + 1) // 2

    digits = len(str(n))
    power_of_10 = 10 ** (digits - 1)
    first_digit = n // power_of_10

    # Compute the sum of digits for numbers from 1 to (first_digit - 1)
    result = digit_sum(first_digit - 1) * power_of_10

    # Compute the sum of digits for numbers with the same number of digits
    # as n, but less than n
    result += first_digit * (n % power_of_10 + 1)

    # Recursively compute the sum of digits for numbers less than power_of_10
    result += first_digit * digit_sum(power_of_10 - 1)

    # Recursively compute the sum of digits for numbers with less digits
    result += digit_sum(n % power_of_10)

    return result


def sum_of_digit_sums(n):
    return digit_sum(n)


# Test cases
test_cases = [12, 1, 2, 3, 1434, 2024, 200000]
for n in test_cases:
    print(sum_of_digit_sums(n))

'''