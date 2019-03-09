class Solution:
    def totalNQueens(self, n: int) -> int:
        if (n < 1): return []
        solutions = []

        def check(board, row, col):
            for i in range(len(board)):
                if col == board[i]: return False
                if abs(row - i) == abs(col - board[i]): return False
            return True

        def placeQueen(scheme):
            for i in range(n):
                if check(scheme, len(scheme), i):
                    scheme.append(i)
                    if len(scheme) == n:
                        solutions.append(0)
                    else:
                        placeQueen(scheme)
                    scheme.pop()
                else:
                    continue

        placeQueen([])
        return len(solutions)