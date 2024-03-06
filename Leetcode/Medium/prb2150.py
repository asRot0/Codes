from typing import List
from collections import Counter


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []
        table = Counter(nums)
        for i in nums:
            if table[i] > 1 or table[i-1] or table[i+1]: continue
            else: res.append(i)
        return res