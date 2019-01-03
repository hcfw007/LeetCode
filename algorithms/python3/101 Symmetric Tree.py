class Solution:
    def isSymmetric(self, root):
        return True if (root == None) else self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if (t1 == None and t2 == None): return True
        if (t1 == None or t2 == None): return False
        return (t1.val == t2 .val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
