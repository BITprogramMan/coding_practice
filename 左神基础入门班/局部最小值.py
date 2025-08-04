class Solution:
    def FindOneLessValueIndex(self, nums):
        if len(nums) < 2:
            return -1
        if nums[0] < nums[1]:
            return 0
        elif nums[-1] < nums[-2]:
            return len(nums) - 1
        else:
            l, r = 0, len(nums) - 2
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    return mid
                else:
                    if nums[mid] > nums[mid - 1]:
                        r = mid - 1
                    else:
                        l = mid + 1
            return l
                        
                    
