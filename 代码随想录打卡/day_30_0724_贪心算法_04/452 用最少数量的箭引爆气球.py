from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res = 1
        end = points[0][1]
        for point in points[1:]:
            if point[0] > end:
                res += 1
                end = point[1]
        return res

