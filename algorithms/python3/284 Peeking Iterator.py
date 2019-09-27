class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._has_next = iterator.hasNext()
        self._next = iterator.next() if self._has_next else None

    def peek(self):
        return self._next

    def next(self):
        val = self._next
        self._has_next = self.iterator.hasNext()
        self._next = self.iterator.next() if self._has_next else None
        return val

    def hasNext(self):
        return self._has_next
