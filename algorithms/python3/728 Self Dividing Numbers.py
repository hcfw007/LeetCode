class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            temp = num
            ok = True
            while temp:
                d = temp % 10
                if d == 0 or num % d != 0:
                    ok = False
                    break
                temp //= 10
            if ok:
                ans.append(num)
        return ans
