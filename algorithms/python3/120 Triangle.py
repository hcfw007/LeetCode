class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                row[j] = triangle[i][j] + min(row[j], row[j + 1])
        return row[0]
