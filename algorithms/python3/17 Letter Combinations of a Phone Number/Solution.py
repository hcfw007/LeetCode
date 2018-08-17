class Solution:
    def letterCombinations(self, digits):
        ans = [""]
        for x in digits:
            ans = [s + c for c in ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"][int(x)-2] for s in ans]
        return [] if len(ans) == 1 else ans