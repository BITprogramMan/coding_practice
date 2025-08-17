from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 1
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= end:
                res += 1
                end = interval[1]
        return len(intervals) - res