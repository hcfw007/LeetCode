class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for ch in s:
            result ^= ord(ch)
        for ch in t:
            result ^= ord(ch)
        return chr(result)
