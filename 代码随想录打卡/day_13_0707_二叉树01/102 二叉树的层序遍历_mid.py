from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderv1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        result = []
        while queue:
            level = []
            for i in range(len(queue)):   # 实质是遍历完当前层的同时也可以遍历完下一层
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(level)
        return result

    def levelOrderv2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []

        def traval(root, level):
            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            if root.left:
                traval(root.left, level + 1)
            if root.right:
                traval(root.right, level + 1)
        traval(root, 0)
        return result
    
    def levelOrderv3(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        from collections import deque
        queue = deque([root])
        currend = root
        nextend = None
        currLayer = []
        while queue:
            root = queue.popleft()
            currLayer.append(root.val)
            if root.left:
                nextend = root.left
                queue.append(root.left)
            if root.right:  
                nextend = root.right
                queue.append(root.right)
            if root == currend:
                currend = nextend
                result.append(currLayer)
                currLayer = []
        return result
