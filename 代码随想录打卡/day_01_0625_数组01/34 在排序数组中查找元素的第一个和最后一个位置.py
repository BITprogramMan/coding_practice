'''
这道题很经典，而且很久没做出来，中等难度，需要反复回顾
'''
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        ans = [-1, -1]
        n = len(nums) - 1
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] != target:
            return ans
        ans[0] = l
        r = n
        while l < r:
            mid = l + (r - l) // 2 + 1
            if nums[mid] > target:
                r = mid -1
            else:
                l = mid
        ans[1] = l
        return ans
    

    def searchRangev2(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target, l, r):
            res = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
                if nums[mid] == target:
                    res = mid
            return res
        def findLast(nums, target, l, r):
            res = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
                if nums[mid] == target:
                    res = mid
            return res
        n = len(nums) - 1 
        
        res = [findFirst(nums, target, 0, n), findLast(nums, target, 0, n)]
        return res
    
    def searchRangev3(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target, length):
            l, r = 0, length
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        n =len(nums)
        start = findFirst(nums, target, n)
        if start == n or nums[start] != target:
            return [-1, -1]
        else:
            return [start, findFirst(nums, target + 1, n) - 1]
        
    def searchRangev4(self, nums: List[int], target: int) -> List[int]:
        """
        剑指oofer，在排序数组中查找数字的解法
        """
        def findFirst(nums, target, l, r, length):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid -1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        r = mid - 1
            return -1

            
        def findLast(nums, target, l, r, length):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    if mid == length - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        l = mid + 1
            return -1

        res = [-1, -1]
        n = len(nums)
        res[0] = findFirst(nums, target, 0, n - 1, n)
        res[1] = findLast(nums, target, 0, n - 1, n)

        return res
                





if __name__ == '__main__':
    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    res = solution.searchRangev4(nums, target)
    print(res)




                
        
# if __name__ == '__main__':
#     solution = Solution()
#     nums=[5,7,7,8,8,10]
#     target = 8
#     res = solution.searchRange(nums, target)
#     print(res)















