class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if (n < 1): return []
        solutions = []

        def check(board, row, col):
            for i in range(len(board)):
                if col == board[i]: return False
                if abs(row - i) == abs(col - board[i]): return False
            return True

        def transferSolution(scheme):
            solution = []
            for i in range(n):
                row = ""
                for j in range(n):
                    if (scheme[i] == j):
                        row += 'Q'
                    else:
                        row += '.'
                solution.append(row)
            return solution

        def placeQueen(scheme):
            for i in range(n):
                if check(scheme, len(scheme), i):
                    scheme.append(i)
                    if len(scheme) == n:
                        solutions.append(transferSolution(scheme))
                    else:
                        placeQueen(scheme)
                    scheme.pop()
                else:
                    continue

        placeQueen([])
        return solutions