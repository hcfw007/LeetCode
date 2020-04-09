class MyHashSet:
    def __init__(self):
        self.buckets = [[] for _ in range(1000)]

    def _hash(self, key: int) -> int:
        return key % 1000

    def add(self, key: int) -> None:
        b = self.buckets[self._hash(key)]
        if key not in b:
            b.append(key)

    def remove(self, key: int) -> None:
        b = self.buckets[self._hash(key)]
        if key in b:
            b.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._hash(key)]
