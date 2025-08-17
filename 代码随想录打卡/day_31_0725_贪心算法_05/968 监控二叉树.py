from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return 2
            leftInfo = dfs(root.left)
            rightInfo = dfs(root.right)
            if leftInfo == 0 or rightInfo == 0:
                res[0] += 1
                return 1
            if leftInfo == 1 or rightInfo == 1:
                return 2
            if leftInfo == 2 and rightInfo ==2:
                return 0
        if dfs(root) == 0:
            res[0] += 1
        return sum(res)    


