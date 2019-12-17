class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if n > m:
            return []
        need = {}
        for ch in p:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        ans = []
        for i in range(m):
            window[s[i]] = window.get(s[i], 0) + 1
            if i >= n:
                left = s[i - n]
                if window[left] == 1:
                    del window[left]
                else:
                    window[left] -= 1
            if window == need:
                ans.append(i - n + 1)
        return ans
