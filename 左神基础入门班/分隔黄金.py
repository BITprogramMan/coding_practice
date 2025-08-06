import heapq
class Solution:
    def lessMoney(self, nums):
        queue = []
        for val in nums:
            heapq.heappush(queue, val)
        res = 0
        while len(queue) > 1:
            a = heapq.heappop(queue)
            b = heapq.heappop(queue)
            res += a + b
            heapq.heappush(queue, a + b)
        return res

