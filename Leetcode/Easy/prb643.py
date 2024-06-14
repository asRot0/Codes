from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = v = sum(nums[:k])

        for i in range(len(nums) - k):
            v = v - nums[i] + nums[i + k]
            max_sum = max(max_sum, v)

        return max_sum / k


nums = [4,2,1,3,3]
k = 2

get = Solution()
print(get.findMaxAverage(nums, k))