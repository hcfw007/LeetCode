from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = Counter(deck)
        values = list(count.values())
        g = values[0]
        for v in values[1:]:
            g = gcd(g, v)
            if g < 2:
                return False
        return g >= 2
