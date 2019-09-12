class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(start, remaining, path):
            if len(path) == k:
                if remaining == 0:
                    ans.append(path[:])
                return
            for num in range(start, 10):
                if num > remaining:
                    break
                path.append(num)
                backtrack(num + 1, remaining - num, path)
                path.pop()

        backtrack(1, n, [])
        return ans
