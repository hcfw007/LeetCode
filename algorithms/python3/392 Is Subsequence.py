class Solution:
    def isSubsequence(self, s, t):
        if (not s):
            return True
        for i in s:
            if (not i in t):
                return False
        index = 0
        for i in t:
            if (i == s[index]):
                if (index == len(s) - 1):
                    return True
                index += 1
        return False