class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.count += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
        elif index <= self.count:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            node = Node(val)
            node.next = cur.next
            cur.next = node
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.count:
            if index == 0:
                self.head = self.head.next
            else:
                cur = self.head
                for _ in range(index - 1):
                    cur = cur.next
                cur.next = cur.next.next
            self.count -= 1
