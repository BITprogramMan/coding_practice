class Solution:
    """
    给定一个无序数组 arr，其中元素可正、可负、可 0，给定一个整数 k。求 arr 所
    有的子数组 中累加和小于或等于 k 的最长子数组长度。
    例如:arr=[3,-2,-4,0,6]，k=-2，相加和小于或等于-2 的最长子数组为{3,-2,-
    4,0}，所以结果返回4。
    """
    def process(self, nums, k):
        n = len(nums)
        min_sums = [0] * n 
        min_sum_tails = [0] * n 
        min_sums[-1] = nums[-1]
        min_sum_tails[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if min_sums[i + 1] <= 0:
                min_sums[i] = min_sums[i + 1] + nums[i]
                min_sum_tails[i] = min_sum_tails[i + 1]
            else:
                min_sums[i] = nums[i]
                min_sum_tails[i] = i
        end = 0
        sum_val = 0
        res = 0
        for i in range(n):
            while end < n and sum_val + min_sums[end] <= k:
                sum_val += min_sums[end]
                end = min_sum_tails[end] + 1
            res = max(res, end - i)
            if end > i:
                sum_val -= nums[i]
            else:
                end = i + 1
        return res

            