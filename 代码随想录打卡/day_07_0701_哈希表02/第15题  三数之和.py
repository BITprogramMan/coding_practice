from typing import List

class Solution:
    def threeSumv1(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0 :
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            record = set()
            for j in range(i + 1, n):
                if j > i + 2 and nums[j] == nums[j - 1] and nums[j] == nums[j - 2]:
                    continue
                if - nums[i] - nums[j] in record:
                    res.append([nums[i], - nums[i] - nums[j], nums[j]])
                    record.remove(- nums[i] - nums[j])
                else:
                    record.add(nums[j])
        return res
    
    def threeSumv1(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()   
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0 :
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res




        