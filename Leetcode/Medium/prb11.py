class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, maxwater = 0, len(height)-1, 0

        while i<j:
            maxwater = max(maxwater, (j-i)*min(height[i], height[j]))
            i, j = (i + 1, j) if height[i] < height[j] else (i, j - 1)

        return maxwater