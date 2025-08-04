from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        tmp_depth = 0
        left, right = root.left, root.right
        while left and right:
            tmp_depth += 1
            left = left.left
            right = right.right
        if not left and not right:
            return (2 << tmp_depth) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)