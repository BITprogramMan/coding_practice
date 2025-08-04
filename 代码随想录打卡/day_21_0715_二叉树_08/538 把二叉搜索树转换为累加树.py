from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.acc_sum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.convertBST(root.right)
        root.val = root.val + self.acc_sum
        self.acc_sum = root.val
        self.convertBST(root.left)
        return root


    def convertBSTv1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = []
        curr = root
        acc_sum = 0
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                curr.val = curr.val + acc_sum
                acc_sum = curr.val
                curr = curr.left
        return root
    
    



