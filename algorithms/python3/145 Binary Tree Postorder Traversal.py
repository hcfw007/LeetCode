class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
