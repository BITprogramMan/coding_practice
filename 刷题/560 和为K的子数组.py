from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        hash_map = {0: 1}
        ans = 0
        for val in pre_sum[1:]:
            remain = val - k
            if remain in hash_map:
                ans += hash_map[remain]
            hash_map[val] = hash_map.get(val, 0) + 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1]
    res = solution.subarraySum(nums, 2)
    print(res)

            