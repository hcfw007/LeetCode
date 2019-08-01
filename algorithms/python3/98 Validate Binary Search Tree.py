class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev is not None and root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
