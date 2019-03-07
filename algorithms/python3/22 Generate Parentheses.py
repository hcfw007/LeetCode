class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        list = []

        def generate(current, pairs, debt):
            if pairs == 0 and debt == 0:
                list.append(current)
                return
            if pairs > 0:
                generate(current + '(', pairs - 1, debt + 1)
            if debt > 0:
                generate(current + ')', pairs, debt - 1)

        generate('', n, 0)
