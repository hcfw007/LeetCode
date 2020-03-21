class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def depth(node):
            if node is None:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        h = depth(root)
        width = (1 << h) - 1
        res = [[""] * width for _ in range(h)]

        def place(node, r, lo, hi):
            if node is None:
                return
            mid = (lo + hi) // 2
            res[r][mid] = str(node.val)
            place(node.left, r + 1, lo, mid)
            place(node.right, r + 1, mid + 1, hi)

        place(root, 0, 0, width)
        return res
