class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        distance = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): distance[i][0] = i
        for j in range(n + 1): distance[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                costAdd = distance[i][j - 1 ] + 1
                costDelete = distance[i - 1][j] + 1
                costReplace = distance[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else distance[i - 1][j - 1] + 1
                distance[i][j] = min(costAdd, costDelete, costReplace)
        
        return distance[m][n]
