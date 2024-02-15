from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        check = {}
        for idx, num in enumerate(sorted(nums)):
            check.setdefault(num, idx)
        return [check[num] for num in nums]


get = Solution()
print(get.smallerNumbersThanCurrent([8,1,2,2,3]))