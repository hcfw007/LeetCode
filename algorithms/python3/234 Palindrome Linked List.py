class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        return vals == vals[::-1]
