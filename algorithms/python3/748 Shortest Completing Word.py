class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = {}
        for ch in licensePlate.lower():
            if ch.isalpha():
                need[ch] = need.get(ch, 0) + 1
        best = None
        for word in words:
            count = {}
            for ch in word:
                count[ch] = count.get(ch, 0) + 1
            if all(count.get(ch, 0) >= cnt for ch, cnt in need.items()):
                if best is None or len(word) < len(best):
                    best = word
        return best
