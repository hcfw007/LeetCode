class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        vals = set()
        stack = [root]
        while stack:
            node = stack.pop()
            vals.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        if len(vals) < 2:
            return -1
        return sorted(vals)[1]
