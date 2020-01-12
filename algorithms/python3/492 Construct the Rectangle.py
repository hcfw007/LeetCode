class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = 1
        while (w + 1) * (w + 1) <= area:
            w += 1
        while area % w != 0:
            w -= 1
        return [area // w, w]
