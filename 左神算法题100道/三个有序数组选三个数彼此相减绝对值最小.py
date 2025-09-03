from typing import List

class Solution:
    """
    三个有序数组，每个数组选出一个数字，分别为x1,x2,x3,怎么选择可以使 abs(x1 - x2) + abs(x2 - x3) + abd(x3 - x1)的取值最小

    思路： abs(x1 - x2) + abs(x2 - x3) + abd(x3 - x1) 实际上等于 2 * (max(x₁, x₂, x₃) - min(x₁, x₂, x₃))
    下面给出更通用的解法，不仅限于三个数组，而是k个数组，与力扣632题 最小区间是一个问题
    """
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # k = len(nums)
        # range_point = [(nums[i][0], i, 0) for i in range(k)]
        # range_point.sort()
        # res = [range_point[0][0], range_point[-1][0]]
        # while True:
        #     popitem = range_point.pop(0)
        #     if popitem[-1] == len(nums[popitem[-2]]):
        #         break
        import heapq
        k = len(nums)
        rangeLeft, rangeRight = -10**9, 10**9
        maxValue = max([vec[0] for vec in nums])
        priorityQueue = [(nums[i][0], i, 0) for i in range(k)]
        heapq.heapify(priorityQueue)
        while True:
            minValue, row, idx = heapq.heappop(priorityQueue)
            if maxValue - minValue < rangeRight - rangeLeft:
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1:
                break
            maxValue = max(maxValue, nums[row][idx + 1])
            heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))
        return [rangeLeft, rangeRight]
