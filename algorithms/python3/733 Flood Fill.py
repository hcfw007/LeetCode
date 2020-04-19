class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        if start == color:
            return image
        m, n = len(image), len(image[0])
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            image[r][c] = color
            for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= rr < m and 0 <= cc < n and image[rr][cc] == start:
                    stack.append((rr, cc))
        return image
