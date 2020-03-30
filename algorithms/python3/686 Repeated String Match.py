class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 1
        text = a
        while len(text) < len(b):
            text += a
            count += 1
        if b in text:
            return count
        if b in text + a:
            return count + 1
        return -1
