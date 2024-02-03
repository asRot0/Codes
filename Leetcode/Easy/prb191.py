class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


# return bin(n).count('1')
'''
Initialization: The count variable is initialized to 0. This variable will be used to keep track of the number of '1' bits.

While Loop: The while n: loop continues until n becomes 0. In each iteration of the loop, the following steps are performed:

a. Bitwise AND (n & 1): The bitwise AND operation is used to check the least significant bit of n. If the result is 1, it means that the least significant bit is set, so the count is incremented.

b. Right Shift (n >>= 1): The number n is right-shifted by 1 bit. This operation effectively removes the least significant bit of n.

Return Count: Once the loop completes (when n becomes 0), the final count is returned. The count represents the number of '1' bits in the binary representation of the original number.

The code uses bitwise operations to efficiently count the number of '1' bits by checking the least significant bit in each iteration and then right-shifting the number. This approach is concise and performs the task in a time complexity proportional to the number of bits in the binary representation of n.

'''