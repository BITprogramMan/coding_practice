# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = []
        def pres(root):
            if not root:
                res.append(' ')
            else:
                res.append(str(root.val))
                pres(root.left)
                pres(root.right)
        pres(root)
        return '\n'.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        from collections import deque
        node_list = deque(data.split('\n'))
        def post(node_list):
            val = node_list.popleft()
            if not val.strip():
                return None
            root = TreeNode(int(val))
            root.left = post(node_list)
            root.right = post(node_list)
            return root
        return post(node_list)


    def serializev1(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            res.append(' ')
        else:
            res.append(str(root.val))
            from collections import deque
            queue = deque([root])
            while queue:
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                    res.append(str(root.left.val))
                else:
                    res.append(' ')
                if root.right:
                    queue.append(root.right)
                    res.append(str(root.right.val))
                else:
                    res.append(' ')
        return '\n'.join(res)
    

    def deserializev1(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        from collections import deque
        nodelist = deque(data.split('\n'))
        val = nodelist.popleft()
        if not val.strip():
            return None
        else:
            head = TreeNode(int(val))
            queue = deque([head])
            while nodelist:
                root = queue.popleft()
                val = nodelist.popleft()
                if not val.strip():
                    root.left = None
                else:
                    node = TreeNode(int(val))
                    root.left = node
                    queue.append(node)
                val = nodelist.popleft()
                if not val.strip():
                    root.right = None
                else:
                    node = TreeNode(int(val))
                    root.right = node
                    queue.append(node)
            return head

                

            



        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))