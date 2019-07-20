class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def checkCoord(coord: List[int]) -> bool:
            return 0 <= coord[0] and 0 <= coord[1] and coord[0] < l and coord[1] < w

        def newCoords(coord: List[int]) -> List[List[int]]:
            return [
                [coord[0] + 1, coord[1]],
                [coord[0] - 1, coord[1]],
                [coord[0], coord[1] + 1],
                [coord[0], coord[1] - 1]
            ]

        def checkExistance(coord: List[int], coords: List[List[int]]) ->bool:
            for item in coords:
                if item[0] == coord[0] and item[1] == coord[1]:
                    return False
            return True

        def tryToWord(coords: List[List[int]], left: str) -> bool:
            print(coords, left)
            coord = coords[-1]
            for newCoord in newCoords(coord):
                print(newCoord, left, checkCoord(newCoord), checkExistance(newCoord, coords), board[newCoord[0]][newCoord[1]] == left[0] if checkCoord(newCoord) else 'N/A')
                if checkCoord(newCoord) and checkExistance(newCoord, coords) and board[newCoord[0]][newCoord[1]] == left[0]:
                    t = left[1:]
                    coords.append(newCoord)
                    if len(t) == 0 or tryToWord(coords, t):
                        return True
                    coords.pop()
            return False

        if len(word) == 0:
            return False
        first = word[0]
        l, w = len(board), len(board[0])
        for i in range(l):
            for j in range(w):
                if board[i][j] == first:
                    if len(word) == 1:
                        return True
                    if tryToWord([[i, j]], word[1:]):
                        return True

        return False