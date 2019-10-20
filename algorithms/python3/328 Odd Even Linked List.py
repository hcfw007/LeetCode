class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
