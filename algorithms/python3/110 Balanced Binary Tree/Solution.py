class Solution:
    def isBalanced(self, root):
        depth, answer = self._is_balanced(root = root, depth = 0)
        return answer
    def _is_balanced(self, root, depth):
        if not root:
            return depth, True
        depth1 = depth2 = depth
        answer1 = answer2 = True
        if root.left:
                depth1, answer1 = self._is_balanced(root.left, depth + 1)
        if root.right:
            depth2, answer2 = self._is_balanced(root.right, depth + 1)
        if not answer2 or not answer1:
            return max(depth1, depth2), False
        return max(depth1, depth2), abs(depth2 - depth1) <= 1