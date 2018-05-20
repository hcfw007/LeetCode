class Solution:
    def reverse(self, x):
        num = int(str(abs(x))[::-1])
        if num >= math.pow(2,31):
            return 0
        else:
            if x>0:
                return num
            else:
                return -num