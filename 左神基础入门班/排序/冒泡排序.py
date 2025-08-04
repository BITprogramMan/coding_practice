class Solution:
    def select_sort(self, nums):
        if len(nums) < 2:
            return nums
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    def swap(self, nums, i, j):
        nums[i] = nums[i] 




if __name__ == '__main__':
    solution = Solution()
    from random import randint
    nums = [randint(0, 100) for _ in range(10)]
    print(nums)
    solution.select_sort(nums)
    print(nums)
