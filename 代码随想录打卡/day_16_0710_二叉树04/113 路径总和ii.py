from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def traval(root, curr_sum, targetSum, path):
            if not root.left and not root.right and curr_sum == targetSum:
                self.res.append(path[:])
                return 
            if root.left:
                path.append(root.left.val)
                traval(root.left, curr_sum + root.left.val, targetSum, path)
                path.pop()
            if root.right:
                path.append(root.right.val)
                traval(root.right, curr_sum + root.right.val, targetSum, path)
                path.pop()
        if not root:
            return []
        traval(root, root.val, targetSum, [root.val])
        return self.res
            
        