class Solution:
    def strStr(self, haystack, needle):
        if (len(needle) == 0): return 0
        for i in range(len(haystack) - len(needle) + 1):
            if (haystack[i] == needle[0]):
                corr = True
                for j in range(1, len(needle)):
                    if (haystack[i + j] != needle[j]):
                        corr = False
                        break
                if (corr): return i
        return -1