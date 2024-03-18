class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l = len(nums)

        for i in range(l):
            nums[i] = nums[i] + l * (nums[nums[i]] % l)

        for i in range(l):
            nums[i] = nums[i] // l

        return nums