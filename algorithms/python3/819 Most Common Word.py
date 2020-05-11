class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = []
        word = []
        for ch in paragraph.lower():
            if ch.isalpha():
                word.append(ch)
            elif word:
                words.append("".join(word))
                word = []
        if word:
            words.append("".join(word))
        count = {}
        for w in words:
            if w not in banned_set:
                count[w] = count.get(w, 0) + 1
        return max(count, key=count.get)
