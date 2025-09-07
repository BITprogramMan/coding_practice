from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def process(root):
            if not root:
                return 0, 0
            if not root.left and not root.right:
                return root.val, 0
            left_info = process(root.left)
            right_info = process(root.right)
            yes = root.val + left_info[1] + right_info[1]
            no = max(left_info[0], left_info[1]) + max(right_info[0], right_info[1])
            return yes, no
        yes, no = process(root)
        return max(yes, no)
                   
        