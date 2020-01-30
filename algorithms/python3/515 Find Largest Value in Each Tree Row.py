from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = []
        queue = deque([root])
        while queue:
            size = len(queue)
            best = None
            for _ in range(size):
                node = queue.popleft()
                if best is None or node.val > best:
                    best = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(best)
        return ans
