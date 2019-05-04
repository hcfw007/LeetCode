class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0] * (n + 1) for _ in range(m + 1)]
        matrix[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (i == 1 and j == 1) or obstacleGrid[i - 1][j - 1] == 1: continue
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m][n] if obstacleGrid[0][0] != 1 else 0