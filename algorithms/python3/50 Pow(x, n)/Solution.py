class Solution:
    def myPow(self, x, n):
        if (n == 0): return 1
        if (x == 0): return 0
        if (x == 1): return 1
        if (x == -1): return 1 if n % 2 == 0 else -1
        ans = 1
        for i in range(n):
            ans *= x
            if (ans == 0.0): break
        for i in range(0, n, -1):
            ans /= x
            if (ans == 0.0): break
        return ans