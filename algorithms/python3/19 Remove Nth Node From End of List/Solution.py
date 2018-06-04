class Solution:
    def removeNthFromEnd(self, head, n):
        t = []
        current = head
        while (current != None):
            t.append(current)
            current = current.next
        if (n == len(t)):
            head = head.next
            return head
        t[len(t) - n - 1].next = t[len(t) - n].next
        return head

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None