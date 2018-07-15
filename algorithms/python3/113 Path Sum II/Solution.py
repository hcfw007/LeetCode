class Solution:
    ansLists = []
    def pathSum(self, root, sum):
        self.ansLists = []
        if (root == None): return []
        l = [root.val]
        self.exploreTree(root, sum - root.val, l)
        return self.ansLists

    def exploreTree(self, root, sum, list):
        _list = list[:]
        if (root.left == None and root.right == None):
            if (sum == 0):
                self.ansLists.append(_list)
                return True
            else:
                return False
        else:
            if (root.left):
                _listl = _list[:]
                _listl.append(root.left.val)
                self.exploreTree(root.left, sum - root.left.val, _listl)
            if (root.right):
                _listr = _list[:]
                _listr.append(root.right.val)
                self.exploreTree(root.right, sum - root.right.val, _listr)