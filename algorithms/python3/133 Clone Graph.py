class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        clones = {}
        def clone(cur) -> 'Node':
            if cur in clones:
                return clones[cur]
            copy = Node(cur.val, [])
            clones[cur] = copy
            for neighbor in cur.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        return clone(node)
