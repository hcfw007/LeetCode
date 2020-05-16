class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        prev = -1
        best = 0
        for i, seat in enumerate(seats):
            if seat == 1:
                if prev == -1:
                    best = i
                else:
                    best = max(best, (i - prev) // 2)
                prev = i
        best = max(best, n - 1 - prev)
        return best
