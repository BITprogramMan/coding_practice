class Solution:
    def BestArrange(self, nums):
        nums.sort(key = lambda x: x[1])
        count = 0
        start = 0
        for item in nums:
            if start <= item[0]:
                count += 1
                start = item[1]
        return count