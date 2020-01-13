class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total = 0
        for i in range(len(timeSeries) - 1):
            total += min(duration, timeSeries[i + 1] - timeSeries[i])
        return total + duration
