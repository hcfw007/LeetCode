class Solution:
    def mySqrt(self, x):
        n = 0
        while (10 ** n < x): n += 1
        ans = 0
        while (n > -1):
            t = ans + 10 ** n
            if (t ** 2 > x):
                n -= 1
            else:
                ans = t
        return ans