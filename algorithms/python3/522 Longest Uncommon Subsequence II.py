class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(a, b):
            it = iter(b)
            return all(ch in it for ch in a)

        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            if all(not is_subsequence(s, other) for j, other in enumerate(strs) if j != i):
                return len(s)
        return -1
