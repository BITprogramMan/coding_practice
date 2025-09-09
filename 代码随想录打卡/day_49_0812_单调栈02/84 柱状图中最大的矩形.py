from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        stack = []
        for i in range(n):
            while stack and heights[stack[-1][0]] > heights[i]:
                popitem = stack.pop()
                if stack:
                    width = i - stack[-1][-1] - 1
                else:
                    width = i
                ans = max(ans, heights[popitem[0]] * width)
            if not stack or heights[stack[-1][0]] != heights[i]:
                stack.append([i])
            else:
                stack[-1].append(i)
        while stack:
            popitem = stack.pop()
            if stack:
                width = n - stack[-1][-1] - 1
            else:
                width = n
            ans = max(ans, heights[popitem[0]] * width)
        return ans
    
if __name__ == '__main__':
    solution = Solution()
    res = solution.largestRectangleArea([5, 4, 1, 2])
    print(res)



        