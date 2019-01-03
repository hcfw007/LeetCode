class Solution:
    def reverseKGroup(self, head, k):
        pre = ListNode("ph")
        pre.next = head
        prehead = pre
        curr = head
        reverseGroup = []
        while (curr != None):
            reverseGroup.append(curr)
            curr = curr.next
            if (len(reverseGroup) == k):
                nex = reverseGroup[-1].next
                for j in range(len(reverseGroup) - 1, -1, -1):
                    reverseGroup[j].next = reverseGroup[j - 1] if j > 0 else nex
                pre.next = reverseGroup[-1]
                pre = reverseGroup[0]
                reverseGroup = []            
        return prehead.next
            

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None