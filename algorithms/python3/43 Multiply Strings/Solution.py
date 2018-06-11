class Solution:
    def multiply(self, num1, num2):
        if (len(num1) < len(num2)): num1, num2 = num2, num1
        lines = []
        for i in range(len(num2) - 1, -1, -1):
            singleMultiplier = num2[i]
            addon = 0
            line = ""
            for j in range(len(num1) - 1, -1, -1):
                t = int(singleMultiplier) * int(num1[j]) + addon
                addon = t // 10
                digit = t % 10
                line = str(digit) + line
            if (addon != 0): line = str(addon) + line
            for j in range(len(num2) - i - 1): line += "0"
            lines.append(line)
        ans = 0
        for i in range(len(lines)):
            ans = self.add(str(ans), lines[i])
        t = -1
        for i in range(len(ans) - 1):
            if (ans[i] != "0"):
                break
            else:
                t = i
        return ans[t + 1:]
    def add(self, num1, num2):
        if (len(num1) < len(num2)): num1, num2 = num2, num1
        ans = ""
        addon = 0
        for i in range(1, len(num1) + 1):
            adder1 = num1[-i]
            adder2 = num2[-i] if (len(num2) + 1 > i) else 0
            digit = int(adder1) + int(adder2) + addon
            addon = 1 if (digit > 9) else 0
            digit = digit - 10 if (addon > 0) else digit
            ans = str(digit) + ans
        if (addon == 1): ans = "1" + ans
        return ans