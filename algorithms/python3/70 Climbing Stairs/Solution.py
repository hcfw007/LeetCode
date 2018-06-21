class Solution(object):
    def climbStairs(self, n):
        if (n == 0 or n == 1): return 1
        l = [1, 1]
        for i in range(2, n + 1): l.append(l[i - 1] + l[i - 2])
        return l[n]