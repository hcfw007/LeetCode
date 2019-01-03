class Solution:
    def hasPathSum(self, root, sum):
        if (root == None): return False
        return self.exploreTree(root, sum - root.val)

    def exploreTree(self, root, sum):
        if (root.left == None and root.right == None):
            if (sum == 0):
                return True
            else:
                return False
        else:
            return (root.left and self.exploreTree(root.left, sum - root.left.val)) or (root.right and self.exploreTree(root.right, sum - root.right.val)) == True