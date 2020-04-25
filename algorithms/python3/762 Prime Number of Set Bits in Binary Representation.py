class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        for num in range(left, right + 1):
            bits = 0
            while num:
                bits += num & 1
                num >>= 1
            if bits in primes:
                count += 1
        return count
