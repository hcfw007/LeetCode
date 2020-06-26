class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                total += node.val
            if node.left and node.val > low:
                stack.append(node.left)
            if node.right and node.val < high:
                stack.append(node.right)
        return total
