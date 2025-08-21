class Solution:
    def process1(self, nums):
        n = len(nums)
        res = float('-inf')
        for i in range(n):
            for j in range(i, n):
                minnum = float('inf')
                currSum = 0
                for k in range(i, j + 1):
                    currSum += nums[i]
                    minnum = min(minnum, nums[i])
                res = max(res, currSum * minnum)
        return res
    
    def process2(self, nums):
        n = len(nums)
        stack = []
        res = float('-inf')
        acc_sum = [0] * n
        acc_sum[0] = nums[0]
        for i in range(1, n):
            acc_sum[i] = acc_sum[i - 1] + nums[i]
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                curr = stack.pop()
                res = max(res, nums[curr] * (acc_sum[i - 1] - 0 if not stack else acc_sum[stack[-1]]))
            stack.append(i)
        while stack:
            curr = stack.pop()
            res = max(res, nums[curr] * (acc_sum[n -1] - 0 if not stack else acc_sum[stack[-1]]))

        return res
                
