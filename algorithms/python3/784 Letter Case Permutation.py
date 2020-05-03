class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        for ch in s:
            if ch.isalpha():
                ans = [prefix + c for prefix in ans for c in (ch.lower(), ch.upper())]
            else:
                ans = [prefix + ch for prefix in ans]
        return ans
