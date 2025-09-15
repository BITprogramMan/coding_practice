from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n != 0:
            return -1
        ans = 0
        avg = total // n
        curr_sum = 0
        for machine in machines:
            diff = machine - avg
            curr_sum += diff
            ans = max([ans, abs(curr_sum), diff])
        return ans
