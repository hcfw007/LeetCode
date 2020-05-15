class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            out = []
            for ch in string:
                if ch == "#":
                    if out:
                        out.pop()
                else:
                    out.append(ch)
            return "".join(out)

        return build(s) == build(t)
