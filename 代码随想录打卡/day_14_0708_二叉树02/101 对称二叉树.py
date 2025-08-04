from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetricv0(self, root: Optional[TreeNode]) -> bool:
        def compare(l, r):
            if not l and not r:
                return True
            elif not l or not r:
                return False
            elif l.val != r.val:
                return False
            else:
                ans1 = compare(l.left, r.right)
                ans2 = compare(l.right, r.left)
                return ans1 and ans2
        if not root:
            return True
        return compare(root.left, root.right)
            
    def isSymmetricv1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        from collections import deque
        stack = deque([root.left, root.right])
        while stack:
            l, r = stack.popleft(), stack.popleft()
            if not l and not r:
                continue
            elif not l or not r:
                return False
            elif l.val != r.val:
                return False
            else:
                stack.append(l.left)
                stack.append(r.right)
                stack.append(l.right)
                stack.append(r.left)
        return True

    def isSymmetricv2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        from collections import deque
        stack = [root.right, root.left]
        while stack:
            l, r = stack.pop(), stack.pop()
            if not l and not r:
                continue
            elif not l or not r:
                return False
            elif l.val != r.val:
                return False
            else:
                stack.append(r.left)
                stack.append(l.right)
                stack.append(r.right)
                stack.append(l.left) 
        return True


