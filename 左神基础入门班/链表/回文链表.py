from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        stack = []
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow = slow.next
        while slow:
            stack.append(slow.val)
            slow = slow.next
        while stack:
            val = stack.pop()
            if val != head.val:
                return False
            else:
                head = head.next
        return True






        # stack = []
        # if not head:
        #     return True
        # curr = head
        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next
        # while stack:
        #     val = stack.pop()
        #     if head.val != val:
        #         return False
        #     else:
        #         head = head.next
        # return True


        # slow, fast = head, head.next
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # prev = slow
        # curr = slow.next
        # slow.next = None
        # while curr:
        #     next_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_node
        # head1, head2 = head, prev
        # while head1 != head2 and head1:
        #     if head1.val != head2.val:
        #         return False
        #     else:
        #         head1 = head1.next
        #         head2 = head2.next
        # head = prev
        # prev = None
        # while head:
        #     next_node = head.next
        #     head.next = prev
        #     prev = head
        #     head = next_node
        # return True
        
