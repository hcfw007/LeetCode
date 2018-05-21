class Solution:
    def convert(self, s, numRows):
        if (s == ""): return ""
        if (numRows == 1): return s
        noPerCycle = numRows * 2 - 2
        cycles = len(s) // noPerCycle + 1
        str = ""
        for i in range(cycles):
            if (i * noPerCycle < len(s)):
                str = str + s[i * noPerCycle]
        for j in range(1, numRows - 1):
            for i in range(cycles):
                if (i * noPerCycle + j < len(s)): str += s[i * noPerCycle + j]
                if ((i + 1) * noPerCycle - j < len(s)): str += s[(i + 1) * noPerCycle - j]
        for i in range(cycles):
            if (i * noPerCycle + numRows - 1 < len(s)): str = str + s[i * noPerCycle + numRows - 1]
        return str