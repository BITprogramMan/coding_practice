from typing import List
import heapq
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])
        
        stack = list()
        dfs("JFK")
        return stack[::-1]

if __name__ == '__main__':
    solution = Solution()
    tickets = [["JFK","AAA"], ["AAA","JFK"], ["BBB","JFK"], ["JFK","BBB"],["JFK","NRT"]]
    res = solution.findItinerary(tickets)
    print(res)