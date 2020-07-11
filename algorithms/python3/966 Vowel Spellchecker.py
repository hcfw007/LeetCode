class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        cap = {}
        vowel = {}
        for word in wordlist:
            lower = word.lower()
            cap.setdefault(lower, word)
            masked = "".join("*" if ch in "aeiou" else ch for ch in lower)
            vowel.setdefault(masked, word)

        def check(q):
            if q in exact:
                return q
            lower = q.lower()
            if lower in cap:
                return cap[lower]
            masked = "".join("*" if ch in "aeiou" else ch for ch in lower)
            return vowel.get(masked, "")

        return [check(q) for q in queries]
