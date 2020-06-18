class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        lo, hi = 0, len(chars) - 1
        while lo < hi:
            if not chars[lo].isalpha():
                lo += 1
            elif not chars[hi].isalpha():
                hi -= 1
            else:
                chars[lo], chars[hi] = chars[hi], chars[lo]
                lo += 1
                hi -= 1
        return "".join(chars)
