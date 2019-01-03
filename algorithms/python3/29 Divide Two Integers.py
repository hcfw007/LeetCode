class Solution:
    def divide(self, dividend, divisor):
        if (dividend < -2 ** 31 or dividend > 2 ** 31 -1): return 2 ** 31 - 1
        if (dividend == -2 ** 31 and divisor == 1): return - 2 ** 31
        if (dividend == -2 ** 31 and divisor == -1): return 2 ** 31 - 1
        if (dividend < 0):
            dividend = -dividend
            divisor = -divisor
        elif (dividend == 0):
            return 0
        ans = 0
        if (abs(divisor) == 1):
            ans = dividend
        else:
            while (dividend >= 100000 * abs(divisor)):
                dividend -= abs(divisor) * 100000
                ans += 100000
            while (dividend >= 1000 * abs(divisor)):
                dividend -= abs(divisor) * 1000
                ans += 1000
            while (dividend >= 10 * abs(divisor)):
                dividend -= abs(divisor) * 10
                ans += 10
            while (dividend >= 0):
                dividend -= abs(divisor)
                ans += 1
            ans -= 1
        return ans if divisor > 0 else -ans