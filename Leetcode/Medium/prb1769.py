'''
boxes: '11010'
-> answer = [0]*len(boxes) -> [0,0,0,0,0]

boxes        1 1 0 1 0
left_sum     1 2 2 3 3
left_cumsum  1 3 5 8 11  --> answer [0,1,3,5,8]
right_sum    2 2 1 1 0
right_cumsum 6 4 2 1 0  --> answer [4,2,1,0,0]
answer [4,3,4,5,8]

'''


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)
        answer = [0]*l

        left_sum = 0
        left_cumsum = 0
        # the number of balls to the left of each box
        for i in range(l):
            answer[i] = left_cumsum
            left_sum += int(boxes[i])
            left_cumsum += left_sum

        right_sum = 0
        right_cumsum = 0
        # the number of balls to the right of each box
        for i in range(l-1, -1, -1):
            answer[i] += right_cumsum
            right_sum += int(boxes[i])
            right_cumsum += right_sum
        return answer


'''
For each index, the cost to move all boxes to it is sum of the cost leftCost to move all left boxes to it, and the cost
rightCost to move all right boxes to it.

    leftCost - for all indexes can be calculted using a single pass from left to right.
    rightCost - for all indexes can be calculted using a single pass from right to left.
    
    
    Example:
    boxes      11010
    leftCount  01223
    leftCost   01358
    rightCount 21100
    rightCost  42100
    ans        43458
    
    class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)
        for i in range(1, n):
            if boxes[i-1] == '1': leftCount += 1
            leftCost += leftCount # each step move to right, the cost increases by # of 1s on the left
            ans[i] = leftCost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1': rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
        return ans
'''


'''
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        res = 0
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j] == '1': res += abs(i-j)
            answer.append(res)
            res = 0
        return answer
'''