from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        queue = deque([root])
        while queue:
            size = len(queue)
            total = 0
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(total / size)
        return ans
