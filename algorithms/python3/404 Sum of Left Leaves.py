class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        total = 0
        if root.left and root.left.left is None and root.left.right is None:
            total += root.left.val
        return total + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
