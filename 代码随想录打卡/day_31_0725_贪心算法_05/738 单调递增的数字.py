from typing import List

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = list(str(n))
        length = len(nums)
        for i in range(len(nums) - 1, 0 , -1):
            if nums[i - 1] > nums[i]:
                nums[i - 1]  = str(int(nums[i - 1]) - 1)
                nums[i:] = '9' * (length - i)
        return int(''.join(nums))


if __name__ == '__main__':
    solution = Solution()
    for n in [332, 10, 1234,]:
        res = solution.monotoneIncreasingDigits(n)
        print(res)