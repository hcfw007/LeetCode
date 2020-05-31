class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocked = set(map(tuple, obstacles))
        x = y = 0
        dx, dy = 0, 1
        best = 0
        for cmd in commands:
            if cmd == -2:
                dx, dy = -dy, dx
            elif cmd == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in blocked:
                        break
                    x, y = nx, ny
                    best = max(best, x * x + y * y)
        return best
