class Solution:
    def process(self, nums, w):
        n = len(nums)
        if n < 1 or n < w:
            return None
        di_queue_max = []
        res = [0] * (n - w + 1)
        index = 0
        for i in range(n):
            while di_queue_max and nums[di_queue_max[-1]] <= nums[i]:
                di_queue_max.pop()
            di_queue_max.append(i)
            if di_queue_max[0] == i - w:
                di_queue_max.pop(0)
            if i >= w - 1:
                res[index] = nums[di_queue_max[0]]
                index += 1
        return res
         