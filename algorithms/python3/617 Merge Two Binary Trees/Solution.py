class Solution:
    def mergeTrees(self, t1, t2):
        if (t1 == None):
            return t2
        if (t2 == None):
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1