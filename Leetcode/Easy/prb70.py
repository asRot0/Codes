class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        fs, sd = 1, 2
        for _ in range(n-2):
            step = fs + sd
            fs, sd = sd, step
        return sd


get = Solution()
print(get.climbStairs(3))