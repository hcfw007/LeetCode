class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        c2w = {}
        w2c = {}
        for ch, w in zip(pattern, words):
            if ch in c2w:
                if c2w[ch] != w:
                    return False
            else:
                c2w[ch] = w
            if w in w2c:
                if w2c[w] != ch:
                    return False
            else:
                w2c[w] = ch
        return True
