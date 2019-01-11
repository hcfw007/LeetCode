# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def getMinNode(lists: List[ListNode]) -> ListNode:
            min = float('inf')
            node = None
            for item in lists:
                if item.val < min:
                    node = item
                    min = item.val
            return node

        lists = list(filter(None, lists)) 
        if len(lists) == 0: return None
        head = getMinNode(lists)
        p = head
        while len(lists) > 0:
            for index in range(len(lists)):
                if lists[index] == p: 
                    lists[index] = p.next
                    if lists[index] == None: lists.remove(lists[index])
                    break
            t = getMinNode(lists)
            p.next = t
            p = t

        return head