from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        def merge(head1, head2):
            if not head1:
                return head2
            elif not head2:
                return head1
            else:
                dumy_head = ListNode()
                curr = dumy_head
                while head1 and head2:
                    if head1.val <= head2.val:
                        curr.next = head1
                        head1 = head1.next
                    else:
                        curr.next = head2
                        head2 = head2.next
                    curr = curr.next
                curr.next = head1 if head1 else head2
                return dumy_head.next
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr = slow.next
        slow.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(curr)
        return merge(head1, head2)

                

