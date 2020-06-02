class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum(1 for row in grid for v in row if v > 0)
        front = sum(max(row) for row in grid)
        side = sum(max(col) for col in zip(*grid))
        return top + front + side
