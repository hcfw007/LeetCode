class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        built = set()
        best = ""
        for word in words:
            if len(word) == 1 or word[:-1] in built:
                built.add(word)
                if len(word) > len(best):
                    best = word
        return best
