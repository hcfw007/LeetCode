class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch, c in count.items():
            if c < k:
                return max(self.longestSubstring(part, k) for part in s.split(ch))
        return len(s)
