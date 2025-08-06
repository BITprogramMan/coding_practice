import heapq

class Solution:
    def findMaximizedCapital(self, k, m, profits, capital):
        nodes_by_cost = [(capital[i], - profits[i]) for i in range(len(profits))]
        minCostQueue = []
        maxProfitQueue = []
        for node in nodes_by_cost:
            heapq.heappush(minCostQueue, node)

        for _ in range(k):
            while minCostQueue and minCostQueue[0][0] <= m:
                capital, profit_ = heapq.heappop(minCostQueue)
                heapq.heappush(maxProfitQueue, (profit_, capital))
            if not maxProfitQueue:
                break
            m += (- heapq.heappop(maxProfitQueue)[0])
            
        return m    



