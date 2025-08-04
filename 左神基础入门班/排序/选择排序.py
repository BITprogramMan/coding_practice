class Solution:
    def select_sort(self, nums):
        if len(nums) < 2:
            return nums
        for i in range(len(nums)):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == '__main__':
    solution = Solution()
    from random import randint
    nums = [randint(0, 100) for _ in range(10)]
    print(nums)
    solution.select_sort(nums)
    print(nums)
