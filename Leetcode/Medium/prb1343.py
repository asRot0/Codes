class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = sum(arr[:k])
        count = 0 if current_sum // k < threshold else 1

        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i-k]
            count += 0 if current_sum // k < threshold else 1
        return count