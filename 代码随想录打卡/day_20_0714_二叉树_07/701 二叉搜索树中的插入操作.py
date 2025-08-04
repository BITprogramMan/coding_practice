from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBSTv0(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traval(root, val):
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    traval(root.left, val)
            else:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    traval(root.right, val)
        if not root:
            return TreeNode(val)
        traval(root, val)
        return root
    
    def insertIntoBSTv1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while curr:
            parent = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root
    


    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
        
        