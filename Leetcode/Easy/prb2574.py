class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum, rightsum = 0, sum(nums)

        for i in range(len(nums)):
            leftsum += nums[i]
            nums[i], rightsum = abs(leftsum - rightsum), rightsum-nums[i]
        return nums