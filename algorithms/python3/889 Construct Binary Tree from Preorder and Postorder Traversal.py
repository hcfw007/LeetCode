class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        left_size = postorder.index(preorder[1]) + 1
        root.left = self.constructFromPrePost(preorder[1:1 + left_size], postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[1 + left_size:], postorder[left_size:-1])
        return root
