class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            d = 2
            while d * d <= num:
                if num % d == 0:
                    return False
                d += 1
            return True

        num = max(n, 2)
        while True:
            s = str(num)
            if s == s[::-1] and is_prime(num):
                return num
            num += 1
            if 10000000 <= num < 100000001:
                num = 100000001
