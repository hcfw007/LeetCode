class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = None
        best = float('inf')
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev is not None:
                best = min(best, node.val - prev)
            prev = node.val
            node = node.right
        return best
