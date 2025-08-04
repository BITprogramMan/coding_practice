from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sH, sT, eH, eT, bH, bT = None, None, None, None, None, None
        while head:
            if head.val < x:
                if not sT:
                    sH, sT = head, head
                else:
                    sT.next = head
                    sT = sT.next
            elif head.val == x:
                if not eT:
                    eH, eT = head, head
                else:
                    eT.next = head
                    eT = eT.next
            else:
                if not bT:
                    bH, bT = head, head
                else:
                    bT.next = head 
                    bT = bT.next
            head = head.next
        if sT:
            sT.next = eH
            if not eT:
                eT = sT
        if eT:
            eT.next = bH
        if sH:
            return sH
        elif eH:
            return eH
        else:
            return bH
        