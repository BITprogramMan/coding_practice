from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        if not root:
            return self.paths
        def traval(root, path):
            if not root.left and not root.right:
                self.paths.append(path)
            else:
                if root.left:
                    new_path = path + '->' + str(root.left.val)
                    traval(root.left, new_path)
                if root.right:
                    new_path = path + '->' + str(root.right.val)
                    traval(root.right, new_path)
        traval(root,str(root.val))
        return self.paths