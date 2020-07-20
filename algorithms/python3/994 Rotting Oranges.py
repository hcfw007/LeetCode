from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while queue:
            r, c, t = queue.popleft()
            minutes = max(minutes, t)
            for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == 1:
                    grid[rr][cc] = 2
                    fresh -= 1
                    queue.append((rr, cc, t + 1))
        return minutes if fresh == 0 else -1
