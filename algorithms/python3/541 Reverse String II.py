class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        for start in range(0, len(chars), 2 * k):
            lo = start
            hi = min(start + k, len(chars)) - 1
            while lo < hi:
                chars[lo], chars[hi] = chars[hi], chars[lo]
                lo += 1
                hi -= 1
        return "".join(chars)
