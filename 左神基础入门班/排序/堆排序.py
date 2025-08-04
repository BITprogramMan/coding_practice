class Solution:
    def heapSort(self, nums):
        n = len(nums)
        if n < 2:
            return 
        # for i in range(n):
        #     self.heapInsert(nums, i)  # 时间复杂度是O(n*logn)
        for i in range(n-1, -1, -1):
            self.heapify(nums, i, n)    # 时间复杂度是O(n)
        n -= 1
        nums[0], nums[n] = nums[n], nums[0]
        while n > 0:
            self.heapify(nums, 0, n)
            n -= 1
            nums[0], nums[n] = nums[n], nums[0]

    def heapInsert(self, nums, index):
        while index > 0 and nums[index] > nums[(index - 1) // 2]:
            nums[index], nums[(index - 1) // 2] = nums[(index - 1) // 2], nums[index]
            index = (index - 1) // 2

    def heapify(self, nums, index, heapSize):
        left = index * 2 + 1
        while left < heapSize:
            largest = (left + 1) if left + 1 < heapSize and nums[left + 1] > nums[left] else left
            largest = largest if nums[largest] > nums[index] else index
            if largest == index:
                break
            nums[largest], nums[index] = nums[index], nums[largest] 
            index = largest
            left = index * 2 + 1 


if __name__ == '__main__':
    import random
    solution = Solution()
    nums = [48, 25, 29, 21, 31, 23, 14, 26, 28, 41]
    solution.heapSort(nums)
    print(nums)

    # for i in range(100):
    #     nums = [random.randint(0,50) for _ in range(10)]
    #     print(nums)
    #     nums1 = nums.copy()
    #     solution.heapSort(nums)
    #     print(nums)
    #     assert nums == nums1.sort()










