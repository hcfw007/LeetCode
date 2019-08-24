class Solution:
    def convertToTitle(self, n: int) -> str:
        result = []
        while n:
            n -= 1
            result.append(chr(n % 26 + ord("A")))
            n //= 26
        return "".join(reversed(result))
