class MyHashMap:
    def __init__(self):
        self.buckets = [[] for _ in range(1000)]

    def _hash(self, key: int) -> int:
        return key % 1000

    def put(self, key: int, value: int) -> None:
        b = self.buckets[self._hash(key)]
        for i, (k, _) in enumerate(b):
            if k == key:
                b[i] = (key, value)
                return
        b.append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.buckets[self._hash(key)]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        b = self.buckets[self._hash(key)]
        for i, (k, _) in enumerate(b):
            if k == key:
                b.pop(i)
                return
