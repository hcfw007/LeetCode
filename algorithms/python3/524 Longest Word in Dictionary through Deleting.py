class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word):
            it = iter(s)
            return all(ch in it for ch in word)

        best = ""
        for word in dictionary:
            if is_subsequence(word) and (len(word) > len(best) or (len(word) == len(best) and word < best)):
                best = word
        return best
