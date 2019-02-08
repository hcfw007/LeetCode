class Solution:
    def trap(self, height: List[int]) -> int:
        max = 0
        for i in range(len(height)):
            if height[i] > height[max]:
                max = i
        
        trap = 0

        cmax = 0
        for i in range(max):
            if height[i] > cmax:
                cmax = height[i]
            else:
                trap += cmax - height[i]

        cmax = 0
        for i in range(len(height) - 1, max - 1, -1):
            if height[i] > cmax:
                cmax = height[i]
            else:
                trap += cmax - height[i]

        return trap