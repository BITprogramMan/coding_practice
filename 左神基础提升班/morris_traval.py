class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def morris_traval_pre(self, root):
        if not root:
            return []
        curr = root
        mostRight = None
        res = []
        while curr:
            if curr.left:
                mostRight = curr.left
                while mostRight.right and mostRight.right!= curr:
                    mostRight = mostRight.right
                if not mostRight.right:
                    mostRight.right = curr
                    res.append(curr.val)
                    curr = curr.left
                    continue
                else:
                    mostRight.right = None
            else:
                res.append(curr.val)
            curr = curr.right
        return res


    def morris_traval_mid(self, root):
        if not root:
            return []
        curr = root
        mostRight = None
        res = []
        while curr:
            if curr.left:
                mostRight = curr.left
                while mostRight.right and mostRight.right!= curr:
                    mostRight = mostRight.right
                if not mostRight.right:
                    mostRight.right = curr
                    curr = curr.left
                    continue
                else:
                    mostRight.right = None
            res.append(curr.val)
            curr = curr.right
        return res

    def morris_traval_after(self, root):
        def reverseEdge(head):
            prev, nextNode = None, None
            while head:
                nextNode = head.right
                head.right = prev
                prev = head
                head = nextNode
            return prev
        def printEdge(head):
            tail = reverseEdge(head)
            curr = tail
            res = []
            while curr:
                res.append(curr.val)
                curr = curr.right
            reverseEdge(tail)
            return res
        if not root:
            return []
        curr = root
        mostRight = None
        res = []
        while curr:
            if curr.left:
                mostRight = curr.left
                while mostRight.right and mostRight.right!= curr:
                    mostRight = mostRight.right
                if not mostRight.right:
                    mostRight.right = curr
                    curr = curr.left
                    continue
                else:
                    mostRight.right = None
                    res.extend(printEdge(curr.left))
            curr = curr.right
        res.extend(printEdge(root))
        return res





if __name__ == '__main__':
    node1 = Node(val=1)
    node2 = Node(val=2)
    node3 = Node(val=3)
    node1.right = node2
    node2.left=node3
    solution = Solution()
    res = solution.morris_traval_after(node1)
    print(res)
