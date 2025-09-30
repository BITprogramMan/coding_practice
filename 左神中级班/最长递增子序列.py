class Solution:
    def process(self, nums):
        def binary_search(target, nums, l, r):
            res = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        n = len(nums)
        ends = [None] * n
        ends[0] = nums[0]
        res = 1
        for i in range(1, n):
            tmp = binary_search(nums[i], ends, 0, res - 1)
            if tmp == -1:
                ends[0] = nums[i]
            else:
                ends[tmp + 1] = nums[i]
            res = max(tmp + 2, res)
        return res


if __name__ == '__main__':
    import random
    solution = Solution()
    nums = [random.randint(0,10) for _ in range(5)]
    nums = [8, 7, 1, 3, 4]
    res = solution.process(nums)
    print(nums)
    print(res)









