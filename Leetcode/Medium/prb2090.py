from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        nums_len = len(nums)
        if nums_len < 2 * k + 1:
            return [-1] * nums_len

        li = [-1] * k
        v = sum(nums[:2 * k + 1])
        li.append(v // (2 * k + 1))

        for i in range(k + 1, nums_len - k):
            v = v + nums[i + k] - nums[i - k - 1]
            li.append(v // (2 * k + 1))
        return li + [-1] * k


'''
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n  # Initialize result array with -1
        window_sum = 0  # This will store the sum of the current window
    
        # Sum the first (2k+1) elements if possible
        for i in range(2 * k + 1):
            if i < n:
                window_sum += nums[i]
    
        # Slide the window across the array
        for i in range(k, n - k):
            result[i] = window_sum // (2 * k + 1)  # Calculate the average for the current window
            if i + k + 1 < n:
                window_sum += nums[i + k + 1]  # Add the next element in the window
            if i - k >= 0:
                window_sum -= nums[i - k]  # Remove the element that is left behind
    
        return result
'''