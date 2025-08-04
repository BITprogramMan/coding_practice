class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2
        while l <= r:
            mid = l + (r - l) // 2
            v = (mid + 1) * (mid + 1)
            if v == x:
                return mid + 1
            if v > x:
                if mid * mid <= x:
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1
            
    def bset_solution(x):
        l, r, ans = 0, x, -1
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid -1
        return ans            







