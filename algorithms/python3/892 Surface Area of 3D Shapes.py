class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] > 0:
                    total += 2 + 4 * grid[r][c]
                    if r > 0:
                        total -= 2 * min(grid[r][c], grid[r - 1][c])
                    if c > 0:
                        total -= 2 * min(grid[r][c], grid[r][c - 1])
        return total
