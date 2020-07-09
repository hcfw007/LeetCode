class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != val:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True
