class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        length = 0
        odd_found = False
        for c in count.values():
            length += c // 2 * 2
            if c % 2 == 1:
                odd_found = True
        return length + 1 if odd_found else length
