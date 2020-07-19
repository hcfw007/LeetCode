class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        info = {}

        def dfs(node, parent, depth):
            if node is None:
                return
            if node.val in (x, y):
                info[node.val] = (parent, depth)
            dfs(node.left, node.val, depth + 1)
            dfs(node.right, node.val, depth + 1)

        dfs(root, None, 0)
        if x not in info or y not in info:
            return False
        px, dx = info[x]
        py, dy = info[y]
        return dx == dy and px != py
