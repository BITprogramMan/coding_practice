class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        def getLeftMost(root):
            while root.left:
                root = root.left
            return root
        if root.right:
            return getLeftMost(root.right)
        else:
            parent = root.parent
            while parent and parent.left != root:
                root = parent
                parent = root.parent
            return parent

        