from typing import List

class Solution:
    def maxSlidingWindowv1(self, nums: List[int], k: int) -> List[int]:
        queue = []
        res = []
        for i in range(len(nums)):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            if i >= k -1:
                if queue[0] == nums[i - k + 1]:
                    res.append(queue.pop(0))
                else:
                    res.append(queue[0])
        return res


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque()
        res = []
        for i in range(len(nums)):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            if i >= k -1:
                if queue[0] == nums[i - k + 1]:
                    res.append(queue.popleft())
                else:
                    res.append(queue[0])
        return res



        