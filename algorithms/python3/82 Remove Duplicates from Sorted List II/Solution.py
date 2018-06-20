class Solution(object):
    def deleteDuplicates(self, head):
        c = head
        if (c == None or c.next == None): return head
        if (c.val == c.next.val and c.next.next == None): return None
        p = ListNode("NaN")
        p.next = c
        c = head
        n = c.next
        head = p
        while (n != None and c != None):
            while (n and c.val == n.val): n = n.next
            if (c.next != n):
                p.next = n
                c = n
                n = n.next if n else None
            else:
                p = p.next
                c = c.next
                n = n.next if n else None
        return head if head.val != "NaN" else head.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None