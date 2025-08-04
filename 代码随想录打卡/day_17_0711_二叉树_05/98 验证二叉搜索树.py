from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.max_val = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:    
        if not root:
            return True
        is_left_bst = self.isValidBST(root.left)
        if not is_left_bst:
            return False
        if self.max_val < root.val:
            self.max_val = root.val
        else:
            return False
        return self.isValidBST(root.right)

    def isValidBSTv1(self, root: Optional[TreeNode]) -> bool:    
        if not root:
            return True
        stack = []
        pre_val = float('-inf')
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val <= pre_val:
                    return False
                else:
                    pre_val = root.val
                root = root.right
        return True



    def isValidBSTv2(self, root: Optional[TreeNode]) -> bool:    
        def traval(root):
            is_bst, min_val, max_val = True, root.val, root.val
            if not root.left and not root.right:
                return is_bst, min_val, max_val
           
            if root.left:
                left_info = traval(root.left)
                is_bst = is_bst and left_info[0] and root.val > left_info[2]
                min_val = min(left_info[1], min_val)
                max_val = max(left_info[2], max_val)
            if root.right:
                right_info = traval(root.right)
                is_bst = is_bst and right_info[0] and root.val < right_info[1]
                min_val = min(right_info[1],  min_val)
                max_val = max(right_info[2], max_val)
            return is_bst, min_val, max_val

        if not root:
            return True
        return traval(root)[0]