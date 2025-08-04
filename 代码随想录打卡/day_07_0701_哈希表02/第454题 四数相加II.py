from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        sum_dict = {}
        for v1 in nums1:
            for v2 in nums2:
                sum_dict[v1 + v2] = sum_dict.get(v1 + v2, 0) + 1
        for v1 in nums3:
            for v2 in nums4:
                v = - (v1 + v2)
                res += sum_dict.get(v, 0)
        return res
