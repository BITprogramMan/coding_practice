from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow



        
if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    res = solution.removeElement(nums, 3)
    print(res)
