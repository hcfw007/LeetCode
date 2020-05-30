class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaves(node, out):
            if node is None:
                return
            if node.left is None and node.right is None:
                out.append(node.val)
                return
            leaves(node.left, out)
            leaves(node.right, out)

        a, b = [], []
        leaves(root1, a)
        leaves(root2, b)
        return a == b
