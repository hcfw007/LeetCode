class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                self.prefix[r + 1][c + 1] = (matrix[r][c] + self.prefix[r][c + 1]
                                             + self.prefix[r + 1][c] - self.prefix[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1]
                - self.prefix[row2 + 1][col1] + self.prefix[row1][col1])
