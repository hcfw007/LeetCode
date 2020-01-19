class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        count = {}
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count[node.val] = count.get(node.val, 0) + 1
            node = node.right
        best = max(count.values())
        return [v for v, c in count.items() if c == best]
