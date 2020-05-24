class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for row in grid:
            if row[0] == 0:
                for i in range(n):
                    row[i] ^= 1
        total = 0
        for c in range(n):
            ones = sum(grid[r][c] for r in range(m))
            total += max(ones, m - ones) << (n - 1 - c)
        return total
