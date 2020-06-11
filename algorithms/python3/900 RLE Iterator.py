class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.i = 0

    def next(self, n: int) -> int:
        while self.i < len(self.encoding) and n > 0:
            if self.encoding[self.i] >= n:
                self.encoding[self.i] -= n
                return self.encoding[self.i + 1]
            n -= self.encoding[self.i]
            self.i += 2
        return -1
