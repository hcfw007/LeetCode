class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for r in range(8):
            for c in range(8):
                if board[r][c] == "R":
                    count = 0
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        rr, cc = r + dr, c + dc
                        while 0 <= rr < 8 and 0 <= cc < 8 and board[rr][cc] == ".":
                            rr += dr
                            cc += dc
                        if 0 <= rr < 8 and 0 <= cc < 8 and board[rr][cc] == "p":
                            count += 1
                    return count
        return 0
