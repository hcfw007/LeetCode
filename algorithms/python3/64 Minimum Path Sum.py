class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        matrix = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        matrix[1][1] = grid[0][0]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1: continue
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1]) + grid[i - 1][j - 1]

        return matrix[m][n]