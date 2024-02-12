from typing import List
import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def soldiers_count(row):
            left, right = 0, len(row)
            while left < right:
                mid = left + (right - left) // 2
                if row[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left

        heap = [(soldiers_count(row), i) for i, row in enumerate(mat)]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
k = 3
get = Solution()
print(get.kWeakestRows(mat, k))


'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = [(sum(row), i) for i, row in enumerate(mat)]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
'''

'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = [(sol.count(1), i) for i, sol in enumerate(mat)]
        # print(heap)
        heapq.heapify(heap)
        # print(heap)

        li = []
        for i in range(k):
            _, ind = heapq.heappop(heap)
            li.append(ind)
        return li
'''