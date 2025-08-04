from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepthv0(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        if not root.left:
            return 1 + self.minDepth(root.right)
        else:
            return 1 + self.minDepth(root.left)
        

    def minDepthv1(self, root: Optional[TreeNode]) -> int:
        mindepth = float('inf')
        if not root:
            return 0
        def traval(root, depth):
            nonlocal mindepth
            if not root.left and not root.right:
                mindepth = min(mindepth, depth)
                return 
            if root.left:
                traval(root.left, depth + 1)
            if root.right:
                traval(root.right, depth + 1)
        traval(root, 1)
        return mindepth


    def minDepthv2(self, root: Optional[TreeNode]) -> int:
        depth = 0 
        if not root:
            return depth
        from collections import deque
        queue = deque([root])
        while queue:
            depth += 1
            for i in range(len(queue)):
                root = queue.popleft()
                if not root.left and not root.right:
                    return depth
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                




