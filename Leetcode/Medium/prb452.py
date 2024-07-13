class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows = 1
        target_end = points[0][1]

        for start, end in points:
            if start > target_end:
                arrows += 1
                target_end = end
        return arrows