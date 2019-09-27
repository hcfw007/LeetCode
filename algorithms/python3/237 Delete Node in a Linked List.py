class Solution:
    def deleteNode(self, node) -> None:
        node.val = node.next.val
        node.next = node.next.next
