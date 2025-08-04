from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        from collections import deque
        queue = deque([(root, 'r')])
        while queue:
            for i in range(len(queue)):
                root, flag = queue.popleft()
                if flag == 'l' and not root.left and not root.right:
                    res += root.val
                if root.left:
                    queue.append((root.left, 'l'))
                if root.right:
                    queue.append((root.right, 'r'))
        return res
