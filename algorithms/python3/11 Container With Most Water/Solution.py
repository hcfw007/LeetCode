class Solution:
    def maxArea(self, height):
        maxCapacity = 0
        i, j = 0, len(height) - 1
        while (j > i):
            maxCapacity = max(maxCapacity, (j - i) * min(height[i], height[j]))
            if (height[i] > height[j]):
                j -= 1
            else:
                i += 1
        return maxCapacity