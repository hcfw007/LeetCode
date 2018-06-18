class Solution(object):
    def addBinary(self, a, b):
        num1 = a
        num2 = b
        if (len(num1) < len(num2)): num1, num2 = num2, num1
        ans = ""
        addon = 0
        for i in range(1, len(num1) + 1):
            adder1 = num1[-i]
            adder2 = num2[-i] if (len(num2) + 1 > i) else 0
            digit = int(adder1) + int(adder2) + addon
            addon = 1 if (digit > 1) else 0
            digit = digit - 2 if (addon > 0) else digit
            ans = str(digit) + ans
        if (addon == 1): ans = "1" + ans
        return ans