class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for src, dst in tickets:
            graph.setdefault(src, []).append(dst)
        for src in graph:
            graph[src].sort(reverse=True)
        route = []

        def visit(airport):
            while graph.get(airport):
                visit(graph[airport].pop())
            route.append(airport)

        visit("JFK")
        return route[::-1]
