from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [-1] * n, [-1] * n
        maxLeft[0] = height[0]
        maxRight[-1] = height[-1]
        for i in range(1, n):
            maxLeft[i] = (max(height[i], maxLeft[i - 1]))
        for i in range(n - 2, -1, -1):
            maxRight[i] = (max(height[i], maxRight[i + 1]))
        res = 0
        for i in range(1, n - 1):
            res += (max(0, min(maxLeft[i], maxRight[i]) - height[i]))
        return res
    
    def trapv1(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        left_max, right_max = height[0], height[-1]
        l, r = 1, n - 2
        while l <= r:
            if left_max == right_max:
                res += max(0, left_max - height[l])
                res += max(0, right_max - height[r]) if l != r else 0
                left_max = max(left_max, height[l])
                right_max = max(right_max, height[r])
                l += 1
                r -= 1
            elif left_max < right_max:
                res += max(0, left_max - height[l])
                left_max = max(left_max, height[l])
                l += 1
                
            else:
                res += max(0, right_max - height[r])
                right_max = max(right_max, height[r])
                r -= 1
        return res








if __name__ == '__main__':
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = solution.trapv1(height)
    print(res)
