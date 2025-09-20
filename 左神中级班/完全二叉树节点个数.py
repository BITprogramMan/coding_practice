class Solution:
    """
    求完全二叉树节点的个数
    """
    def process(self, head):
        if not head:
            return 0
        stack = [head]
        ans = 0
        while stack:
            head = stack.pop()
            ans += 1
            if head.right:
                stack.append(head.right)
            if head.left:
                stack.append(head.left)
        return ans
            
    def processv1(self, head):
        if not head:
            return 0
        stack = []
        ans = 0
        while stack or head:
            if head:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                ans += 1
                head = head.right
        return ans

    def processv2(self, head):
        def mostLeftLevel(node, level):
            while node:
                level += 1
                node = node.left
            return level - 1
        def numNodeOfCompleteTree(head, l, h):
            if l == h:
                return 1
            if mostLeftLevel(head.right, l + 1) == h:
                return (1 << (h - l)) + numNodeOfCompleteTree(head.right, l + 1, h)
            else:
                return (1 << (h - l - 1)) + numNodeOfCompleteTree(head.left, l+ 1, h)

        if not head:
            return 0
        return numNodeOfCompleteTree(head, 1, mostLeftLevel(head, 1))




