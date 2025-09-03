class Difference:
    def __init__(self, nums):
        n = len(nums)
        self.diff_nums = [0] * n
        self.diff_nums[0] = nums[0]
        for i in range(1, n):
            self.diff_nums[i] = nums[i] - nums[i - 1]
        
    def increment(self, i, j, val):
        self.diff_nums[i] += val
        if j + 1 < len(self.diff_nums):
            self.diff_nums[j + 1] -= val

    def result(self):
        res = [0] * len(self.diff_nums)
        res[0] = self.diff_nums[0]
        for i in range(1, len(res)):
            res[i] = self.diff_nums[i] + res[i - 1]
        return res
            
    