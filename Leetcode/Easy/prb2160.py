class Solution:
    def minimumSum(self, num: int) -> int:
        digit = []
        while num > 0:
            digit.append(num%10)
            num //= 10
        digit.sort()

        return digit[0]*10 + digit[-1] + digit[1]*10 +digit[-2]