class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        chars = list(s)
        lo, hi = 0, len(chars) - 1
        while lo < hi:
            while lo < hi and chars[lo] not in vowels:
                lo += 1
            while lo < hi and chars[hi] not in vowels:
                hi -= 1
            chars[lo], chars[hi] = chars[hi], chars[lo]
            lo += 1
            hi -= 1
        return "".join(chars)
