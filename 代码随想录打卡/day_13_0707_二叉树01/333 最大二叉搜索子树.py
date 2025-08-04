from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def traval(root):
            if not root:
                return None
            v_min, v_max = root.val, root.val
            num_max_bst_node = 0
            is_bst = False
            left_res = traval(root.left)
            right_res = traval(root.right)
            if left_res:
                v_min = min(left_res[0], v_min)
                v_max = max(left_res[1], v_max)
                num_max_bst_node = left_res[-2]
            if right_res:
                v_min = min(right_res[0], v_min)
                v_max = max(right_res[1], v_max)
                num_max_bst_node = max(num_max_bst_node, right_res[-2])
            if (not left_res or left_res[-1]) and (not right_res or right_res[-1]) and (not left_res or left_res[1] < root.val) and(not right_res or right_res[0] > root.val):
                is_bst = True
                num_max_bst_node = (0 if not left_res else left_res[2]) + (0 if not right_res else right_res[2]) + 1
            return v_min, v_max, num_max_bst_node, is_bst
        res = traval(root)
        return 0 if not res else res[2]











    def largestBSTSubtreev1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traval(root):
            if not root:
                return None
            v_min, v_max = root.val, root.val
            num_max_bst_node = 0
            bst_head = None
            is_bst = False
            left_res = traval(root.left)
            right_res = traval(root.right)
            if left_res:
                v_min = min(left_res[0], v_min)
                v_max = max(left_res[1], v_max)
                num_max_bst_node = left_res[2]
                bst_head = left_res[3]
            if right_res:
                v_min = min(right_res[0], v_min)
                v_max = max(right_res[1], v_max)
                if right_res[2] > num_max_bst_node:
                    num_max_bst_node = right_res[2]
                    bst_head = right_res[3]
            if (not left_res or left_res[-1]) and (not right_res or right_res[-1]) and (not left_res or left_res[1] < root.val) and(not right_res or right_res[0] > root.val):
                is_bst = True
                num_max_bst_node = (0 if not left_res else left_res[2]) + (0 if not right_res else right_res[2]) + 1
                bst_head = root
            return v_min, v_max, num_max_bst_node, bst_head, is_bst
        res = traval(root)
        return None if not res else res[3]

