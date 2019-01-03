class Solution:
    def longestPalindrome(self, s):
        maxLength = 1
        start = 0
        for i in range(len(s)):
            t1 = 0
            while ((i - t1) >= 0 and (i + t1) < len(s) and s[i - t1] == s[i + t1]): t1 = t1 + 1
            t1 = t1 - 1
            if ((t1 * 2 + 1) > maxLength):
                maxLength = t1 * 2 + 1
                start = i - t1
            t2 = 1
            while ((i - t2 + 1) >= 0 and (i + t2) < len(s) and s[i - t2 + 1] == s[i + t2]): t2 = t2 + 1
            t2 = t2 - 1
            if ((t2 * 2) > maxLength):
                maxLength = t2 * 2
                start = i - t2 + 1
        str = ""
        for i in range(start, start + maxLength):
            str = str + s[i]
        return str