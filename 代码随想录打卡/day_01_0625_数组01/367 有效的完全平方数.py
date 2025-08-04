class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = l + (r - l) // 2
            v = mid * mid
            if v == num:
                return True
            elif v < num:
                l = mid + 1
            else:
                r = mid - 1

        return False





