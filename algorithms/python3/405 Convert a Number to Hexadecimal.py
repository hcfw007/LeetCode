class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        chars = "0123456789abcdef"
        num &= 0xFFFFFFFF
        out = []
        while num:
            out.append(chars[num & 15])
            num >>= 4
        return "".join(reversed(out))
