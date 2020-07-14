class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        a = 1
        while a <= bound:
            b = 1
            while a + b <= bound:
                result.add(a + b)
                if y == 1:
                    break
                b *= y
            if x == 1:
                break
            a *= x
        return list(result)
