class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}

        def in_order(a, b):
            for ca, cb in zip(a, b):
                if rank[ca] < rank[cb]:
                    return True
                if rank[ca] > rank[cb]:
                    return False
            return len(a) <= len(b)

        return all(in_order(words[i], words[i + 1]) for i in range(len(words) - 1))
