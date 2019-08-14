class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        while root or stack:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right
        return result
