class MonotonousStack:
    def getNearLessNoRepeat(self, nums):
        n = len(nums)
        res = [[0] * 2 for _ in range(n)]
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                popIndex = stack.pop()
                leftLessIndex = -1 if not stack else stack[-1]
                res[popIndex][0] = leftLessIndex
                res[popIndex][1] = i
            stack.append(i)
        while stack:
            popIndex = stack.pop()
            leftLessIndex = -1 if not stack else stack[-1]
            res[popIndex][0] = leftLessIndex
            res[popIndex][1] = -1
        return res
                

