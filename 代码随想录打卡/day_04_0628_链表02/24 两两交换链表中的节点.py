from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairsv1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
               return head
        prev = head
        curr = head.next
        nextNode = head.next.next
        curr.next = prev
        prev.next = self.swapPairs(nextNode)
        return curr
          
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
               return head
        dumy_head = ListNode(next=head)
        curr = dumy_head
        while curr.next and curr.next.next:
            tmpNode = curr.next
            curr.next = tmpNode.next
            tmpNode.next = tmpNode.next.next
            curr.next.next = tmpNode
            curr = tmpNode
            
        return dumy_head.next
        