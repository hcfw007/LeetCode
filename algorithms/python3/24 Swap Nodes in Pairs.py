class Solution:
    def swapPairs(self, head):
        if (head == None or head.next == None): return head
        current = head
        newHead = head.next
        t1 = t2 = last = None
        while (current != None and current.next != None):
            t1 = current
            t2 = current.next
            if (last != None): last.next = t2
            t1.next = t2.next
            t2.next = t1
            last = t1
            current = t1.next
        return newHead