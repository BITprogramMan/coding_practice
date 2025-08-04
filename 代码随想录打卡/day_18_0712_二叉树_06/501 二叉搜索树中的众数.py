from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        pre, count, max_count = None, 0, 0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val != pre:
                    if count > max_count:
                        res = [pre]
                        max_count = count
                    elif count == max_count and pre is not None:
                        res.append(pre)
                    count = 1
                else:
                    count += 1
                pre = root.val
                root = root.right
        if count == max_count:
            res.append(pre)
        elif count > max_count:
            res = [pre]
        return res

    def findModev1(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        pre, count, max_count = None, 0, 0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if pre is None or root.val != pre:
                    count = 1
                elif root.val == pre:
                    count += 1 
                if count > max_count:
                    res = [root.val]
                    max_count = count
                elif count == max_count:
                    res.append(root.val)
                pre = root.val
                root = root.right
        return res
