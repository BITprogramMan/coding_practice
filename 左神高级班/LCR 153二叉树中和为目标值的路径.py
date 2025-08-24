from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathTarget(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        res = []
        def dfs(root, curr_sum, path):
            if not root.left and not root.right:
                if curr_sum + root.val == target:
                    path.append(root.val)
                    res.append(path[:])
                    path.pop()
                return
            if root.left:
                path.append(root.val)
                curr_sum += root.val
                dfs(root.left, curr_sum, path)
                curr_sum -= root.val
                path.pop()
            if root.right:
                path.append(root.val)
                curr_sum += root.val
                dfs(root.right, curr_sum, path)
                curr_sum -= root.val
                path.pop()
        if not root:
            return res
        dfs(root, 0, [])
        return res
    


if __name__ == '__main__':
    solution = Solution()
    node1= TreeNode(val=5)
    node2 = TreeNode(val=4)
    node3 = TreeNode(val=8)
    node4 = TreeNode(val=11)
    node5 = TreeNode(val=13)
    node6 = TreeNode(val=4)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node4.left = TreeNode(val=7)
    node4.right = TreeNode(val=2)
    node6.left = TreeNode(val=5)
    node6.right = TreeNode(val=1)

    res = solution.pathTarget(node1, 22)
    print(res)

