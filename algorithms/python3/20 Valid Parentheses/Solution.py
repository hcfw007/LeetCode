class Solution:
    def isValid(self, s):
        brackets = ['(', '[', '{', ')', ']', '}']
        stack = []
        for i in range(len(s)):
            t = brackets.index(s[i])
            if (t < 3):
                stack.append(t)
            else:
                if (len(stack) > 0 and (stack[len(stack) - 1]) == t - 3):
                    stack.pop(len(stack) - 1)
                else:
                    return False
        if (len(stack) == 0):
            return True
        else:
            return False