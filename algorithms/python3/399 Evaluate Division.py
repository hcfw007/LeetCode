class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (a, b), v in zip(equations, values):
            graph.setdefault(a, []).append((b, v))
            graph.setdefault(b, []).append((a, 1.0 / v))

        def query(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited = {src}
            stack = [(src, 1.0)]
            while stack:
                node, prod = stack.pop()
                for nxt, w in graph[node]:
                    if nxt == dst:
                        return prod * w
                    if nxt not in visited:
                        visited.add(nxt)
                        stack.append((nxt, prod * w))
            return -1.0

        return [query(a, b) for a, b in queries]
