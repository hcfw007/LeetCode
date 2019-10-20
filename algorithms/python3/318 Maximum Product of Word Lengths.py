class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = {}
        for w in words:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - 97)
            masks[mask] = max(masks.get(mask, 0), len(w))
        best = 0
        items = list(masks.items())
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i][0] & items[j][0] == 0:
                    best = max(best, items[i][1] * items[j][1])
        return best
