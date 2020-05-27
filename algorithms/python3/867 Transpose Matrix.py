class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        return [[matrix[r][c] for r in range(m)] for c in range(n)]
