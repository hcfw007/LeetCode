class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        i = 0
        while i < len(s):
            print(i)
            if i + max_length > len(s) - 1: break
            current_length = 0
            debt = 0
            j = 0
            debt_pivot = float('inf')
            while debt >= 0 and i + j < len(s):
                if s[i + j] == '(':
                    debt += 1
                else:
                    debt -= 1
                    print(debt, debt_pivot)
                    if debt_pivot > debt: debt_pivot = debt
                if debt == 0:
                    current_length = j + 1
                j += 1
            if current_length > max_length:
                max_length = current_length

                print(i, current_length)
                i += current_length
                
                continue
            if debt_pivot == float('inf'): return max_length
            if debt_pivot > 0 and i + j >= len(s):
                t = 0
                while i + t < len(s) and s[i + t] == '(' and t < debt_pivot: t += 1
                k = 1
                while k < len(s) and s[-k] == '(': k += 1
                if t > k + 1:
                    i += t - k - 1
                    continue
            i += 1

        return max_length