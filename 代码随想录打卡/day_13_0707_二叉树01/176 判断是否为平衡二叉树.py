from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traval(root):
            if not root:
                return 0, True
            l_height, l_balance = traval(root.left)
            r_height, r_balance = traval(root.right)
            height = max(l_height, r_height) + 1
            if not l_balance or not r_balance or abs(l_height - r_height) > 1:
                return height, False
            else:
                return height, True
        
        height, balance = traval(root)
        return balance




