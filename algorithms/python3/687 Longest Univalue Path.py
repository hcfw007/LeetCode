class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        best = 0

        def helper(node):
            nonlocal best
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            left_arrow = left + 1 if node.left and node.left.val == node.val else 0
            right_arrow = right + 1 if node.right and node.right.val == node.val else 0
            best = max(best, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        helper(root)
        return best
