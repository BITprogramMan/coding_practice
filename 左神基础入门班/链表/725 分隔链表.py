from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        num_split, num_remain = length // k, length % k
        index = 0
        res = [None] * k
        while index < k and head:
            res[index] = head
            part_size = num_split + (1 if index < num_remain else 0)
            for _ in range(part_size - 1):
                head = head.next
            next_node = head.next
            head.next = None
            head = next_node
            index += 1
        return res

            





