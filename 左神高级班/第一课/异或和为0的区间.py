class Solution:
    """
    给出n个数字 a_1,...,a_n，问最多有多少不重叠的非空区间，使得每个区间内数字的xor都等于0。
    """
    def process(self, nums):
        n = len(nums)
        map_dict = {0:-1}
        eor_pre_sum = 0
        dp = [0] * n
        for i in range(n):
            eor_pre_sum = eor_pre_sum ^ nums[i]
            if eor_pre_sum in map_dict:
                pre = map_dict[eor_pre_sum]
                dp[i] = 1 if pre == -1 else dp[pre] + 1
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])
            map_dict[eor_pre_sum] = i
            ans = max(ans, dp[i])
        return ans

