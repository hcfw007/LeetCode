class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = []
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((cur, num))
                cur = []
                num = 0
            elif ch == ']':
                prev, repeat = stack.pop()
                prev.extend(cur * repeat)
                cur = prev
            else:
                cur.append(ch)
        return "".join(cur)
