class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for row in image:
            result.append([1 - pixel for pixel in reversed(row)])
        return result
