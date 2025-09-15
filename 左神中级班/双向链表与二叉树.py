class Solution:
    """
    双向链表节点结构和二叉树节点结构是一样的，如果你把last认为是left，
    next认为是next的话。
    给定一个搜索二叉树的头节点head，请转化成一条有序的双向链表，并返回链
    表的头节点。
    """
    def process(self, head):
        def recursive(head):
            if not head.left and not head.right:
                return head, head
            left_head, left_tail, right_head, right_tail = None, None, None, None
            if head.left:
                left_head, left_tail = recursive(head.left)
                left_tail.next = head
                head.pre = left_tail
            if head.right:
                right_head, right_tail = recursive(head.right)
                head.next = right_head
                right_head.pre = head
            left_head = left_head if left_head else head
            right_tail = right_tail if right_tail else head
            return left_head, right_tail
        if not head:
            return None
        else:
            left_head, right_tail = recursive(head)
            return left_head
