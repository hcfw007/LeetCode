class Solution:
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        ans = s.rfind(" ")
        if not s: return 0
        return len(s) if ans < 0 else len(s) - ans - 1