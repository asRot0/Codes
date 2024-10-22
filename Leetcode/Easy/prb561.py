class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in nums[::2]:
            res += i
        return res