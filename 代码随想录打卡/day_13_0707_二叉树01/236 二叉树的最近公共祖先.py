
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traval(root, p, q):
            if not root:    
                return False, False, None
            l_contain_p, l_contain_q, l_common_parent = traval(root.left, p, q)
            r_contain_p, r_contain_q, r_common_parent = traval(root.right, p, q)
            contain_p, contain_q, common_parent = False, False, None
            if l_contain_p or r_contain_p or root == p:
                contain_p = True
            if l_contain_q or r_contain_q or root == q:
                contain_q = True
            if l_common_parent:
                common_parent = l_common_parent
            elif r_common_parent:
                common_parent = r_common_parent
            elif contain_p and contain_q:
                common_parent = root
            return contain_p, contain_q, common_parent
        return traval(root, p, q)[-1]

    
                       

    def lowestCommonAncestorv1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        hashMap = dict()
        def traval(root):
            if not root:
                return None
            if root.left:
                hashMap[root.left] = root
            if root.right:
                hashMap[root.right] = root
            traval(root.left)
            traval(root.right)
        hashMap[root] = None
        traval(root)
        p_parent_list = set()
        p_parent = p
        while p_parent:
            p_parent_list.add(p_parent)
            p_parent = hashMap[p_parent]
        node = q
        while node not in p_parent_list:
            node = hashMap[node]
        return node
        




