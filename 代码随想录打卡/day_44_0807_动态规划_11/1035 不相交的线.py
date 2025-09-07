from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        dp = [0] * (n2 + 1)
        for i in range(1, n1 + 1):
            diag = 0
            for j in range(1, n2 + 1):
                tmp = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = diag + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                diag = tmp
        return dp[-1]

        