class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return sum(isPrime)
