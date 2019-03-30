import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        ans = ""
        factorial = 1
        for i in range(1, n): factorial *= i
        print(factorial)
        while n > 1:
            index = math.floor((k - 1) / factorial)
            print(index, nums, k)
            ans += nums[index]
            nums.pop(index)
            k -= factorial * (index + 1)
            factorial /= (n - 1)
            n -= 1

        ans += nums[0]

        return ans