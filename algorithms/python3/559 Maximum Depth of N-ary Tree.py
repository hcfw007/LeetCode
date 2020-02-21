class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)
