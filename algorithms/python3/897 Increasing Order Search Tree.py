class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(0)
        self.cur = dummy

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            inorder(node.right)

        inorder(root)
        return dummy.right
