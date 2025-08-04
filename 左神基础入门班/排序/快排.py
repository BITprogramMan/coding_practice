class Solution:

    def partitionv1(self, nums, l, r):
        index = r - 1
        while l <= index:
            if nums[l] <= nums[r]:
                l += 1
            else:
                nums[l], nums[index] = nums[index], nums[l]
                index -= 1
        nums[index + 1], nums[r] = nums[r], nums[index + 1]


    def partitionv2(self, nums, l, r):
        index = r - 1
        while l <= index:
            if nums[l] <= nums[r]:
                l += 1
            else:
                nums[l], nums[index] = nums[index], nums[l]
                index -= 1
        nums[index + 1], nums[r] = nums[r], nums[index + 1]


    def partitionv3(self, nums, l, r):
        index = r
        while l < index:
            if nums[l] <= nums[r]:
                l += 1
            else:
                index -= 1
                nums[l], nums[index] = nums[index], nums[l]
        nums[index], nums[r] = nums[r], nums[index]


    
    def quickSort(nums):
        import random
        if len(nums) < 2:
            return nums
        
        def partition(nums, l, r):
            less, more = l - 1, r
            while l < more:
                if nums[l] < nums[r]:
                    less += 1
                    nums[less], nums[l] = nums[l] ,nums[less]
                    l += 1
                elif nums[l] > nums[r]:
                    more -= 1
                    nums[l], nums[more] = nums[more], nums[l]
                else:
                    l += 1
                nums[more], nums[r] = nums[r], nums[more]
                return less + 1, more

        
        def quick_sort(nums, l, r):
            
            if l < r:
                random_point = l + int((r - l + 1) * random.random())
                nums[r], nums[random_point] = nums[random_point], nums[r]
                p = partition(nums, l, r)
                quick_sort(nums, l, p[0] - 1)
                quick_sort(nums, p[1] + 1, r)

        quick_sort(nums, 0, len(nums) - 1)



if __name__ == '__main__':
    solution = Solution()
    import random
    for i in range(100):
        nums1 = [random.randint(0, 10) for _ in range(15)]
        nums2 = nums1.copy()
        # print(nums1, nums2, sep='\t')
        solution.partitionv1(nums1, 0, len(nums1) - 1)
        solution.partitionv3(nums2, 0, len(nums2) - 1)
        try:
            assert nums1 == nums2
        except:
            print(nums1, nums2, '---',sep='\t')





