class Solution:
    """数轴上从左到右有n各点a[0], a[1], ……,a[n -1]，给定一根长度为L的绳子，求绳子最多能覆盖其中的几个点"""
    def max_covered_points(self, nums, k):
        if not nums:
            return 0
        l = 0
        max_count = 0
        n = len(nums)
        for r in range(n):
            # 移动左指针直到窗口满足条件
            while nums[r] - nums[l] > k:
                l += 1
            # 当前窗口大小
            current_count = r - l + 1
            # 更新最大值
            max_count = max(max_count, current_count)
        return max_count

if __name__ == '__main__':
    solution = Solution()
    res = solution.max_covered_points([1, 2, 3, 4, 5], 2)
    print(res)

