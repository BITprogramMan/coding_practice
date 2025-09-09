from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        help = {}
        for i in range(n):
            while stack and stack[-1] < nums2[i]:
                val = stack.pop()
                help[val] = nums2[i]
            stack.append(nums2[i])
        ans = []
        for val in nums1:
            ans.append(help.get(val, -1))
        return ans
