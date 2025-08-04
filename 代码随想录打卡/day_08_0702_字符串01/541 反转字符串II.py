class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def swap(nums):
            n = len(nums)
            for i in range( n //2):
                nums[i], nums[n - 1 - i] = nums[n - 1 -i], nums[i]
            return nums
            
        n = len(s)
        nums = list(s)
        for start in range(0, n, 2 * k):
            nums[start:start + k] = swap(nums[start:start + k])
        return ''.join(nums)


            


if __name__ =='__main__':
    solution = Solution()
    s = 'abcdefg'
    res = solution.reverseStr(s, 2)
    print(res)

