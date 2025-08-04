from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepthv0(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        def get_depth(root, depth):
            nonlocal result
            if depth > result:
                result = depth
            if root.left:
                get_depth(root.left, depth + 1)
            if root.right:
                get_depth(root.right, depth + 1)
        get_depth(root, 1)    
        return result

