from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, o1, o2):
        return o1.val - o2.val



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        if len(lists) < 1:
            return None 
        dumy_head = ListNode()
        heapq.heapify(lists)
        head = heapq.heappop(lists)
        if head.next:
            heapq.heappush(lists, head.next)
        pre = head
        while lists:
            node = heapq.heappop(lists)
            pre.next = node
            pre = node
            if node.next:
                heapq.heappush(lists, node.next)
        return head
