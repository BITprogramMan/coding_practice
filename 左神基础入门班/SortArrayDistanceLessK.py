class Solution:
    def sortedArrDistanceLessK(self, nums, k):
        import heapq
        res = []
        n = len(nums)
        for i in range(min(n, k)):
            heapq.heappush(res, nums[i])
        i += 1
        index = 0
        for j in range(i, n):
            heapq.heappush(res, nums[i])
            nums[index] = heapq.heappop(res)
            index += 1
        while res:
            nums[index] = heapq.heappop(res)
            index += 1

