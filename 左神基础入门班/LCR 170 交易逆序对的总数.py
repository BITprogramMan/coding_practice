from typing import List

class Solution:
    def reversePairs(self, record: List[int]) -> int:
        if len(record) < 2:
            return 0
        count = [0]
        def merge(nums, l, mid, r):
            p1, p2 = l, mid + 1
            res = []
            while p1 <= mid and p2 <= r:
                if nums[p1] > nums[p2]:
                    count[0] += (mid - p1 + 1)
                    res.append(nums[p2])
                    p2 += 1
                else:
                    res.append(nums[p1])
                    p1 += 1
            while p1 <= mid: 
                res.append(nums[p1])
                p1 += 1
            while p2 <= r:
                res.append(nums[p2])
                p2 += 1
            for i in range(len(res)):
                nums[l + i] = res[i]

        def merge_sort(nums, l, r):
            if l == r:
                return
            mid = l + (r - l) // 2
            merge_sort(nums, l, mid)
            merge_sort(nums, mid + 1, r)
            merge(nums, l, mid, r)
        merge_sort(record, 0, len(record) - 1)
        return count[0]


