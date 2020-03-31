class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        total = 0
        stack = [id]
        while stack:
            e = emap[stack.pop()]
            total += e.importance
            stack.extend(e.subordinates)
        return total
