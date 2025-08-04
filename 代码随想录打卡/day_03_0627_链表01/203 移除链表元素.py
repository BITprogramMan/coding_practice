from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElementsv1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        dumyHead = ListNode(next=head)
        currentNode = dumyHead
        while head:
            while head and head.val == val:
                head = head.next
            currentNode.next = head
            currentNode = currentNode.next 
            if head:
                head = head.next
            
        return dumyHead.next
    
    def removeElementsv2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dumy_head = ListNode(next=head)
        current = dumy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dumy_head.next
    
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """递归解决"""
        if not head:
            return head
        if head.val == val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
            return head
        


    def removeElementsv3(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        curr = head
        if not head:
            return head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head



