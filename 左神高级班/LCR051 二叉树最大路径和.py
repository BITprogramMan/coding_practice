class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [float('-inf')]
        def dfs(root):
            res[0] = max(res[0], root.val)
            if not root.left and not root.right:
                return root.val
            left_val, right_val = -1, -1
            if root.left:
                left_val = dfs(root.left)
            if root.right:
                right_val = dfs(root.right)
            res[0] = max([res[0], left_val + root.val, right_val + root.val, left_val + right_val + root.val])
            return max([root.val, left_val + root.val, right_val + root.val])
        
        dfs(root)
        return res[0]

            

            


