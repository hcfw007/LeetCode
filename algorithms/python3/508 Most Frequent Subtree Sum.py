class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        count = {}

        def total(node):
            if node is None:
                return 0
            s = node.val + total(node.left) + total(node.right)
            count[s] = count.get(s, 0) + 1
            return s

        total(root)
        if not count:
            return []
        best = max(count.values())
        return [s for s, c in count.items() if c == best]
