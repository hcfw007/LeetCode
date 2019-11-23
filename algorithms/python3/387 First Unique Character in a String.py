class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1
