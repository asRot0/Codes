class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = right = -1

        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i+j) >> 1
            if nums[mid] == target:
                left = mid
                j = mid - 1
            elif nums[mid] > target: j = mid - 1
            else: i = mid + 1
        if left == -1: return []

        i, j = left, len(nums)-1
        while i <= j:
            mid = (i+j) >> 1
            if nums[mid] == target:
                right = mid
                i = mid + 1
            elif nums[mid] > target: j = mid - 1
            else: i = mid + 1
        return range(left, right+1)