class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                inner = stack.pop()
                stack[-1] += max(2 * inner, 1)
        return stack[0]
