from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        n = n // 2
        for key, value in m.items():
            if value > n:
                return key

        return 0


'''
nums = [2,2,1,1,1,2,2]
# Output: 2

print(max(set(nums), key=nums.count))
'''

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
'''
