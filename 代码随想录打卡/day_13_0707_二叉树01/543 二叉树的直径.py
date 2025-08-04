from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traval(root):
            if not root:
                return 0, 0 
            else:
                l_height, l_max_dis = traval(root.left)
                r_height, r_max_dis = traval(root.right)
                height = max(l_height, r_height) + 1
                max_dis = max([l_max_dis, r_max_dis, l_height + r_height])
                return height, max_dis
        height, max_dis = traval(root)
        return max_dis

        