from math import log10
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n<1: return False
        p = log10(n)/log10(3)
        print(p)
        return p.is_integer()

get = Solution()
print(get.isPowerOfThree(27))

'''
avoiding the use of log10 and is_integer() which 
involve floating-point operations. Instead, you 
can use the fact that the maximum power of 3 that 
fits within the 32-bit signed integer range is
3^19, so you can directly check if 3^19 is 
divisible by n. Here's the optimized code

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0


- n > 0: Ensure that n is a positive integer.
- 1162261467 is the largest power of 3 that fits
  within the 32-bit signed integer range.
- 1162261467 % n == 0: Check if n is a divisor of 
  1162261467. If it is, then n is a power of 3.
'''