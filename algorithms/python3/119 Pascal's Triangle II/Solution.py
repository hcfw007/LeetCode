class Solution:
    def getRow(self, rowIndex):
        if (rowIndex == 0): return [1]
        ans = []
        for i in range(rowIndex + 1):
            ans.append(self.getCombination(rowIndex, i))
        return ans
    
    def getCombination(self, n, m):
        if (m == 0 or m == n): return 1
        return (self.getFactorial(n)) // (self.getFactorial(m) * self.getFactorial(n - m))

    def getFactorial(self, x):
        ans = 1
        for i in range(1, x + 1):
            ans *= i
        return ans