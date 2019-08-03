class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        level = [root] if root else []
        while level:
            result.append([node.val for node in level])
            level = [child for node in level for child in (node.left, node.right) if child]
        return result
