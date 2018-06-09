class Solution:
    def longestCommonPrefix(self, strs):
        commonStr = ""
        if (len(strs) == 0): return ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if (len(strs[j]) <= i or strs[j][i] != strs[0][i]):
                    return commonStr
            commonStr += strs[0][i]
        return commonStr