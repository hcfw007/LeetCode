class Solution:
    def lengthOfLongestSubstring(self, s):
        if (len(s) == 0 ): return 0
        h = t = 0
        l = 1
        chars = {s[0]}
        for t in range(len(s)):
            if (h == t): continue
            if (s[t] in chars):
                while (s[h] != s[t]):
                    chars.remove(s[h])
                    h = h + 1
                h = h + 1
            else:
                chars.add(s[t])
            if (t - h + 1 > l): l = t - h + 1
        return l