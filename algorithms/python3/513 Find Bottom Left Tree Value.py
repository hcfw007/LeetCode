from collections import deque


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([root])
        ans = root.val
        while queue:
            node = queue.popleft()
            ans = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return ans
