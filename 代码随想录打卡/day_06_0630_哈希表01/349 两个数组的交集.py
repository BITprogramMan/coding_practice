from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited = set()
        for num in nums1:
            visited.add(num)
        res = []
        for num in nums2:
            if num in visited:
                res.append(num)
                visited.remove(num)
        return res