class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j, ch in enumerate(typed):
            if i < len(name) and name[i] == ch:
                i += 1
            elif j == 0 or typed[j - 1] != ch:
                return False
        return i == len(name)
