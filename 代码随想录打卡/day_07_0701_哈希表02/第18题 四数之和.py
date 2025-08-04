from typing import List

class Solution:
    def fourSumv1(self, nums: List[int], target: int) -> List[List[int]]:
        freq = {}
        n = len(nums)
        res = set()
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    value = target - nums[i] - nums[j] - nums[k]
                    if value in freq:
                        count = (nums[i] == value) + (nums[j] == value) + (nums[k] == value)
                        if freq[value] > count:
                            res.add(tuple(sorted([nums[i], nums[j], nums[k], value])))
        return list(res)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] > target and (target > 0 or nums[i] > 0) :
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                value = nums[i] + nums[j]
                if value > target and (target > 0 or value > 0):
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    tmp_value = nums[left] + nums[right]
                    if tmp_value == target - value:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    else:
                        if tmp_value < target - value:
                            left += 1
                        else:
                            right -= 1
        return res

                        
            
