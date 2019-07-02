class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]: return False
        for i in range(m):
            if target < matrix[i][0]:
                for j in range(n):
                    if matrix[i - 1][j] == target: return True
                break
        else:
            for j in range(n):
                    if matrix[m - 1][j] == target: return True

        return False