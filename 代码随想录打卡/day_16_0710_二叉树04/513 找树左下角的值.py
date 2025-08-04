from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        queue = deque([root])
        res = -1
        while queue:
            for i in range(len(queue)):
                root = queue.popleft()
                if i == 0:
                    res = root.val
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return res
    
    def findBottomLeftValuev1(self, root: Optional[TreeNode]) -> int:
        self.res = [0, -1]
        def traval(root, depth):
            if not root.left and not root.right:
                if depth > self.res[0]:
                    self.res = [depth, root.val]
            if root.left:
                traval(root.left, depth + 1)
            if root.right:
                traval(root.right, depth + 1)
        traval(root, 0)
        return self.res[1]





