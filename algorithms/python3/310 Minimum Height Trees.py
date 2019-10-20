class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1
        alive = set(range(n))
        leaves = [i for i in range(n) if degree[i] == 1]
        while len(alive) > 2:
            alive -= set(leaves)
            next_leaves = []
            for leaf in leaves:
                for nxt in adj[leaf]:
                    if nxt in alive:
                        degree[nxt] -= 1
                        if degree[nxt] == 1:
                            next_leaves.append(nxt)
            leaves = next_leaves
        return sorted(alive)
