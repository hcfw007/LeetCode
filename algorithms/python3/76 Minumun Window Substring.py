class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}
        for i in range(len(t)):
            if not t[i] in tDict:
                tDict[t[i]] = 1
            else:
                tDict[t[i]] += 1

        if not validate(s, tDict): return ''

        head = 0
        tail = 0
        ans = -1
        while (not validate(s[head:tail + 1], tDict)) and tail <len(s) - 1:
            tail += 1
        ans = head
        minLength = tail - head + 1

        while tail < len(s):
            while (not s[head] in tDict) or s[head:tail + 1].count(s[head]) > tDict[s[head]]:
                head += 1

            if tail - head < minLength:
                minLength = tail - head
                ans = head

            missingChar = s[head]
            head += 1
            tail += 1
            while tail < len(s) and s[tail] != missingChar:
                tail += 1

        return s[ans:ans + minLength + 1]


def validate(s: str, t: dict) -> bool:
    for i in t:
        if s.count(i) < t[i]: return False
    return True