class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        avail = 9
        cur = 9
        for _ in range(2, n + 1):
            cur *= avail
            avail -= 1
            ans += cur
        return ans
