class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def same(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

        def contains(node):
            if node is None:
                return False
            return same(node, subRoot) or contains(node.left) or contains(node.right)

        return contains(root)
