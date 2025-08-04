from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traval(root, val):
            if not root.left and not root.right and root.val == val:
                return True
            if root.left and traval(root.left, val - root.val):
                return True
            if root.right and traval(root.right, val - root.val):
                return True
            return False
        if not root:
            return False
        return traval(root, targetSum)
    
    def hasPathSumv1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack=[(root, root.val)]
        while stack:
            root, curr_sum = stack.pop()
            if not root.left and not root.right and curr_sum == targetSum:
                return True
            if root.left:
                stack.append((root.left, curr_sum + root.left.val))
            if root.right:
                stack.append((root.right, curr_sum + root.right.val))
        return False