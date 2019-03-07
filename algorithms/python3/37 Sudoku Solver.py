class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def findNextSlot():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.': return [i, j]
            return None

        def place(position, num):
            for i in range(9):
                if board[i][position[1]] == str(num) or board[position[0]][i] == str(num): return False

            x = (position[0] // 3) * 3
            y = (position[1] // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[x + i][y + j] == str(num): return False
            return True

        def nextStep():
            position = findNextSlot()
            if not position: return True

            for i in range(1, 10):
                if place(position, i):
                    board[position[0]][position[1]] = str(i)
                    if nextStep(): return True
                    board[position[0]][position[1]] = '.'

            return False

        nextStep()