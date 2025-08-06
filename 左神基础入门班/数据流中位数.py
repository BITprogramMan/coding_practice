import heapq
class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def modifyTwoHeapSize(self):
        if len(self.maxHeap) == len(self.minHeap) + 2:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.minHeap) == len(self.maxHeap) + 2:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def addNum(self, num):
        if len(self.maxHeap) == 0 or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        self.modifyTwoHeapSize()

    def getMedian(self):
        minHeapSize = len(self.minHeap)
        maxHeapSize = len(self.maxHeap)
        total_size = minHeapSize + maxHeapSize
        if total_size == 0:
            return None
        if total_size % 2 == 1:
            return -self.maxHeap[0] if maxHeapSize > minHeapSize else self.minHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        
if __name__ == '__main__':
    solution = Solution()
    import random
    nums = [67, 60, 68, 10, 64, 100, 54, 37, 65, 15]
    print(nums)
    res = []
    for num in nums:
        solution.addNum(num)
        res.append(solution.getMedian())
    print(res)
