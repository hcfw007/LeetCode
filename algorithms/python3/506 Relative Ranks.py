class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        rank = {s: i for i, s in enumerate(sorted_scores)}
        ans = []
        for s in score:
            i = rank[s]
            if i == 0:
                ans.append("Gold Medal")
            elif i == 1:
                ans.append("Silver Medal")
            elif i == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(i + 1))
        return ans
