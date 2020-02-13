class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        best = 0

        def depth(node):
            nonlocal best
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            best = max(best, left + right)
            return 1 + max(left, right)

        depth(root)
        return best
