from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''先满足最容易满足的孩子'''
        s.sort()
        g.sort()
        start, end = 0, len(g)
        res = 0
        for i in range(len(s)):
            if start < end and s[i] >= g[start]:
                res += 1
                start += 1
        return res

    
if __name__ == '__main__':
    solution = Solution()
    res = solution.findContentChildren([1, 2, 3], [1, 1])
    print(res)

