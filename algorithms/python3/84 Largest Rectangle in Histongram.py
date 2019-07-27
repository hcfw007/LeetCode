class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        heights.append(0)
        stack = []
        pStack = -1
        pHeights = 0
        maxArea = 0
        while pHeights < len(heights):
            if len(stack) == 0 or heights[stack[pStack]] <= heights[pHeights]:
                stack.append(pHeights)
                pStack += 1
            else:
                while len(stack) > 0 and heights[stack[pStack]] > heights[pHeights]:
                    height = heights[stack[pStack]]
                    width = pHeights - (-1 if pStack <= 0 else stack[pStack - 1]) - 1
                    maxArea = max(maxArea, height * width)
                    t = stack.pop()
                    pStack -= 1
                stack.append(pHeights)
                pStack += 1
            pHeights += 1
        
        return maxArea