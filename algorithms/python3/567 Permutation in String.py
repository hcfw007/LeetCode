class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        for i in range(n):
            window[s2[i]] = window.get(s2[i], 0) + 1
            if i >= m:
                left = s2[i - m]
                if window[left] == 1:
                    del window[left]
                else:
                    window[left] -= 1
            if window == need:
                return True
        return False
