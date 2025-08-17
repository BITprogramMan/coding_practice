from typing import List 

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: abs(x), reverse=True)
        ans = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] < 0:
                if k > 0:
                    ans -= nums[i]
                    k -= 1
                else:
                    ans += nums[i]
            else:
                ans += nums[i]
        if k & 1 == 1:
            ans -= nums[-1]
        else:
            ans += nums[-1]
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 3, 2]
    res = solution.largestSumAfterKNegations([2,-3,-1,5,-4], k = 2)
    print(res)

