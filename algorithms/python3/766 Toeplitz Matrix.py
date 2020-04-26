class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False
        return True
