from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        start = 0
        count = 0
        product = 1

        for end in range(len(nums)):
            product *= nums[end]

            while product >= k:
                product //= nums[start]
                start += 1

            count += end - start + 1
        return count


'''
To solve the problem of finding the number of contiguous subarrays where the product of all elements is strictly less than k, we can use the sliding window (or two-pointer) technique. This method is efficient and avoids the need for nested loops, which would be too slow for large arrays.

The key idea is to maintain a sliding window of subarrays that have a product less than k. We expand the window by including new elements and contract it when the product exceeds k.

Here's the step-by-step approach:

Initialize two pointers, start and end, to define the sliding window.
Use a variable product to keep track of the product of elements in the current window.
Iterate with the end pointer through the array:
Multiply the current element to the product.
While the product is greater than or equal to k, move the start pointer to the right and divide the product by the element at the start pointer.
The number of subarrays with the current end element that have a product less than k is end - start + 1. Add this count to the total.
This approach ensures that each element is processed at most twice, giving us a time complexity of O(n).

Here’s the implementation:

python
Copy code
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        product = 1
        start = 0
        count = 0
        
        for end in range(len(nums)):
            product *= nums[end]
            while product >= k:
                product //= nums[start]
                start += 1
            count += end - start + 1
        
        return count

# Example usage:
solution = Solution()
print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))  # Output: 8
print(solution.numSubarrayProductLessThanK([1, 2, 3], 0))  # Output: 0
Explanation:
Initialization:

product is initialized to 1, start is initialized to 0, and count is initialized to 0.
Sliding Window:

The end pointer iterates through each element of nums.
The current element is multiplied to product.
If product becomes greater than or equal to k, the window is contracted from the left by moving the start pointer to the right and dividing product by nums[start].
The number of valid subarrays ending at end is calculated as end - start + 1 and added to count.
Return Result:

The total count of valid subarrays is returned.
This solution is efficient with a time complexity of O(n) and a space complexity of O(1), making it suitable for large input sizes.
'''