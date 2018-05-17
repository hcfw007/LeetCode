class Solution:
    def addTwoNumbers(self, l1, l2):
        addOne = 0
        head = ListNode(0)
        current = head
        while ((l1 != None) or (l2 != None) or (addOne != 0)):
            t = addOne
            t = t + l1.val if l1 != None else t
            t = t + l2.val if l2 != None else t
            if t >= 10:
                t -= 10
                addOne = 1
            else:
                addOne = 0
            tempNode = ListNode(t)
            current.next = tempNode
            current = tempNode
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        return head.next

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None