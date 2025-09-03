from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for booking in bookings:
            diff[booking[0] - 1] += booking[-1]
            if booking[1] < n:
                diff[booking[1]] -= booking[-1]
        res = [0] * n
        res[0] = diff[0]
        for i in range(1, n):
            res[i] = res[i - 1] + diff[i]
        return res