class Solution:
    def mergeTwoLists(self, l1, l2):
        if (not l1): return l2
        if (not l2): return l1
        if (l1.val < l2.val):
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        curr = head
        while l1 and l2:
            if l1.val < l2.val:                
                curr.next = l1
                l1=l1.next                
            else:                
                curr.next = l2
                l2=l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return head