class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i, c in enumerate(citations):
            if c >= n - i:
                return n - i
        return 0
