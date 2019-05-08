class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s :
            return False

        if s[0] in ['+', '-']:
            s = s[1:]
        if 'e' in s:
            eList = s.split('e')
            if len(eList) > 2:
                return False
            eList[0] = eList[0].replace('.', '', 1)
            if len(eList[1]) > 0 and eList[1][0] in ['+', '-']:
                eList[1] = eList[1].replace(eList[1][0], '', 1)
            return eList[0].isnumeric() and eList[1].isnumeric()

        s = s.replace('.', '', 1)
        if s.isnumeric():
            return True
        return False 