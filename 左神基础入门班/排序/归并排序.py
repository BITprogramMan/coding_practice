class Solution:
    def mergeSortv1(self, nums):
        if len(nums) < 2:
            return nums
        def merge(nums, l ,mid, r):
            p1, p2 = l, mid + 1
            res = []
            while p1 <= mid and p2 <= r:
                if nums[p1] <= nums[p2]:
                    res.append(nums[p1])
                    p1 += 1
                else:
                    res.append(nums[p2])
                    p2 += 1
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
        merge_sort(nums, 0, len(nums) - 1)
        

    def mergeSort(self, nums):
        if len(nums) < 2:
            return nums
        def merge(nums1, nums2):
            res = []
            while nums1 and nums2:
                if nums1[0] <= nums2[0]:
                    res.append(nums1.pop(0))
                else:
                    res.append(nums2.pop(0))
            while nums1:
                res.append(nums1.pop(0))
            while nums2:
                res.append(nums2.pop(0))
            return res


        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return merge(left, right)



if __name__ == '__main__':
    solution = Solution()
    from random import randint 
    nums = [randint(0, 100) for _ in range(10)]
    print(nums)
    res = solution.mergeSort(nums)
    print(res)
