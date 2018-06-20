class Solution(object):
    def deleteDuplicates(self, head):
        c = head
        if (c == None): return head
        n = c.next
        while (n != None and c != None):
            while (n and c.val == n.val): n = n.next
            c.next = n
            c = n
            n = n.next if n else None
        return head


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
