class Solution:
    """
    给定一个整数数组A，长度为n，有 1 <= A[i] <= n，且对于[1,n]的整数，其
    中部分整数会重复出现而部分不会出现。
    实现算法找到[1,n]中所有未出现在A中的整数。
    提示：尝试实现O(n)的时间复杂度和O(1)的空间复杂度（返回值不计入空间复
    杂度）。
    输入描述：
    一行数字，全部为整数，空格分隔
    A0 A1 A2 A3...
    输出描述：
    一行数字，全部为整数，空格分隔R0 R1 R2 R3...
    示例1:
    输入
    1 3 4 3
    输出
    2
    """
    def process(self, nums):
        def modify(val, nums):
            while nums[val - 1] != val:
                tmp = nums[val - 1]
                nums[val - 1] = val
                val = tmp
        if nums is None or len(nums) < 1:
            return []
        n = len(nums)
        res = []
        for i in range(n):
            modify(nums[i], nums)
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res



if __name__ == '__main__':
    solution = Solution()
    import random
    nums = [random.randint(1, 6) for _ in range(6)]
    print(nums)
    res = solution.process(nums)
    print(res)
