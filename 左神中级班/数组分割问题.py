class Solution:
    """
    在数组中找到一个分割点，使得左部分最大值与右部分最大值的绝对差最大
    """
    def process(self, nums):
        if len(nums) < 2:
            return -1
        max_val = float('-inf')
        for val in nums:
            max_val = max(max_val, val)
        return max_val - min(nums[0], nums[-1])