class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            rcheck = set()
            ccheck = set()
            scheck = set()
            for j in range(9):
                if (board[i][j] != "."):
                    if (board[i][j] in rcheck):
                        return False
                    else:
                        rcheck.add(board[i][j])
                if (board[j][i] != "."):
                    if (board[j][i] in ccheck):
                        return False
                    else:
                        ccheck.add(board[j][i])
                si = (i // 3) * 3 + j // 3
                sj = (i % 3) * 3 + j % 3
                if (board[si][sj] != "."):
                    if (board[si][sj] in scheck):
                        return False
                    else:
                        scheck.add(board[si][sj])
        return True