class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        out = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(num1[i]) - 48
                i -= 1
            if j >= 0:
                total += ord(num2[j]) - 48
                j -= 1
            carry, digit = divmod(total, 10)
            out.append(chr(48 + digit))
        return "".join(reversed(out))
