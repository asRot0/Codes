class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left , right = [], []
        count = 0

        for i in nums:
            if i < pivot: left.append(i)
            elif i > pivot: right.append(i)
            else: count += 1
        return left + [pivot]*count + right