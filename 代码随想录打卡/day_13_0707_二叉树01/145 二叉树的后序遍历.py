from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversalv1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        if root.left:
            res.extend(self.postorderTraversal(root.left))
        if root.right:
            res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res
    

    def postorderTraversalv2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]

    def postorderTraversalv3(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        c = root
        while stack:
            root = stack[-1]
            if root.left and root.left != c and root.right != c:
                root = root.left
                stack.append(root)
            elif root.right and root.right != c:
                root = root.right
                stack.append(root)
            else:
                root = stack.pop()
                res.append(root.val)
                c = root
        return res

