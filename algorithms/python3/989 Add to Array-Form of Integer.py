class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        digits = []
        i = len(num) - 1
        carry = k
        while i >= 0 or carry:
            if i >= 0:
                carry += num[i]
                i -= 1
            digits.append(carry % 10)
            carry //= 10
        return digits[::-1]
