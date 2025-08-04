from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def traval(root):
            if not root:
                return 0, True, True
            else:
                l_height, l_is_complete, l_is_full = traval(root.left)
                r_height, r_is_complete, r_is_full = traval(root.right)
                height = max(l_height, r_height) + 1
                if l_is_full and r_is_full and l_height == r_height:
                    return height, True, True
                if not l_is_complete or not r_is_complete:
                    return height, False, False
                else:
                    if l_height == r_height:
                        if l_is_full:
                            return height, True, False 
                        else:
                            return height, False, False 
                    elif l_height == r_height + 1 and r_is_full:
                        return height, True, False 
                    return height, False, False
        return traval(root)[1]

    def isCompleteTreev1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        from collections import deque
        queue = deque([root])
        first_miss_child_node = True
        while queue:
            root = queue.popleft()
            if root.right and not root.left:
                return False
            if not first_miss_child_node and (root.left or root.right):
                return False
            if not root.left or not root.right:
                first_miss_child_node = False
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return True           




