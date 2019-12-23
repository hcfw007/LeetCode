class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for i, (x1, y1) in enumerate(points):
            dist_count = {}
            for j, (x2, y2) in enumerate(points):
                if i == j:
                    continue
                d = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
                dist_count[d] = dist_count.get(d, 0) + 1
            for c in dist_count.values():
                total += c * (c - 1)
        return total
