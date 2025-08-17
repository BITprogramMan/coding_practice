from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        currSum = 0
        totalSum = 0
        start = 0
        for i in range(n):
            profit = gas[i] - cost[i]
            currSum += profit
            totalSum += profit
            if currSum < 0:
                start = i + 1
                currSum = 0
        if totalSum < 0:
            return -1
        return start    


    def canCompleteCircuitv1(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        minSum = float('inf')
        totalSum = 0
        start = 0
        for i in range(n):
            totalSum += gas[i] - cost[i]
            if totalSum < minSum:
                minSum = totalSum
                start = i + 1
        if totalSum < 0:
            return -1
        return start % n  

        
