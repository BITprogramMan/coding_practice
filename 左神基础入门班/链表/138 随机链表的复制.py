from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomListv0(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hash_map = dict()
        curr = head
        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            hash_map[curr].next = hash_map[curr.next] if curr.next else None
            hash_map[curr].random = hash_map[curr.random] if curr.random else None
            curr = curr.next
        return hash_map[head]

        
    def copyRandomListv1(self, head: 'Optional[Node]') -> 'Optional[Node]':        
        if not head:
            return None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = Node(curr.val)
            curr.next.next = next_node
            curr = next_node
        curr = head
        while curr:
            next_node = curr.next.next
            copy_node = curr.next
            copy_node.random = curr.random.next if curr.random else None
            curr = next_node
        curr = head
        res = head.next
        while curr:
            copy_node = curr.next
            next_node = curr.next.next
            copy_node.next = next_node.next if next_node else None
            curr.next = next_node
            curr = curr.next
        return res

        

        

        




