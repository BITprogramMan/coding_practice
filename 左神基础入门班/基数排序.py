class Solution:
    def RadixSort(self, nums):
        if len(nums) < 2:
            return 
        def max_bits(nums):
            max_val = max(nums)
            res = 0
            while max_val != 0:
                res += 1
                max_val = max_val // 10
            return res
        def getDigit(x, d):
            return (x // 10 ** (d - 1)) % 10
        
        def radix_sort(nums, begin, end, digit):
            radix = 10
            bucket = [0] * (end - begin + 1)
            for d in range(1, digit + 1):
                count = [0] * radix
                for i in range(begin, end + 1):
                    j = getDigit(nums[i], d)
                    count[j] += 1
                for i in range(1, radix):
                    count[i] += count[i - 1]
                for i in range(end, begin - 1, -1):
                    j = getDigit(nums[i], d)
                    bucket[count[j] - 1] = nums[i]
                    count[j] -= 1
                j = 0
                for i in range(begin, end + 1):
                    nums[i] = bucket[j]
                    j += 1

        radix_sort(nums, 0, len(nums) - 1, max_bits(nums))



if __name__ == '__main__':
    import random
    solution = Solution()
    for _ in range(100):
        nums1 = [random.randint(0,10000) for _ in range(20)]
        nums2 = nums1.copy()
        solution.RadixSort(nums1)
        nums2.sort()
        assert nums1 == nums2



