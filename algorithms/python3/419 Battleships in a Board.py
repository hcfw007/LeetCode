class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        count = 0
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X':
                    if (r == 0 or board[r - 1][c] != 'X') and (c == 0 or board[r][c - 1] != 'X'):
                        count += 1
        return count
