class Solution:
    def isPalindrome(self, s):
        s = [c.lower() for c in s if (c.isalnum())]               
        return s[:] == s[::-1]