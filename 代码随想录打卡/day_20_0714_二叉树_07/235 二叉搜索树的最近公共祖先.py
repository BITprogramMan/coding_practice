class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val):
            return root
        elif root.val > p.val and root.val > q.val and root.left:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val and root.right:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
    def lowestCommonAncestorv1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
                