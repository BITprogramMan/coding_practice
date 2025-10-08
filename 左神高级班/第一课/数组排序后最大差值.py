class Solution:
    """
    给定一个数组，求如果排序之后，相邻两数的最大差值。要求时间复杂度O(N)，且要
    求不能用非基于比较的排序。
    """
    def process(self, nums):
        n = len(nums)
        if nums is None or len(nums) < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        bucket_min_nums, bucket_max_nums, bucket_flag_nums = [None] * (n + 1), [None] * (n + 1), [False] * (n + 1)
        # n + 1个桶，保证至少有一个空桶，这样的话相邻两数最大差值必然不可能在同一个桶中，这里n + 1个桶创造了一个潜在的平凡解，但不一定是最终的解
        for i in range(n):
            bucket_id = round((nums[i] - min_val) / (max_val - min_val) * n, 0)
            bucket_min_nums[bucket_id] = min(nums[i], bucket_min_nums[bucket_id]) if bucket_flag_nums[bucket_id] else nums[i]
            bucket_max_nums[bucket_id] = max(nums[i], bucket_max_nums[bucket_id]) if bucket_flag_nums[bucket_id] else nums[i]
            bucket_flag_nums[bucket_id] = True
        res = 0
        lastMax = bucket_max_nums[0]
        for i in range(1, n + 1):
            if bucket_flag_nums[i]:
                res = max(bucket_min_nums[i] - lastMax, res)
                lastMax = bucket_max_nums[i]
        return res

