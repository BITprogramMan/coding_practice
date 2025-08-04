from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNodev0(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr = root.right
                while curr and curr.left:
                    curr = curr.left
                curr.left = root.left
                return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def deleteOneNode(root):
            if not root:
                return None
            elif not root.right:
                return root.left
            else:
                curr = root.right
                while curr and curr.left:
                    curr = curr.left
                curr.left = root.left
                return root.right
            
        if not root:
            return None
        parent, curr = None, root
        while curr:
            if curr.val == key:
                break
            parent = curr
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right
        if not parent:
            return deleteOneNode(curr)
        elif parent.left and parent.left.val == key:
            parent.left = deleteOneNode(parent.left)
        elif parent.right and parent.right.val == key:
            parent.right = deleteOneNode(parent.right)
        return root
