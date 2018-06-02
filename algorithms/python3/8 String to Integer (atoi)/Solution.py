import string

class Solution:
    def myAtoi(self, str):
        s = str.strip()
        if not s:
            return 0
        
        i = 1 if (s[0] == '-' or s[0] == '+') else 0
        while i < len(s):
            if s[i] in string.digits:
                i += 1
            else:
                break
        
        s = s[0:i]
        if not s:
            return 0
        if (s == '+' or s == '-'): return 0
        s = int(s)
        return 2**31-1 if s >= 2**31 - 1 else -2**31 if s <= -2**31 else s