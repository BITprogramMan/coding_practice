from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * n2 for _ in range(n1)]
        ans = 0
        for i in range(n1):
            dp[i][0] = 1 if nums1[i] == nums2[0] else 0
            ans = max(ans, dp[i][0])
        for i in range(n2):
            dp[0][i] = 1 if nums1[0] == nums2[i] else 0
            ans = max(ans, dp[0][i])
        for i in range(1, n1):
            for j in range(1, n2):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans

    def findLengthv1(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n1, n2 = len(nums1), len(nums2)
        row, col = 0, n2 - 1
        while row < n1:
            i, j = row, col
            length = 0
            while i < n1 and j < n2:
                if nums1[i] == nums2[j]:
                    length += 1
                else:
                    length = 0
                ans = max(ans, length)
                i += 1
                j += 1
            if col > 0:
                col -= 1
            else:
                row += 1
        return ans

