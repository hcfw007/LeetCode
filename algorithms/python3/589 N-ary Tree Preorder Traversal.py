class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def helper(node):
            if node is None:
                return
            ans.append(node.val)
            for child in node.children:
                helper(child)

        helper(root)
        return ans
