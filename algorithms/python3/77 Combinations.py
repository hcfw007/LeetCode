class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        def generate(current: List[int], left: List[int]) -> None:
            for i in range(len(left)):
                t = left[i]
                current.append(t)
                if len(current) == k:
                    results.append(current[:])
                else:
                    generate(current, left[i + 1:])
                current.pop()

        generate([], [i for i in range(1, n + 1)])
        return results