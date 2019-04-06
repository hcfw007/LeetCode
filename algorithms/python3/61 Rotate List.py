class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None: return None
        tail = head
        count = 1
        while tail.next != None:
            count += 1
            tail = tail.next
        tail.next = head
        rotate = count - (k % count)
        p = head
        while rotate > 1:
            p = p.next
            rotate -= 1
        newHead = p.next
        p.next = None
        return newHead
        