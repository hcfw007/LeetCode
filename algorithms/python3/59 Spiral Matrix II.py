class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(n)]
        count = 1
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        direction = 0
        point = [0, 0]
        while count <= n ** 2:
            matrix[point[0]][point[1]] = count
            newPoint = [point[0] + directions[direction][0], point[1] + directions[direction][1]]
            if newPoint[0] < n and newPoint[1] < n and matrix[newPoint[0]][newPoint[1]] == -1:
                point = newPoint
            else:
                if direction == len(directions) - 1:
                    direction = 0
                else:
                    direction += 1
                point = [point[0] + directions[direction][0], point[1] + directions[direction][1]]
            count += 1
        
        return matrix