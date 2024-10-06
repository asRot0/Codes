'''
for _ in range(int(input())):
    n, k = map(int, input().split())
    c = 0
    even = 0
    for i in range(n, 0,-1):
        if c == k:
            break
        c += 1
        even += i*i
    print(['yes', 'no'][even & 1])


for _ in range(int(input())):
    n, k = map(int, input().split())
    even = 0
    for i in range(n-k+1, n+1):
        even += i*i
    print(['yes', 'no'][even & 1])
'''

for _ in range(int(input())):
    n, k = map(int, input().split())

    start = n - k + 1
    odds_in_range = (n + 1) // 2 - (start // 2)

    if odds_in_range % 2 == 0:
        print("YES")
    else:
        print("NO")

'''
Even vs. Odd Focus:

We only care whether the sum of the leaves is even or odd.
Adding even numbers does not affect the parity (evenness or oddness) of the result. What really matters is how many odd numbers contribute to the sum.
If the count of odd numbers in the last k years is even, the total sum will be even. If the count is odd, the sum will be odd.
Properties of Squares:

The square of an even number is always even.
The square of an odd number is always odd.
Therefore, the only way the sum will be odd is if the count of odd numbers in the range of years contributing to the sum is odd. Otherwise, the sum will be even.

Efficient Range Counting:

Rather than actually summing up the squares, we can simply count how many odd numbers are present in the range [n-k+1, n].
This is efficient because we can use arithmetic to count the odd numbers in a given range without iterating through each number.
Detailed Breakdown of the Solution:
Input:

Each test case gives us two numbers: n (the year for which we want to compute the number of leaves) and k (the number of years during which leaves last).
Key Step: Counting Odd Numbers:

The leaves grown in year i will last from year i to year i+k-1.
Therefore, the leaves contributing to year n are those grown from years n-k+1 to n.
Our goal is to count how many odd numbers are in this range [n-k+1, n] because only odd numbers affect the parity of the sum.
How to Count Odd Numbers Efficiently:

To count the odd numbers in a range, we don't need to iterate through the numbers. Instead, we can use a simple formula:
Count of odd numbers up to n: (n + 1) // 2
Count of odd numbers up to n - k: (n - k + 1) // 2
'''