class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def helper(node):
            if node is None:
                return
            for child in node.children:
                helper(child)
            ans.append(node.val)

        helper(root)
        return ans
