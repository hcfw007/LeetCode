class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def magic(r, c):
            vals = [grid[r + dr][c + dc] for dr in range(3) for dc in range(3)]
            if sorted(vals) != list(range(1, 10)):
                return False
            for i in range(3):
                if sum(vals[3 * i:3 * i + 3]) != 15:
                    return False
                if vals[i] + vals[i + 3] + vals[i + 6] != 15:
                    return False
            return vals[0] + vals[4] + vals[8] == 15 and vals[2] + vals[4] + vals[6] == 15

        count = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                if grid[r + 1][c + 1] == 5 and magic(r, c):
                    count += 1
        return count
