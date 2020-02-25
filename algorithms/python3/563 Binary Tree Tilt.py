class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total = 0

        def helper(node):
            nonlocal total
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            total += abs(left - right)
            return left + right + node.val

        helper(root)
        return total
