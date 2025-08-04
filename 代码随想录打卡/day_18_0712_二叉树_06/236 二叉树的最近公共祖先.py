class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root, p, q):
            find_p, find_q, common_parent = False, False, None
            if not root:
                return find_p, find_q, common_parent
            left_info = find(root.left, p, q)
            right_info = find(root.right, p, q)
            find_p = left_info[0] or right_info[0] or root == p
            find_q = left_info[1] or right_info[1] or root == q
            if find_p and find_q and not left_info[2] and not right_info[2]:
                common_parent = root
            elif left_info[2]:
                common_parent = left_info[2]
            else:
                common_parent = right_info[2]
            return find_p, find_q, common_parent

        return find(root, p ,q)[2]




