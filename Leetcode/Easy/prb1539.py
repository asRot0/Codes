class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r =0, len(arr)
        while l< r:
            mid = (l+r)//2
            missing = arr[mid] - (mid + 1)

            if missing < k: l = mid + 1
            else: r = mid
        return l + k


'''
Initialize two pointers, left and right, to keep track of the search range. Initially, set left to 0 and right to 
the last element of the array. While left is less than right, calculate the midpoint of the range as (left + right) 
// 2. Count the number of missing positive integers between arr[0] and the midpoint. You can do this by subtracting 
the value of arr[mid] from its index mid + 1. This gives you the count of positive integers missing before arr[mid]. 
If the count of missing positive integers is less than or equal to k, then update left to mid + 1, indicating that 
you need to search in the right half of the array. Otherwise, update right to mid, indicating that you need to search 
in the left half of the array. Continue this process until left is equal to right. At the end of the loop, 
left will be pointing to the kth missing positive integer.
'''