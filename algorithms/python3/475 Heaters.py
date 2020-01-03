class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0

        def closest(h):
            lo, hi = 0, len(heaters)
            while lo < hi:
                mid = (lo + hi) // 2
                if heaters[mid] < h:
                    lo = mid + 1
                else:
                    hi = mid
            best = None
            if lo < len(heaters):
                best = heaters[lo] - h
            if lo > 0 and (best is None or h - heaters[lo - 1] < best):
                best = h - heaters[lo - 1]
            return best

        for h in houses:
            radius = max(radius, closest(h))
        return radius
