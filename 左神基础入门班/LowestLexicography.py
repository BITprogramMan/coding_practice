from functools import cmp_to_key



class Solution:
    def LowestLexicography(self, nums):
        if not nums or len(nums) < 1:
            return ''
        nums.sort(key=cmp_to_key(lambda x, y: -1 if x + y < y + x else 1))
        return ''.join(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = ['ba', 'ab']
    res = solution.LowestLexicography(nums)
    print(res)










