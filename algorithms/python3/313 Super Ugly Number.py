class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        idx = [0] * len(primes)
        vals = primes[:]
        while len(ugly) < n:
            nxt = min(vals)
            ugly.append(nxt)
            for i, v in enumerate(vals):
                if v == nxt:
                    idx[i] += 1
                    vals[i] = ugly[idx[i]] * primes[i]
        return ugly[-1]
