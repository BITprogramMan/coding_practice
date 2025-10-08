class Solution:
    """
    给定一个环形链表，长度为n，从头结点开始编号，从1到n。给定一个整数m，从头结点开始报数，报数从1开始，报到m就删除这个节点，
    下个节点从1开始重新报数，最后只剩下一个节点，求解这个节点的编号
    """
    def process1(self, head, m):
        if head is None or head.next == head or m < 1:
            return head
        last = head
        while last.next != head:
            last = last.next
        count = 0
        while head != last:
            count += 1
            if count == m:
                last.next = head.next
                count = 0
            else:
                last = last.next
            head = head.next
        return head
    
    def process2(self, head, m):
        if head is None or head.next == head or m < 1:
            return head
        cur = head.next
        length = 1
        while cur != head:
            cur = cur.next
            length += 1
        def getLive(length, m):
            if length == 1:
                return 1
            return (getLive(length - 1, m) + m - 1) % length + 1
        node_id = getLive(length, m)
        while node_id > 1:
            head = head.next
        head.next = head
        return head